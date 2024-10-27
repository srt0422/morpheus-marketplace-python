# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .supply import (
    SupplyResource,
    AsyncSupplyResource,
    SupplyResourceWithRawResponse,
    AsyncSupplyResourceWithRawResponse,
    SupplyResourceWithStreamingResponse,
    AsyncSupplyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TokenResource", "AsyncTokenResource"]


class TokenResource(SyncAPIResource):
    @cached_property
    def supply(self) -> SupplyResource:
        return SupplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> TokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return TokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return TokenResourceWithStreamingResponse(self)


class AsyncTokenResource(AsyncAPIResource):
    @cached_property
    def supply(self) -> AsyncSupplyResource:
        return AsyncSupplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncTokenResourceWithStreamingResponse(self)


class TokenResourceWithRawResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

    @cached_property
    def supply(self) -> SupplyResourceWithRawResponse:
        return SupplyResourceWithRawResponse(self._token.supply)


class AsyncTokenResourceWithRawResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

    @cached_property
    def supply(self) -> AsyncSupplyResourceWithRawResponse:
        return AsyncSupplyResourceWithRawResponse(self._token.supply)


class TokenResourceWithStreamingResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

    @cached_property
    def supply(self) -> SupplyResourceWithStreamingResponse:
        return SupplyResourceWithStreamingResponse(self._token.supply)


class AsyncTokenResourceWithStreamingResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

    @cached_property
    def supply(self) -> AsyncSupplyResourceWithStreamingResponse:
        return AsyncSupplyResourceWithStreamingResponse(self._token.supply)
