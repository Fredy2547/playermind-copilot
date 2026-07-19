from datetime import datetime
from pathlib import Path

from app.models.analysis_plan import AnalysisPlan
from app.models.video_metadata import VideoMetadata


class AnalysisPlanner:
    """
    Creates the analysis strategy and prepares the workspace.
    """

    def create(self, metadata: VideoMetadata) -> AnalysisPlan:

        # -----------------------------------
        # 1. Define frame interval
        # -----------------------------------

        if metadata.duration_seconds < 300:
            interval = 0.5

        elif metadata.duration_seconds < 1800:
            interval = 1.0

        else:
            interval = 2.0

        # -----------------------------------
        # 2. Estimate number of frames
        # -----------------------------------

        max_frames = int(metadata.duration_seconds / interval)

        # -----------------------------------
        # 3. Create workspace
        # -----------------------------------

        safe_title = (
            metadata.title
            .replace(" ", "_")
            .replace(".", "_")
            .lower()
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        workspace = Path("workspace") / f"{safe_title}_{timestamp}"

        frames_folder = workspace / "frames"

        workspace.mkdir(parents=True, exist_ok=True)
        frames_folder.mkdir(exist_ok=True)

        # -----------------------------------
        # 4. Create analysis plan
        # -----------------------------------

        return AnalysisPlan(
            analysis_type="soccer",
            frame_interval_seconds=interval,
            max_frames=max_frames,
            ai_model="gpt-4.1",
            estimated_time_minutes=0,
            estimated_cost_usd=0,
            workspace=workspace,
            frames_folder=frames_folder,
        )