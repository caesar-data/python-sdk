# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResearchCreateResponse"]


class ResearchCreateResponse(BaseModel):
    id: str
    """Research job identifier."""

    status: Literal["queued", "searching", "summarizing", "analyzing", "completed", "failed", "researching"]
    """Current status of the research job."""

    api_key_secret: Optional[str] = None
    """Temporary API key secret created for this x402 request."""
