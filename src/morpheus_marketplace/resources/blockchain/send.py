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
from ...types.blockchain import send_eth_params, send_mor_params
from ...types.blockchain.send_eth_response import SendEthResponse
from ...types.blockchain.send_mor_response import SendMorResponse

__all__ = ["SendResource", "AsyncSendResource"]


class SendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return SendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return SendResourceWithStreamingResponse(self)

    def eth(
        self,
        *,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendEthResponse:
        """
        Transfers ETH to a specified address.

        Args:
          amount: Amount of ETH to be transferred.

          to: Recipient ETH address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/send/eth",
            body=maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                send_eth_params.SendEthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendEthResponse,
        )

    def mor(
        self,
        *,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendMorResponse:
        """
        Transfers MOR tokens to a specified address.

        Args:
          amount: Amount of MOR tokens to be transferred.

          to: Recipient ETH address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/send/mor",
            body=maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                send_mor_params.SendMorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendMorResponse,
        )


class AsyncSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncSendResourceWithStreamingResponse(self)

    async def eth(
        self,
        *,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendEthResponse:
        """
        Transfers ETH to a specified address.

        Args:
          amount: Amount of ETH to be transferred.

          to: Recipient ETH address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/send/eth",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                send_eth_params.SendEthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendEthResponse,
        )

    async def mor(
        self,
        *,
        amount: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendMorResponse:
        """
        Transfers MOR tokens to a specified address.

        Args:
          amount: Amount of MOR tokens to be transferred.

          to: Recipient ETH address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/send/mor",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "to": to,
                },
                send_mor_params.SendMorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendMorResponse,
        )


class SendResourceWithRawResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.eth = to_raw_response_wrapper(
            send.eth,
        )
        self.mor = to_raw_response_wrapper(
            send.mor,
        )


class AsyncSendResourceWithRawResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.eth = async_to_raw_response_wrapper(
            send.eth,
        )
        self.mor = async_to_raw_response_wrapper(
            send.mor,
        )


class SendResourceWithStreamingResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.eth = to_streamed_response_wrapper(
            send.eth,
        )
        self.mor = to_streamed_response_wrapper(
            send.mor,
        )


class AsyncSendResourceWithStreamingResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.eth = async_to_streamed_response_wrapper(
            send.eth,
        )
        self.mor = async_to_streamed_response_wrapper(
            send.mor,
        )
