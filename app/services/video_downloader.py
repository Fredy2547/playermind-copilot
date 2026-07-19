from pathlib import Path

from yt_dlp import YoutubeDL

from app.infrastructure.system_tools import SystemTools
from app.models.download_result import DownloadResult
from app.models.downloaded_video import DownloadedVideo
from app.services.video_index import VideoIndex


class VideoDownloader:
    """
    Downloads videos using yt-dlp.
    """

    def __init__(self, output_folder: Path | str = "videos"):
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

        self.video_index = VideoIndex()

    def _build_options(self) -> dict:

        options = {
            "format": "best[ext=mp4]/best",
            "outtmpl": str(self.output_folder / "%(title)s.%(ext)s"),
        }

        deno_path = SystemTools.find_deno()

        if deno_path:
            options["js_runtimes"] = {
                "deno": {
                    "path": deno_path
                }
            }
            options["remote_components"] = [
                "ejs:github"
            ]

        return options

    def download(self, url: str) -> DownloadResult:

        options = self._build_options()

        with YoutubeDL(options) as ydl:

            # Obtener la información del video SIN descargarlo
            info = ydl.extract_info(url, download=False)

            video_id = info["id"]

            # Buscar en el índice
            cached = self.video_index.get(video_id)

            if cached:

                file_path = self.output_folder / cached["file_name"]

                # Verificar que el archivo realmente exista
                if file_path.exists():

                    video = DownloadedVideo(
                        video_id=video_id,
                        url=url,
                        title=cached["title"],
                        file_path=file_path
                    )

                    return DownloadResult(
                        success=True,
                        video=video,
                        message="Video recuperado del caché."
                    )

            # El video no existe, descargarlo
            info = ydl.extract_info(url, download=True)

            video = DownloadedVideo(
                video_id=video_id,
                url=url,
                title=info["title"],
                file_path=Path(ydl.prepare_filename(info))
            )

            self.video_index.put(
                video_id,
                {
                    "title": video.title,
                    "file_name": video.file_path.name
                }
            )

            return DownloadResult(
                success=True,
                video=video,
                message="Video descargado correctamente."
            )