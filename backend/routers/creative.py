from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from services.openai_service import analyze_creative_for_targeting, transcribe_video
from services.media_utils import (
    extract_video_storyboard,
    process_uploaded_file,
    encode_image_to_base64
)
from data.facebook_india_targeting import (
    REAL_META_INTERESTS,
    REAL_META_BEHAVIORS,
    CITY_TIERS,
    AGE_CLUSTERS,
    AD_PLACEMENTS
)

router = APIRouter(prefix="/api", tags=["Campaign Optimizer"])


@router.post("/campaign-optimizer")
async def campaign_optimizer(
    creative: UploadFile = File(...)
):
    if not creative or not creative.filename:
        raise HTTPException(status_code=400, detail="Creative file is required.")

    file_bytes = await creative.read()
    content_type = creative.content_type or "image/jpeg"
    is_video = "video" in content_type

    # ── Step 1: Extract frames ───────────────────────────────
    if is_video:
        frame_bytes_list = extract_video_storyboard(file_bytes, num_frames=4)
        if not frame_bytes_list:
            raise HTTPException(
                status_code=400,
                detail="Could not extract frames from video. Try MP4 or MOV format."
            )
    else:
        single = process_uploaded_file(file_bytes, content_type)
        if not single:
            raise HTTPException(status_code=400, detail="Could not process image.")
        frame_bytes_list = [single]

    frame_b64_list = [encode_image_to_base64(f) for f in frame_bytes_list]

    # ── Step 2: Transcribe if video ──────────────────────────
    transcript = ""
    if is_video:
        transcript = await transcribe_video(file_bytes, filename=creative.filename or "video.mp4")

    # ── Step 3: AI analysis ──────────────────────────────────
    ai_result = await analyze_creative_for_targeting(
        frame_b64_list=frame_b64_list,
        transcript=transcript,
        is_video=is_video
    )

    return JSONResponse({
        "ai_analysis": ai_result,
        "transcript": transcript,
        "is_video": is_video,
        "frames_analyzed": len(frame_b64_list),
        "status": "success"
    })


@router.get("/targeting-data")
async def get_targeting_data():
    return JSONResponse({
        "interest_categories": REAL_META_INTERESTS,
        "behaviors": REAL_META_BEHAVIORS,
        "city_tiers": CITY_TIERS,
        "age_clusters": AGE_CLUSTERS,
        "ad_placements": AD_PLACEMENTS,
        "status": "success"
    })
