# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.proxy.sessions.claimable_balance import ClaimableBalance

__all__ = ["ProviderClaimableBalanceResource", "AsyncProviderClaimableBalanceResource"]


class ProviderClaimableBalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderClaimableBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return ProviderClaimableBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderClaimableBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return ProviderClaimableBalanceResourceWithStreamingResponse(self)

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
    ) -> ClaimableBalance:
        """
        Get provider claimable balance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/proxy/sessions/{id}/providerClaimableBalance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimableBalance,
        )


class AsyncProviderClaimableBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderClaimableBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderClaimableBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderClaimableBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncProviderClaimableBalanceResourceWithStreamingResponse(self)

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
    ) -> ClaimableBalance:
        """
        Get provider claimable balance

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/proxy/sessions/{id}/providerClaimableBalance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimableBalance,
        )


class ProviderClaimableBalanceResourceWithRawResponse:
    def __init__(self, provider_claimable_balance: ProviderClaimableBalanceResource) -> None:
        self._provider_claimable_balance = provider_claimable_balance

        self.retrieve = to_raw_response_wrapper(
            provider_claimable_balance.retrieve,
        )


class AsyncProviderClaimableBalanceResourceWithRawResponse:
    def __init__(self, provider_claimable_balance: AsyncProviderClaimableBalanceResource) -> None:
        self._provider_claimable_balance = provider_claimable_balance

        self.retrieve = async_to_raw_response_wrapper(
            provider_claimable_balance.retrieve,
        )


class ProviderClaimableBalanceResourceWithStreamingResponse:
    def __init__(self, provider_claimable_balance: ProviderClaimableBalanceResource) -> None:
        self._provider_claimable_balance = provider_claimable_balance

        self.retrieve = to_streamed_response_wrapper(
            provider_claimable_balance.retrieve,
        )


class AsyncProviderClaimableBalanceResourceWithStreamingResponse:
    def __init__(self, provider_claimable_balance: AsyncProviderClaimableBalanceResource) -> None:
        self._provider_claimable_balance = provider_claimable_balance

        self.retrieve = async_to_streamed_response_wrapper(
            provider_claimable_balance.retrieve,
        )
