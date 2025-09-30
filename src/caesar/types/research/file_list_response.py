# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FileListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Unique identifier for the file."""

    content_type: str
    """MIME type of the file as detected/stored."""

    file_name: str
    """Original uploaded filename."""


class Pagination(BaseModel):
    has_next: bool
    """Whether another page is available."""

    limit: int
    """Page size (items per page)."""

    page: int
    """Current page number (1-based)."""

    total: Optional[int] = None
    """Total number of items (may be omitted)."""


class FileListResponse(BaseModel):
    data: List[Data]
    """List of file objects."""

    pagination: Pagination
