import structlog
from fastapi import APIRouter, HTTPException

from app.schemas.estimation import EstimationRequest
from app.services.llm_service import LLMServiceError, generate_estimation

log = structlog.get_logger()

router = APIRouter(prefix="/api/v1", tags=["estimations"])


@router.post("/estimate", response_model=None)
async def create_estimation(request: EstimationRequest) -> dict:
    """Receive a meeting transcription and return a software project estimation."""
    try:
        result = generate_estimation(request.transcription)
    except LLMServiceError as exc:
        log.error("estimation_endpoint_error", error=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))

    return result