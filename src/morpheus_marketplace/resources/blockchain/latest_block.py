# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.blockchain.latest_block import LatestBlock

__all__ = ["LatestBlockResource", "AsyncLatestBlockResource"]


class LatestBlockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LatestBlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return LatestBlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LatestBlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return LatestBlockResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestBlock:
        """Retrieves the latest block number from the blockchain."""
        return self._get(
            "/blockchain/latestBlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LatestBlock,
        )


class AsyncLatestBlockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLatestBlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLatestBlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLatestBlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncLatestBlockResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestBlock:
        """Retrieves the latest block number from the blockchain."""
        return await self._get(
            "/blockchain/latestBlock",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LatestBlock,
        )


class LatestBlockResourceWithRawResponse:
    def __init__(self, latest_block: LatestBlockResource) -> None:
        self._latest_block = latest_block

        self.retrieve = to_raw_response_wrapper(
            latest_block.retrieve,
        )


class AsyncLatestBlockResourceWithRawResponse:
    def __init__(self, latest_block: AsyncLatestBlockResource) -> None:
        self._latest_block = latest_block

        self.retrieve = async_to_raw_response_wrapper(
            latest_block.retrieve,
        )


class LatestBlockResourceWithStreamingResponse:
    def __init__(self, latest_block: LatestBlockResource) -> None:
        self._latest_block = latest_block

        self.retrieve = to_streamed_response_wrapper(
            latest_block.retrieve,
        )


class AsyncLatestBlockResourceWithStreamingResponse:
    def __init__(self, latest_block: AsyncLatestBlockResource) -> None:
        self._latest_block = latest_block

        self.retrieve = async_to_streamed_response_wrapper(
            latest_block.retrieve,
        )
