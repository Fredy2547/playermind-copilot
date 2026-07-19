from dataclasses import dataclass
from pathlib import Path


@dataclass
class VideoMetadata:
    """
    Información básica de un video.
    """

    title: str
    source: str
    path: Path

    duration_seconds: float

    fps: float
    
    total_frames: int

    width: int

    height: int

    size_mb: float

    @property
    def resolution(self) -> str:
        return f"{self.width}x{self.height}"
    
    @property
    def duration_minutes(self) -> float:
        return round(self.duration_seconds / 60, 2)
    
    def __str__(self):

        return (
        "\n"
        "=====================================\n"
        " PLAYERMIND - VIDEO INSPECTOR\n"
        "=====================================\n"
        f"Título      : {self.title}\n"
        f"Origen      : {self.source}\n"
        f"Duración    : {self.duration_minutes} minutos\n"
        f"Resolución  : {self.resolution}\n"
        f"FPS         : {self.fps}\n"
        f"Frames      : {self.total_frames:,}\n"
        f"Tamaño      : {self.size_mb:.2f} MB\n"
        "====================================="
    )