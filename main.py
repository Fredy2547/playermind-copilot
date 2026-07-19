from app.services.video_inspector import VideoInspector
from app.models.analysis_plan import AnalysisPlan
from app.services.frame_extractor import FrameExtractor



def main():

    inspector = VideoInspector()

    metadata = inspector.inspect(
        "videos/Copa Metropolitana, Semifinal U17. FB. Fortaleza Vs R. Cmarca..mp4"
    )

    print(metadata)

    plan = AnalysisPlan(
        analysis_type="summary",
        frame_interval_seconds=5,
        max_frames=300,
        ai_model="gemini-flash",
        estimated_time_minutes=2,
        estimated_cost_usd=0.03
    )

    extractor = FrameExtractor()

    frames = extractor.extract_frames(
    metadata,
    plan
)

    print(frames)

if __name__ == "__main__":
    main()