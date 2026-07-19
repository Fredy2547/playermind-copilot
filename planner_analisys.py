from app.services.analysis_planner import AnalysisPlanner
from app.services.frame_analyzer import FrameAnalyzer
from app.services.frame_extractor import FrameExtractor
from app.services.video_downloader import VideoDownloader
from app.services.video_inspector import VideoInspector

def main():

    url = input("Ingrese la URL del video: ")

    # ---------------------------------
    # 1. Descargar video
    # ---------------------------------

    downloader = VideoDownloader()
    download = downloader.download(url)

    print(download)

    if not download.success:
        return

    # ---------------------------------
    # 2. Inspeccionar video
    # ---------------------------------

    inspector = VideoInspector()
    metadata = inspector.inspect(download.video.file_path)

    print(metadata)

    # ---------------------------------
    # 3. Crear plan de análisis
    # ---------------------------------

    planner = AnalysisPlanner()
    plan = planner.create(metadata)

    print(plan)

    # ---------------------------------
    # 4. Extraer frames
    # ---------------------------------

    extractor = FrameExtractor()
    frame_collection = extractor.extract(
        download.video.file_path,
        plan
    )

    print(frame_collection)

     # ---------------------------------
    # 5. Analizar frames
    # ---------------------------------

    analyzer = FrameAnalyzer()

    analysis_result = analyzer.analyze(
        frame_collection
    )

    print(analysis_result)


if __name__ == "__main__":
    main()