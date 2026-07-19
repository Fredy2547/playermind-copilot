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

    original_total_frames: int | None = None

    @property
    def total_frames(self) -> int:
        return len(self.files)

    @property
    def discarded_frames(self) -> int:

        if self.original_total_frames is None:
            return 0

        return self.original_total_frames - self.total_frames

    @property
    def reduction_percentage(self) -> float:

        if self.original_total_frames is None:
            return 0.0

        if self.original_total_frames == 0:
            return 0.0

        return (
            self.discarded_frames / self.original_total_frames
        ) * 100

    def __str__(self):

        text = (
            "\n"
            "=====================================\n"
            " PLAYERMIND - FRAME COLLECTION\n"
            "=====================================\n"
            f"Video       : {self.video_title}\n"
            f"Carpeta     : {self.folder}\n"
            f"Imágenes    : {self.total_frames}\n"
            f"Intervalo   : {self.frame_interval_seconds} segundos\n"
        )

        if self.original_total_frames is not None:

            text += (
                f"Originales  : {self.original_total_frames}\n"
                f"Descartados : {self.discarded_frames}\n"
                f"Reducción   : {self.reduction_percentage:.1f}%\n"
            )

        text += "====================================="

        return text