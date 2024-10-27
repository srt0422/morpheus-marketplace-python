# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.blockchain import bid_create_params, bid_session_params
from ...types.shared.session import Session
from ...types.blockchain.bid_create_response import BidCreateResponse
from ...types.blockchain.bid_delete_response import BidDeleteResponse
from ...types.blockchain.bid_retrieve_response import BidRetrieveResponse

__all__ = ["BidsResource", "AsyncBidsResource"]


class BidsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return BidsResourceWithStreamingResponse(self)

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
    ) -> BidCreateResponse:
        """
        Places a bid for a model on the blockchain.

        Args:
          model_id: ID of the model the bid is associated with.

          price_per_second: Price per second of model usage.

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
                bid_create_params.BidCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BidCreateResponse,
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
    ) -> BidRetrieveResponse:
        """
        Retrieves bid details by its ID.

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
            cast_to=BidRetrieveResponse,
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
    ) -> BidDeleteResponse:
        """
        Removes a bid from the blockchain by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BidDeleteResponse,
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
        Opens a session based on a specific bid ID, linking the provider and model via a
        bid.

        Args:
          session_duration: The duration of the session in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/blockchain/bids/{id}/session",
            body=maybe_transform({"session_duration": session_duration}, bid_session_params.BidSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class AsyncBidsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBidsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBidsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBidsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBidsResourceWithStreamingResponse(self)

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
    ) -> BidCreateResponse:
        """
        Places a bid for a model on the blockchain.

        Args:
          model_id: ID of the model the bid is associated with.

          price_per_second: Price per second of model usage.

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
                bid_create_params.BidCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BidCreateResponse,
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
    ) -> BidRetrieveResponse:
        """
        Retrieves bid details by its ID.

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
            cast_to=BidRetrieveResponse,
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
    ) -> BidDeleteResponse:
        """
        Removes a bid from the blockchain by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/blockchain/bids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BidDeleteResponse,
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
        Opens a session based on a specific bid ID, linking the provider and model via a
        bid.

        Args:
          session_duration: The duration of the session in seconds.

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
                {"session_duration": session_duration}, bid_session_params.BidSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class BidsResourceWithRawResponse:
    def __init__(self, bids: BidsResource) -> None:
        self._bids = bids

        self.create = to_raw_response_wrapper(
            bids.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bids.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            bids.delete,
        )
        self.session = to_raw_response_wrapper(
            bids.session,
        )


class AsyncBidsResourceWithRawResponse:
    def __init__(self, bids: AsyncBidsResource) -> None:
        self._bids = bids

        self.create = async_to_raw_response_wrapper(
            bids.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bids.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            bids.delete,
        )
        self.session = async_to_raw_response_wrapper(
            bids.session,
        )


class BidsResourceWithStreamingResponse:
    def __init__(self, bids: BidsResource) -> None:
        self._bids = bids

        self.create = to_streamed_response_wrapper(
            bids.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bids.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            bids.delete,
        )
        self.session = to_streamed_response_wrapper(
            bids.session,
        )


class AsyncBidsResourceWithStreamingResponse:
    def __init__(self, bids: AsyncBidsResource) -> None:
        self._bids = bids

        self.create = async_to_streamed_response_wrapper(
            bids.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bids.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            bids.delete,
        )
        self.session = async_to_streamed_response_wrapper(
            bids.session,
        )
