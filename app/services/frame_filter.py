import cv2

from app.models.frame_collection import FrameCollection


class FrameFilter:

    def __init__(
        self,
        pixel_threshold: int = 5000
    ):
        self.pixel_threshold = pixel_threshold

    def filter(
        self,
        collection: FrameCollection
    ) -> FrameCollection:

        if collection.total_frames <= 1:
            return collection

        filtered_files = []

        previous_gray = None

        for file in collection.files:

            image = cv2.imread(str(file))

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

            if previous_gray is None:

                filtered_files.append(file)
                previous_gray = gray

                continue

            diff = cv2.absdiff(
                previous_gray,
                gray
            )

            _, threshold = cv2.threshold(
                diff,
                30,
                255,
                cv2.THRESH_BINARY
            )

            changed_pixels = cv2.countNonZero(
                threshold
            )

            if changed_pixels >= self.pixel_threshold:

                filtered_files.append(file)

                previous_gray = gray

        print(
            f"FrameFilter: "
            f"{collection.total_frames} -> "
            f"{len(filtered_files)}"
        )

        return FrameCollection(
            video_title=collection.video_title,
            folder=collection.folder,
            files=filtered_files,
            frame_interval_seconds=collection.frame_interval_seconds,
            original_total_frames=collection.original_total_frames
        )
    