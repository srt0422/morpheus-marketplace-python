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
from ...types.blockchain import mor_send_params
from ...types.shared.balance import Balance

__all__ = ["MorResource", "AsyncMorResource"]


class MorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return MorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return MorResourceWithStreamingResponse(self)

    def send(
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
    ) -> Balance:
        """
        Send MOR to a specified address

        Args:
          amount: Amount of MOR to send

          to: Ethereum address to send MOR to

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
                mor_send_params.MorSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Balance,
        )


class AsyncMorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncMorResourceWithStreamingResponse(self)

    async def send(
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
    ) -> Balance:
        """
        Send MOR to a specified address

        Args:
          amount: Amount of MOR to send

          to: Ethereum address to send MOR to

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
                mor_send_params.MorSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Balance,
        )


class MorResourceWithRawResponse:
    def __init__(self, mor: MorResource) -> None:
        self._mor = mor

        self.send = to_raw_response_wrapper(
            mor.send,
        )


class AsyncMorResourceWithRawResponse:
    def __init__(self, mor: AsyncMorResource) -> None:
        self._mor = mor

        self.send = async_to_raw_response_wrapper(
            mor.send,
        )


class MorResourceWithStreamingResponse:
    def __init__(self, mor: MorResource) -> None:
        self._mor = mor

        self.send = to_streamed_response_wrapper(
            mor.send,
        )


class AsyncMorResourceWithStreamingResponse:
    def __init__(self, mor: AsyncMorResource) -> None:
        self._mor = mor

        self.send = async_to_streamed_response_wrapper(
            mor.send,
        )
