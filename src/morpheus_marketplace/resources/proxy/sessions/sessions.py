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
from ....types.proxy import session_initiate_params, session_provider_claim_params
from ...._base_client import make_request_options
from ....types.shared.session import Session
from .provider_claimable_balance import (
    ProviderClaimableBalanceResource,
    AsyncProviderClaimableBalanceResource,
    ProviderClaimableBalanceResourceWithRawResponse,
    AsyncProviderClaimableBalanceResourceWithRawResponse,
    ProviderClaimableBalanceResourceWithStreamingResponse,
    AsyncProviderClaimableBalanceResourceWithStreamingResponse,
)
from ....types.proxy.sessions.claimable_balance import ClaimableBalance

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def provider_claimable_balance(self) -> ProviderClaimableBalanceResource:
        return ProviderClaimableBalanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def initiate(
        self,
        *,
        model_id: str,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Initiate a proxy session

        Args:
          model_id: Model ID to initiate session with

          session_duration: Duration of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/proxy/sessions/initiate",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "session_duration": session_duration,
                },
                session_initiate_params.SessionInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def provider_claim(
        self,
        id: str,
        *,
        claim: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClaimableBalance:
        """
        Claim provider balance

        Args:
          claim: Claim identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/proxy/sessions/{id}/providerClaim",
            body=maybe_transform({"claim": claim}, session_provider_claim_params.SessionProviderClaimParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimableBalance,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def provider_claimable_balance(self) -> AsyncProviderClaimableBalanceResource:
        return AsyncProviderClaimableBalanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def initiate(
        self,
        *,
        model_id: str,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Initiate a proxy session

        Args:
          model_id: Model ID to initiate session with

          session_duration: Duration of the session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/proxy/sessions/initiate",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "session_duration": session_duration,
                },
                session_initiate_params.SessionInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def provider_claim(
        self,
        id: str,
        *,
        claim: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClaimableBalance:
        """
        Claim provider balance

        Args:
          claim: Claim identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/proxy/sessions/{id}/providerClaim",
            body=await async_maybe_transform(
                {"claim": claim}, session_provider_claim_params.SessionProviderClaimParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimableBalance,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.initiate = to_raw_response_wrapper(
            sessions.initiate,
        )
        self.provider_claim = to_raw_response_wrapper(
            sessions.provider_claim,
        )

    @cached_property
    def provider_claimable_balance(self) -> ProviderClaimableBalanceResourceWithRawResponse:
        return ProviderClaimableBalanceResourceWithRawResponse(self._sessions.provider_claimable_balance)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.initiate = async_to_raw_response_wrapper(
            sessions.initiate,
        )
        self.provider_claim = async_to_raw_response_wrapper(
            sessions.provider_claim,
        )

    @cached_property
    def provider_claimable_balance(self) -> AsyncProviderClaimableBalanceResourceWithRawResponse:
        return AsyncProviderClaimableBalanceResourceWithRawResponse(self._sessions.provider_claimable_balance)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.initiate = to_streamed_response_wrapper(
            sessions.initiate,
        )
        self.provider_claim = to_streamed_response_wrapper(
            sessions.provider_claim,
        )

    @cached_property
    def provider_claimable_balance(self) -> ProviderClaimableBalanceResourceWithStreamingResponse:
        return ProviderClaimableBalanceResourceWithStreamingResponse(self._sessions.provider_claimable_balance)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.initiate = async_to_streamed_response_wrapper(
            sessions.initiate,
        )
        self.provider_claim = async_to_streamed_response_wrapper(
            sessions.provider_claim,
        )

    @cached_property
    def provider_claimable_balance(self) -> AsyncProviderClaimableBalanceResourceWithStreamingResponse:
        return AsyncProviderClaimableBalanceResourceWithStreamingResponse(self._sessions.provider_claimable_balance)
