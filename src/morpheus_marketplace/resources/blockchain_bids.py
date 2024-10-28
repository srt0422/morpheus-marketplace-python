# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import blockchain_bid_create_params, blockchain_bid_session_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.bid import Bid
from ..types.shared.session import Session

__all__ = ["BlockchainBidsResource", "AsyncBlockchainBidsResource"]


class BlockchainBidsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockchainBidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BlockchainBidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockchainBidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return BlockchainBidsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model_id: str,
        price_per_second: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Create a new bid

        Args:
          model_id: ID of the model to bid on

          price_per_second: Bid price per second

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/bids",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "price_per_second": price_per_second,
                },
                blockchain_bid_create_params.BlockchainBidCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bid,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Retrieve a bid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bid,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a bid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def session(
        self,
        id: str,
        *,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a session for a bid

        Args:
          session_duration: Duration of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/blockchain/bids/{id}/session",
            body=maybe_transform(
                {"session_duration": session_duration}, blockchain_bid_session_params.BlockchainBidSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class AsyncBlockchainBidsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockchainBidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockchainBidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockchainBidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBlockchainBidsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model_id: str,
        price_per_second: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Create a new bid

        Args:
          model_id: ID of the model to bid on

          price_per_second: Bid price per second

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/bids",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "price_per_second": price_per_second,
                },
                blockchain_bid_create_params.BlockchainBidCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bid,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bid:
        """
        Retrieve a bid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bid,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a bid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def session(
        self,
        id: str,
        *,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a session for a bid

        Args:
          session_duration: Duration of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/blockchain/bids/{id}/session",
            body=await async_maybe_transform(
                {"session_duration": session_duration}, blockchain_bid_session_params.BlockchainBidSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class BlockchainBidsResourceWithRawResponse:
    def __init__(self, blockchain_bids: BlockchainBidsResource) -> None:
        self._blockchain_bids = blockchain_bids

        self.create = to_raw_response_wrapper(
            blockchain_bids.create,
        )
        self.retrieve = to_raw_response_wrapper(
            blockchain_bids.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            blockchain_bids.delete,
        )
        self.session = to_raw_response_wrapper(
            blockchain_bids.session,
        )


class AsyncBlockchainBidsResourceWithRawResponse:
    def __init__(self, blockchain_bids: AsyncBlockchainBidsResource) -> None:
        self._blockchain_bids = blockchain_bids

        self.create = async_to_raw_response_wrapper(
            blockchain_bids.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            blockchain_bids.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            blockchain_bids.delete,
        )
        self.session = async_to_raw_response_wrapper(
            blockchain_bids.session,
        )


class BlockchainBidsResourceWithStreamingResponse:
    def __init__(self, blockchain_bids: BlockchainBidsResource) -> None:
        self._blockchain_bids = blockchain_bids

        self.create = to_streamed_response_wrapper(
            blockchain_bids.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            blockchain_bids.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            blockchain_bids.delete,
        )
        self.session = to_streamed_response_wrapper(
            blockchain_bids.session,
        )


class AsyncBlockchainBidsResourceWithStreamingResponse:
    def __init__(self, blockchain_bids: AsyncBlockchainBidsResource) -> None:
        self._blockchain_bids = blockchain_bids

        self.create = async_to_streamed_response_wrapper(
            blockchain_bids.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            blockchain_bids.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            blockchain_bids.delete,
        )
        self.session = async_to_streamed_response_wrapper(
            blockchain_bids.session,
        )
