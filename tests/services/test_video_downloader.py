downloader = VideoDownloader()

video = downloader.download(URL)

assert isinstance(video, DownloadedVideo)