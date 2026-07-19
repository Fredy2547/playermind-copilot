from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class AnalysisPlan:

    analysis_type: str

    frame_interval_seconds: float

    max_frames: int

    ai_model: str

    estimated_time_minutes: float

    estimated_cost_usd: float

    workspace: Path

    frames_folder: Path

    def __str__(self) -> str:
        return (
            "\n"
            "=====================================\n"
            " PLAYERMIND - ANALYSIS PLAN\n"
            "=====================================\n"
            f"Tipo análisis : {self.analysis_type}\n"
            f"Intervalo     : {self.frame_interval_seconds} s\n"
            f"Máx. Frames   : {self.max_frames}\n"
            f"Modelo IA     : {self.ai_model}\n"
            f"Tiempo Est.   : {self.estimated_time_minutes:.1f} min\n"
            f"Costo Est.    : USD {self.estimated_cost_usd:.2f}\n"
            f"Workspace     : {self.workspace}\n"
            f"Frames        : {self.frames_folder}\n"
            "====================================="
        )

   