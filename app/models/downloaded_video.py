from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class DownloadedVideo:
    """Represents a successfully downloaded video."""
    
    video_id: str
    url: str
    title: str
    file_path: Path

    @property
    def youtube_url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.video_id}"
