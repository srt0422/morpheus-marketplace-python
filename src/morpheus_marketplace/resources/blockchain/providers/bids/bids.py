# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .active import (
    ActiveResource,
    AsyncActiveResource,
    ActiveResourceWithRawResponse,
    AsyncActiveResourceWithRawResponse,
    ActiveResourceWithStreamingResponse,
    AsyncActiveResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.shared.bid import Bid
from .....types.blockchain.providers import bid_list_params

__all__ = ["BidsResource", "AsyncBidsResource"]


class BidsResource(SyncAPIResource):
    @cached_property
    def active(self) -> ActiveResource:
        return ActiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> BidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return BidsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Retrieves bids placed by a specific provider.

        Args:
          limit: Limit for pagination.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/blockchain/providers/{id}/bids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    bid_list_params.BidListParams,
                ),
            ),
            cast_to=Bid,
        )


class AsyncBidsResource(AsyncAPIResource):
    @cached_property
    def active(self) -> AsyncActiveResource:
        return AsyncActiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBidsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Retrieves bids placed by a specific provider.

        Args:
          limit: Limit for pagination.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/blockchain/providers/{id}/bids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    bid_list_params.BidListParams,
                ),
            ),
            cast_to=Bid,
        )


class BidsResourceWithRawResponse:
    def __init__(self, bids: BidsResource) -> None:
        self._bids = bids

        self.list = to_raw_response_wrapper(
            bids.list,
        )

    @cached_property
    def active(self) -> ActiveResourceWithRawResponse:
        return ActiveResourceWithRawResponse(self._bids.active)


class AsyncBidsResourceWithRawResponse:
    def __init__(self, bids: AsyncBidsResource) -> None:
        self._bids = bids

        self.list = async_to_raw_response_wrapper(
            bids.list,
        )

    @cached_property
    def active(self) -> AsyncActiveResourceWithRawResponse:
        return AsyncActiveResourceWithRawResponse(self._bids.active)


class BidsResourceWithStreamingResponse:
    def __init__(self, bids: BidsResource) -> None:
        self._bids = bids

        self.list = to_streamed_response_wrapper(
            bids.list,
        )

    @cached_property
    def active(self) -> ActiveResourceWithStreamingResponse:
        return ActiveResourceWithStreamingResponse(self._bids.active)


class AsyncBidsResourceWithStreamingResponse:
    def __init__(self, bids: AsyncBidsResource) -> None:
        self._bids = bids

        self.list = async_to_streamed_response_wrapper(
            bids.list,
        )

    @cached_property
    def active(self) -> AsyncActiveResourceWithStreamingResponse:
        return AsyncActiveResourceWithStreamingResponse(self._bids.active)
