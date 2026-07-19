from pathlib import Path

import cv2

from app.models.analysis_plan import AnalysisPlan
from app.models.frame_collection import FrameCollection


class FrameExtractor:

    def extract(
        self,
        video_path: Path,
        plan: AnalysisPlan
    ) -> FrameCollection:

        cap = cv2.VideoCapture(str(video_path))

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_step = max(
            1,
            int(fps * plan.frame_interval_seconds)
        )

        saved_files = []

        frame_number = 0
        extracted = 0

        while True:

            success, frame = cap.read()

            if not success:
                break

            if frame_number % frame_step == 0:

                second = frame_number / fps

                filename = (
                    f"frame_{extracted + 1:06d}_{second:06.1f}s.jpg"
                )

                output_file = plan.frames_folder / filename

                cv2.imwrite(str(output_file), frame)

                saved_files.append(output_file)

                extracted += 1

            frame_number += 1

        cap.release()

        return FrameCollection(
            video_title=video_path.stem,
            folder=plan.frames_folder,
            files=saved_files,
            frame_interval_seconds=plan.frame_interval_seconds,
            original_total_frames=extracted
        )