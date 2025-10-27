# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.x402 import research_create_params
from ..._base_client import make_request_options
from ...types.x402.research_create_response import ResearchCreateResponse

__all__ = ["ResearchResource", "AsyncResearchResource"]


class ResearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return ResearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        x_payment: str,
        compute_units: int | Omit = omit,
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """Start a new research job using x402 payment.

        This endpoint mints a temporary API
        key that is returned in the response and is billed via the x402 settlement flow
        instead of your Caesar API credits.

        Args:
          query: Primary research question or instruction.

          compute_units: Optional compute budget for the job. Defaults to 1.

          system_prompt: Optional system prompt to steer the assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"X-PAYMENT": x_payment, **(extra_headers or {})}
        return self._post(
            "/x402/research",
            body=maybe_transform(
                {
                    "query": query,
                    "compute_units": compute_units,
                    "system_prompt": system_prompt,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )


class AsyncResearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return AsyncResearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        x_payment: str,
        compute_units: int | Omit = omit,
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """Start a new research job using x402 payment.

        This endpoint mints a temporary API
        key that is returned in the response and is billed via the x402 settlement flow
        instead of your Caesar API credits.

        Args:
          query: Primary research question or instruction.

          compute_units: Optional compute budget for the job. Defaults to 1.

          system_prompt: Optional system prompt to steer the assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"X-PAYMENT": x_payment, **(extra_headers or {})}
        return await self._post(
            "/x402/research",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "compute_units": compute_units,
                    "system_prompt": system_prompt,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )


class ResearchResourceWithRawResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_raw_response_wrapper(
            research.create,
        )


class AsyncResearchResourceWithRawResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_raw_response_wrapper(
            research.create,
        )


class ResearchResourceWithStreamingResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_streamed_response_wrapper(
            research.create,
        )


class AsyncResearchResourceWithStreamingResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_streamed_response_wrapper(
            research.create,
        )
