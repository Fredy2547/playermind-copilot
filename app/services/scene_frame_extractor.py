from pathlib import Path

import cv2
from scenedetect import SceneManager, open_video
from scenedetect.detectors import ContentDetector

from app.models.downloaded_video import DownloadedVideo
from app.models.frame_collection import FrameCollection

"""
Experimental extractor based on PySceneDetect.

Result:
Not suitable for continuous soccer matches.
Kept for future research.
"""

class SceneFrameExtractor:

    def __init__(
        self,
        output_folder: str = "workspace",
        threshold: float = 27.0
    ):
        self.output_folder = Path(output_folder)
        self.threshold = threshold

    def extract(
        self,
        video: DownloadedVideo
    ) -> FrameCollection:

        scene_manager = SceneManager()
        scene_manager.add_detector(
            ContentDetector(threshold=self.threshold)
        )

        video_stream = open_video(str(video.file_path))

        scene_manager.detect_scenes(video_stream)

        scenes = scene_manager.get_scene_list()

        print()
        print("=====================================")
        print(" PLAYERMIND - SCENE DETECTOR")
        print("=====================================")
        print(f"Escenas detectadas : {len(scenes)}")
        print("=====================================")
        print()

        folder = (
            self.output_folder
            / video.file_path.stem
            / "scene_frames"
        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        capture = cv2.VideoCapture(
            str(video.file_path)
        )

        files = []

        for index, scene in enumerate(scenes, start=1):

            start = scene[0].get_frames()
            end = scene[1].get_frames()

            middle = int((start + end) / 2)

            capture.set(
                cv2.CAP_PROP_POS_FRAMES,
                middle
            )

            ok, frame = capture.read()

            if not ok:
                continue

            file = folder / f"scene_{index:04}.jpg"

            cv2.imwrite(
                str(file),
                frame
            )

            files.append(file)

        capture.release()

        return FrameCollection(
            video_title=video.title,
            folder=folder,
            files=files,
            frame_interval_seconds=0,
            original_total_frames=len(files)
        )