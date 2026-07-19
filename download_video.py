from app.services.video_downloader import VideoDownloader
from app.infrastructure.system_tools import SystemTools


def main():
    downloader = VideoDownloader()

    print("Deno:", SystemTools.find_deno())
    print("FFmpeg :", SystemTools.find_ffmpeg())

    url = input("Ingrese la URL del video: ")

    downloader = VideoDownloader()

    result = downloader.download(url)

    print(result)


if __name__ == "__main__":
    main()