from time import perf_counter

from app.models.analysis_result import AnalysisResult
from app.models.frame_analysis import FrameAnalysis
from app.models.frame_collection import FrameCollection


class FrameAnalyzer:

    def analyze(self, collection: FrameCollection) -> AnalysisResult:

        start = perf_counter()

        result = AnalysisResult()

        for index, frame in enumerate(collection.files):

            analysis = FrameAnalysis(
                frame_path=frame,
                timestamp_seconds=index * collection.frame_interval_seconds,
                description="Pendiente de análisis por IA",
                detected_objects=[],
                confidence=0.0,
            )

            result.frames.append(analysis)

        result.processing_time_seconds = perf_counter() - start

        return result