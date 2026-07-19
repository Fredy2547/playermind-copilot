from dataclasses import dataclass, field

from app.models.frame_analysis import FrameAnalysis


@dataclass(slots=True)
class AnalysisResult:

    frames: list[FrameAnalysis] = field(default_factory=list)

    model: str = ""

    processing_time_seconds: float = 0

    total_cost_usd: float = 0

    @property
    def total_frames(self) -> int:
        return len(self.frames)

    def __str__(self):

        return (
            "\n"
            "=====================================\n"
            " PLAYERMIND - ANALYSIS RESULT\n"
            "=====================================\n"
            f"Frames Analizados : {self.total_frames}\n"
            f"Modelo IA         : {self.model}\n"
            f"Tiempo            : {self.processing_time_seconds:.2f} s\n"
            f"Costo             : USD {self.total_cost_usd:.4f}\n"
            "====================================="
        )