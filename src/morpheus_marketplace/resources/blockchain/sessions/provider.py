# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.blockchain.sessions import provider_list_params
from ....types.blockchain.sessions.provider_list_response import ProviderListResponse

__all__ = ["ProviderResource", "AsyncProviderResource"]


class ProviderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return ProviderResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        provider: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """
        Retrieves a list of sessions for a specified provider.

        Args:
          provider: Ethereum address of the provider.

          limit: Limit for pagination.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/blockchain/sessions/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "limit": limit,
                        "offset": offset,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )


class AsyncProviderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncProviderResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        provider: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """
        Retrieves a list of sessions for a specified provider.

        Args:
          provider: Ethereum address of the provider.

          limit: Limit for pagination.

          offset: Offset for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/blockchain/sessions/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "limit": limit,
                        "offset": offset,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )


class ProviderResourceWithRawResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_raw_response_wrapper(
            provider.list,
        )


class AsyncProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_raw_response_wrapper(
            provider.list,
        )


class ProviderResourceWithStreamingResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_streamed_response_wrapper(
            provider.list,
        )


class AsyncProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_streamed_response_wrapper(
            provider.list,
        )
