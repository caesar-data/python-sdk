# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .research import (
    ResearchResource,
    AsyncResearchResource,
    ResearchResourceWithRawResponse,
    AsyncResearchResourceWithRawResponse,
    ResearchResourceWithStreamingResponse,
    AsyncResearchResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["X402Resource", "AsyncX402Resource"]


class X402Resource(SyncAPIResource):
    @cached_property
    def research(self) -> ResearchResource:
        return ResearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> X402ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return X402ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> X402ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return X402ResourceWithStreamingResponse(self)


class AsyncX402Resource(AsyncAPIResource):
    @cached_property
    def research(self) -> AsyncResearchResource:
        return AsyncResearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncX402ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncX402ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncX402ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return AsyncX402ResourceWithStreamingResponse(self)


class X402ResourceWithRawResponse:
    def __init__(self, x402: X402Resource) -> None:
        self._x402 = x402

    @cached_property
    def research(self) -> ResearchResourceWithRawResponse:
        return ResearchResourceWithRawResponse(self._x402.research)


class AsyncX402ResourceWithRawResponse:
    def __init__(self, x402: AsyncX402Resource) -> None:
        self._x402 = x402

    @cached_property
    def research(self) -> AsyncResearchResourceWithRawResponse:
        return AsyncResearchResourceWithRawResponse(self._x402.research)


class X402ResourceWithStreamingResponse:
    def __init__(self, x402: X402Resource) -> None:
        self._x402 = x402

    @cached_property
    def research(self) -> ResearchResourceWithStreamingResponse:
        return ResearchResourceWithStreamingResponse(self._x402.research)


class AsyncX402ResourceWithStreamingResponse:
    def __init__(self, x402: AsyncX402Resource) -> None:
        self._x402 = x402

    @cached_property
    def research(self) -> AsyncResearchResourceWithStreamingResponse:
        return AsyncResearchResourceWithStreamingResponse(self._x402.research)
