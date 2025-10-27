# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResearchCreateParams"]


class ResearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """Primary research question or instruction."""

    x_payment: Required[Annotated[str, PropertyInfo(alias="X-PAYMENT")]]

    compute_units: int
    """Optional compute budget for the job. Defaults to 1."""

    system_prompt: str
    """Optional system prompt to steer the assistant."""
