from pathlib import Path
import cv2

from app.models.video_metadata import VideoMetadata


class VideoInspector:

    def inspect(self, video_path: str) -> VideoMetadata:

        path = Path(video_path)

        cap = cv2.VideoCapture(str(path))

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        duration = frame_count / fps if fps > 0 else 0

        cap.release()

        size_mb = path.stat().st_size / (1024 * 1024)

        return VideoMetadata(
            title=path.stem,
            source="local",
            path=path,
            duration_seconds=duration,
            fps=fps,
            total_frames=frame_count,
            width=width,
            height=height,
            size_mb=size_mb 
        )