from dataclasses import dataclass
from pathlib import Path


@dataclass
class FrameCollection:
    """
    Representa el conjunto de imágenes extraídas de un video.
    """

    video_title: str

    folder: Path

    files: list[Path]

    frame_interval_seconds: int

    @property
    def total_frames(self) -> int:
        return len(self.files)

    def __str__(self):

        return (
            "\n"
            "=====================================\n"
            " PLAYERMIND - FRAME COLLECTION\n"
            "=====================================\n"
            f"Video       : {self.video_title}\n"
            f"Carpeta     : {self.folder}\n"
            f"Imágenes    : {self.total_frames}\n"
            f"Intervalo   : {self.frame_interval_seconds} segundos\n"
            "====================================="
        )