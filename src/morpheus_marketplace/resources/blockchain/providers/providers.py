# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .bids import (
    BidsResource,
    AsyncBidsResource,
    BidsResourceWithRawResponse,
    AsyncBidsResourceWithRawResponse,
    BidsResourceWithStreamingResponse,
    AsyncBidsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .bids.bids import BidsResource, AsyncBidsResource
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.blockchain import provider_create_params
from ....types.blockchain.provider import Provider
from ....types.blockchain.provider_list_response import ProviderListResponse
from ....types.blockchain.provider_delete_response import ProviderDeleteResponse

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def bids(self) -> BidsResource:
        return BidsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        endpoint: str,
        stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Provider:
        """
        Registers or updates a provider.

        Args:
          endpoint: Endpoint URL of the provider.

          stake: Amount of tokens staked by the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/providers",
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "stake": stake,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """Retrieves a list of all registered providers."""
        return self._get(
            "/blockchain/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderListResponse,
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
    ) -> ProviderDeleteResponse:
        """
        Removes a provider’s registration from the blockchain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/blockchain/providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDeleteResponse,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def bids(self) -> AsyncBidsResource:
        return AsyncBidsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        endpoint: str,
        stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Provider:
        """
        Registers or updates a provider.

        Args:
          endpoint: Endpoint URL of the provider.

          stake: Amount of tokens staked by the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/providers",
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "stake": stake,
                },
                provider_create_params.ProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Provider,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """Retrieves a list of all registered providers."""
        return await self._get(
            "/blockchain/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderListResponse,
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
    ) -> ProviderDeleteResponse:
        """
        Removes a provider’s registration from the blockchain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/blockchain/providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDeleteResponse,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_raw_response_wrapper(
            providers.create,
        )
        self.list = to_raw_response_wrapper(
            providers.list,
        )
        self.delete = to_raw_response_wrapper(
            providers.delete,
        )

    @cached_property
    def bids(self) -> BidsResourceWithRawResponse:
        return BidsResourceWithRawResponse(self._providers.bids)


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_raw_response_wrapper(
            providers.create,
        )
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            providers.delete,
        )

    @cached_property
    def bids(self) -> AsyncBidsResourceWithRawResponse:
        return AsyncBidsResourceWithRawResponse(self._providers.bids)


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.create = to_streamed_response_wrapper(
            providers.create,
        )
        self.list = to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            providers.delete,
        )

    @cached_property
    def bids(self) -> BidsResourceWithStreamingResponse:
        return BidsResourceWithStreamingResponse(self._providers.bids)


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.create = async_to_streamed_response_wrapper(
            providers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            providers.delete,
        )

    @cached_property
    def bids(self) -> AsyncBidsResourceWithStreamingResponse:
        return AsyncBidsResourceWithStreamingResponse(self._providers.bids)
