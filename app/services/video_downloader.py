from pathlib import Path
from yt_dlp import YoutubeDL
from app.infrastructure.system_tools import SystemTools
from app.models.download_result import DownloadResult
from app.models.downloaded_video import DownloadedVideo



class VideoDownloader:
    """
     Downloads videos using yt-dlp.
    """
 
    def __init__(self, output_folder: Path | str = "videos"):
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
    
   

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
            options["remote_components"]  = [  
                 "ejs:github"
            ]
            

        return options

    def download(self, url: str) -> DownloadResult:

        options = self._build_options()

        with YoutubeDL(options) as ydl:

            info = ydl.extract_info(url, download=True)

            video = DownloadedVideo(
                url=url,
                title=info["title"],
                file_path=Path(ydl.prepare_filename(info))
            )

            return DownloadResult(
                success=True,
                video=video,
                message="Video descargado correctamente."
            )