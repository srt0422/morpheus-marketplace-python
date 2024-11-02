# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sessions.sessions import SessionsResource, AsyncSessionsResource

__all__ = ["ProxyResource", "AsyncProxyResource"]


class ProxyResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return ProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return ProxyResourceWithStreamingResponse(self)


class AsyncProxyResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncProxyResourceWithStreamingResponse(self)


class ProxyResourceWithRawResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._proxy.sessions)


class AsyncProxyResourceWithRawResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._proxy.sessions)


class ProxyResourceWithStreamingResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._proxy.sessions)


class AsyncProxyResourceWithStreamingResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._proxy.sessions)
