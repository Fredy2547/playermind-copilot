import json
from pathlib import Path


class VideoIndex:

    def __init__(self, videos_folder: str = "videos"):

        self.index_file = Path(videos_folder) / "index.json"

    def load(self) -> dict:

        with open(self.index_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data: dict) -> None:

        with open(self.index_file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def get(self, video_id: str):

        data = self.load()
        return data.get(video_id)

    def put(self, video_id: str, metadata: dict):

        data = self.load()
        data[video_id] = metadata
        self.save(data)

    def contains(self, video_id: str) -> bool:

        return self.get(video_id) is not None

    def remove(self, video_id: str):

        data = self.load()

        if video_id in data:
            del data[video_id]
            self.save(data)