from dataclasses import dataclass

from app.models.downloaded_video import DownloadedVideo


@dataclass(frozen=True, slots=True)
class DownloadResult:
    """
    Represents the result of a download operation.
    """

    success: bool

    video: DownloadedVideo | None

    message: str

    def __str__(self) -> str:

        status = "OK" if self.success else "ERROR"

        title = self.video.title if self.video else "-"

        file_path = self.video.file_path if self.video else "-"

        return (
            "\n"
            "=====================================\n"
            " PLAYERMIND - DOWNLOAD RESULT\n"
            "=====================================\n"
            f"Estado      : {status}\n"
            f"Título      : {title}\n"
            f"Archivo     : {file_path}\n"
            f"Mensaje     : {self.message}\n"
            "====================================="
        )