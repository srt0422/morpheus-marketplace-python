# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .budget import (
    BudgetResource,
    AsyncBudgetResource,
    BudgetResourceWithRawResponse,
    AsyncBudgetResourceWithRawResponse,
    BudgetResourceWithStreamingResponse,
    AsyncBudgetResourceWithStreamingResponse,
)
from .provider import (
    ProviderResource,
    AsyncProviderResource,
    ProviderResourceWithRawResponse,
    AsyncProviderResourceWithRawResponse,
    ProviderResourceWithStreamingResponse,
    AsyncProviderResourceWithStreamingResponse,
)
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
from ....types.blockchain import session_create_params
from ....types.shared.session import Session
from ....types.blockchain.session_close_response import SessionCloseResponse
from ....types.blockchain.session_retrieve_response import SessionRetrieveResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def provider(self) -> ProviderResource:
        return ProviderResource(self._client)

    @cached_property
    def budget(self) -> BudgetResource:
        return BudgetResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        approval: str,
        approval_sig: str,
        stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Opens a session with a provider, including staking requirements.

        Args:
          approval: Approval data for session initiation.

          approval_sig: Digital signature associated with the approval.

          stake: Amount of tokens staked for the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/sessions",
            body=maybe_transform(
                {
                    "approval": approval,
                    "approval_sig": approval_sig,
                    "stake": stake,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
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
    ) -> SessionRetrieveResponse:
        """
        Fetches details of a specific session by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/blockchain/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    def close(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCloseResponse:
        """
        Closes an active session using its unique session ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/blockchain/sessions/{id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCloseResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def provider(self) -> AsyncProviderResource:
        return AsyncProviderResource(self._client)

    @cached_property
    def budget(self) -> AsyncBudgetResource:
        return AsyncBudgetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        approval: str,
        approval_sig: str,
        stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Opens a session with a provider, including staking requirements.

        Args:
          approval: Approval data for session initiation.

          approval_sig: Digital signature associated with the approval.

          stake: Amount of tokens staked for the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/sessions",
            body=await async_maybe_transform(
                {
                    "approval": approval,
                    "approval_sig": approval_sig,
                    "stake": stake,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
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
    ) -> SessionRetrieveResponse:
        """
        Fetches details of a specific session by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/blockchain/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    async def close(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCloseResponse:
        """
        Closes an active session using its unique session ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/blockchain/sessions/{id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCloseResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.close = to_raw_response_wrapper(
            sessions.close,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._sessions.user)

    @cached_property
    def provider(self) -> ProviderResourceWithRawResponse:
        return ProviderResourceWithRawResponse(self._sessions.provider)

    @cached_property
    def budget(self) -> BudgetResourceWithRawResponse:
        return BudgetResourceWithRawResponse(self._sessions.budget)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.close = async_to_raw_response_wrapper(
            sessions.close,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._sessions.user)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithRawResponse:
        return AsyncProviderResourceWithRawResponse(self._sessions.provider)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithRawResponse:
        return AsyncBudgetResourceWithRawResponse(self._sessions.budget)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.close = to_streamed_response_wrapper(
            sessions.close,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._sessions.user)

    @cached_property
    def provider(self) -> ProviderResourceWithStreamingResponse:
        return ProviderResourceWithStreamingResponse(self._sessions.provider)

    @cached_property
    def budget(self) -> BudgetResourceWithStreamingResponse:
        return BudgetResourceWithStreamingResponse(self._sessions.budget)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.close = async_to_streamed_response_wrapper(
            sessions.close,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._sessions.user)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithStreamingResponse:
        return AsyncProviderResourceWithStreamingResponse(self._sessions.provider)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithStreamingResponse:
        return AsyncBudgetResourceWithStreamingResponse(self._sessions.budget)
