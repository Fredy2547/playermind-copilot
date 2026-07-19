from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class DownloadedVideo:
    """Represents a successfully downloaded video."""
    
    url: str
    title: str
    file_path: Path
