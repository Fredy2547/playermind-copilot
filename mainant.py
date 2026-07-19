from app.services.video_downloader import VideoDownloader
from app.models.analysis_plan import AnalysisPlan


def main():

    # Prueba del modelo AnalysisPlan
    plan = AnalysisPlan(
        analysis_type="summary",
        frame_interval_seconds=5,
        max_frames=300,
        ai_model="gemini-flash",
        estimated_time_minutes=2,
        estimated_cost_usd=0.03
    )

    print(plan)
    print(plan.is_fast_analysis)

    # Downloader
    url = input("\nIngrese la URL del partido: ")

    downloader = VideoDownloader()

    downloader.download(url)


if __name__ == "__main__":
    main()