from pydantic import BaseModel, Field


class EstimationRequest(BaseModel):
    """Request body for generating a project estimation."""

    transcription: str = Field(..., min_length=1)
