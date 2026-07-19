from pathlib import Path

from app.models.downloaded_video import DownloadedVideo


def test_create_downloaded_video():

    video = DownloadedVideo(
        url="https://youtu.be/123",
        title="My Match",
        file_path=Path("videos/match.mp4"),
    )

    assert video.url == "https://youtu.be/123"
    assert video.title == "My Match"
    assert video.file_path == Path("videos/match.mp4")