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
from ...types.blockchain import allowance_retrieve_params
from ...types.blockchain.allowance_retrieve_response import AllowanceRetrieveResponse

__all__ = ["AllowanceResource", "AsyncAllowanceResource"]


class AllowanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllowanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AllowanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllowanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AllowanceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        spender: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllowanceRetrieveResponse:
        """
        Retrieve allowance

        Args:
          spender: Spender Ethereum address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/blockchain/allowance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"spender": spender}, allowance_retrieve_params.AllowanceRetrieveParams),
            ),
            cast_to=AllowanceRetrieveResponse,
        )


class AsyncAllowanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllowanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllowanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllowanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncAllowanceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        spender: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllowanceRetrieveResponse:
        """
        Retrieve allowance

        Args:
          spender: Spender Ethereum address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/blockchain/allowance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"spender": spender}, allowance_retrieve_params.AllowanceRetrieveParams
                ),
            ),
            cast_to=AllowanceRetrieveResponse,
        )


class AllowanceResourceWithRawResponse:
    def __init__(self, allowance: AllowanceResource) -> None:
        self._allowance = allowance

        self.retrieve = to_raw_response_wrapper(
            allowance.retrieve,
        )


class AsyncAllowanceResourceWithRawResponse:
    def __init__(self, allowance: AsyncAllowanceResource) -> None:
        self._allowance = allowance

        self.retrieve = async_to_raw_response_wrapper(
            allowance.retrieve,
        )


class AllowanceResourceWithStreamingResponse:
    def __init__(self, allowance: AllowanceResource) -> None:
        self._allowance = allowance

        self.retrieve = to_streamed_response_wrapper(
            allowance.retrieve,
        )


class AsyncAllowanceResourceWithStreamingResponse:
    def __init__(self, allowance: AsyncAllowanceResource) -> None:
        self._allowance = allowance

        self.retrieve = async_to_streamed_response_wrapper(
            allowance.retrieve,
        )
