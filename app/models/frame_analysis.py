from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class FrameAnalysis:

    frame_path: Path

    timestamp_seconds: float

    description: str

    detected_objects: list[str]

    confidence: float