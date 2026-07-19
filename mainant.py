from time import perf_counter

from app.services.analysis_planner import AnalysisPlanner
from app.services.frame_analyzer import FrameAnalyzer
## from app.services.frame_extractor import FrameExtractor
## from app.services.frame_filter import FrameFilter
from app.services.frame_extractor import FrameExtractor
from app.services.video_downloader import VideoDownloader
from app.services.video_inspector import VideoInspector
from app.services.scene_frame_extractor import SceneFrameExtractor


def main():

    total_start = perf_counter()

    url = input("Ingrese la URL del video: ")

    # ---------------------------------
    # 1. Descargar video
    # ---------------------------------

    start = perf_counter()

    downloader = VideoDownloader()
    download = downloader.download(url)

    download_time = perf_counter() - start

    print(download.message)

    if not download.success:
        return

    # ---------------------------------
    # 2. Inspeccionar video
    # ---------------------------------

    start = perf_counter()

    inspector = VideoInspector()
    metadata = inspector.inspect(download.video.file_path)

    inspect_time = perf_counter() - start

    print(metadata)

    # ---------------------------------
    # 3. Crear plan
    # ---------------------------------

    start = perf_counter()

    planner = AnalysisPlanner()
    plan = planner.create(metadata)

    planning_time = perf_counter() - start

    print(plan)

    # ---------------------------------
    # 4. Extraer frames  - Detectar escenas
    # ---------------------------------

    start = perf_counter()

    extractor = FrameExtractor()

    original_collection = extractor.extract(
        download.video.file_path,
        plan
    )


    extraction_time = perf_counter() - start

    print("\nESCENAS DETECTADAS")
    print(original_collection)

    # ---------------------------------
    # 5. Filtrar frames
    # ---------------------------------

    start = perf_counter()

    
    frame_filter = FrameFilter(pixel_threshold=5000)

    filtered_collection = frame_filter.filter(
        original_collection
    )

    ##filtering_time = perf_counter() - start

    print("\nDESPUÉS DEL FILTRO")
    print(filtered_collection)

    # ---------------------------------
    # 6. Analizar frames
    # ---------------------------------

    start = perf_counter()

    analyzer = FrameAnalyzer()

    analysis_result = analyzer.analyze(
        filtered_collection
    )

    analysis_time = perf_counter() - start

    print(analysis_result)

    # ---------------------------------
    # Resumen
    # ---------------------------------

    total_time = perf_counter() - total_start

    print("\n=====================================")
    print(" PLAYERMIND - RESUMEN")
    print("=====================================")
    print(f"Frames originales : {original_collection.total_frames}")
    print(f"Frames filtrados  : {filtered_collection.total_frames}")
    print(f"Descartados       : {filtered_collection.discarded_frames}")
    print(f"Reducción         : {filtered_collection.reduction_percentage:.1f}%")
    print("=====================================")

    print("\n=====================================")
    print(" PLAYERMIND - PERFORMANCE")
    print("=====================================")
    print(f"Descarga video    : {download_time:8.2f} s")
    print(f"Inspección video  : {inspect_time:8.2f} s")
    print(f"Planificación     : {planning_time:8.2f} s")
    print(f"Extracción frames : {extraction_time:8.2f} s")
    print(f"Filtro frames     : {filtering_time:8.2f} s")
    print(f"Análisis IA       : {analysis_time:8.2f} s")
    print("-------------------------------------")
    print(f"TOTAL             : {total_time:8.2f} s")
    print("=====================================")


if __name__ == "__main__":
    main()