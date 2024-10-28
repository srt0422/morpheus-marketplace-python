# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    blockchain_session_user_params,
    blockchain_session_create_params,
    blockchain_session_provider_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.budget import Budget
from ..types.shared.session import Session
from ..types.shared.session_list import SessionList

__all__ = ["BlockchainSessionsResource", "AsyncBlockchainSessionsResource"]


class BlockchainSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockchainSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BlockchainSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockchainSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return BlockchainSessionsResourceWithStreamingResponse(self)

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
        Create a new session

        Args:
          approval: Approval identifier

          approval_sig: Signature for the approval

          stake: Stake amount for the session

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
                blockchain_session_create_params.BlockchainSessionCreateParams,
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
    ) -> Session:
        """
        Retrieve a session

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
            cast_to=Session,
        )

    def budget(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Budget:
        """Get session budget"""
        return self._get(
            "/blockchain/sessions/budget",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
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
    ) -> None:
        """
        Close a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/blockchain/sessions/{id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def provider(
        self,
        *,
        provider: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList:
        """
        List provider sessions

        Args:
          provider: Provider identifier

          limit: Maximum number of results to return

          offset: Number of results to skip

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
                    blockchain_session_provider_params.BlockchainSessionProviderParams,
                ),
            ),
            cast_to=SessionList,
        )

    def user(
        self,
        *,
        user: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList:
        """
        List user sessions

        Args:
          user: User identifier

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/blockchain/sessions/user",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "user": user,
                        "limit": limit,
                        "offset": offset,
                    },
                    blockchain_session_user_params.BlockchainSessionUserParams,
                ),
            ),
            cast_to=SessionList,
        )


class AsyncBlockchainSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockchainSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockchainSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockchainSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBlockchainSessionsResourceWithStreamingResponse(self)

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
        Create a new session

        Args:
          approval: Approval identifier

          approval_sig: Signature for the approval

          stake: Stake amount for the session

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
                blockchain_session_create_params.BlockchainSessionCreateParams,
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
    ) -> Session:
        """
        Retrieve a session

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
            cast_to=Session,
        )

    async def budget(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Budget:
        """Get session budget"""
        return await self._get(
            "/blockchain/sessions/budget",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
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
    ) -> None:
        """
        Close a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/blockchain/sessions/{id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def provider(
        self,
        *,
        provider: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList:
        """
        List provider sessions

        Args:
          provider: Provider identifier

          limit: Maximum number of results to return

          offset: Number of results to skip

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
                    blockchain_session_provider_params.BlockchainSessionProviderParams,
                ),
            ),
            cast_to=SessionList,
        )

    async def user(
        self,
        *,
        user: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionList:
        """
        List user sessions

        Args:
          user: User identifier

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/blockchain/sessions/user",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "user": user,
                        "limit": limit,
                        "offset": offset,
                    },
                    blockchain_session_user_params.BlockchainSessionUserParams,
                ),
            ),
            cast_to=SessionList,
        )


class BlockchainSessionsResourceWithRawResponse:
    def __init__(self, blockchain_sessions: BlockchainSessionsResource) -> None:
        self._blockchain_sessions = blockchain_sessions

        self.create = to_raw_response_wrapper(
            blockchain_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            blockchain_sessions.retrieve,
        )
        self.budget = to_raw_response_wrapper(
            blockchain_sessions.budget,
        )
        self.close = to_raw_response_wrapper(
            blockchain_sessions.close,
        )
        self.provider = to_raw_response_wrapper(
            blockchain_sessions.provider,
        )
        self.user = to_raw_response_wrapper(
            blockchain_sessions.user,
        )


class AsyncBlockchainSessionsResourceWithRawResponse:
    def __init__(self, blockchain_sessions: AsyncBlockchainSessionsResource) -> None:
        self._blockchain_sessions = blockchain_sessions

        self.create = async_to_raw_response_wrapper(
            blockchain_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            blockchain_sessions.retrieve,
        )
        self.budget = async_to_raw_response_wrapper(
            blockchain_sessions.budget,
        )
        self.close = async_to_raw_response_wrapper(
            blockchain_sessions.close,
        )
        self.provider = async_to_raw_response_wrapper(
            blockchain_sessions.provider,
        )
        self.user = async_to_raw_response_wrapper(
            blockchain_sessions.user,
        )


class BlockchainSessionsResourceWithStreamingResponse:
    def __init__(self, blockchain_sessions: BlockchainSessionsResource) -> None:
        self._blockchain_sessions = blockchain_sessions

        self.create = to_streamed_response_wrapper(
            blockchain_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            blockchain_sessions.retrieve,
        )
        self.budget = to_streamed_response_wrapper(
            blockchain_sessions.budget,
        )
        self.close = to_streamed_response_wrapper(
            blockchain_sessions.close,
        )
        self.provider = to_streamed_response_wrapper(
            blockchain_sessions.provider,
        )
        self.user = to_streamed_response_wrapper(
            blockchain_sessions.user,
        )


class AsyncBlockchainSessionsResourceWithStreamingResponse:
    def __init__(self, blockchain_sessions: AsyncBlockchainSessionsResource) -> None:
        self._blockchain_sessions = blockchain_sessions

        self.create = async_to_streamed_response_wrapper(
            blockchain_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            blockchain_sessions.retrieve,
        )
        self.budget = async_to_streamed_response_wrapper(
            blockchain_sessions.budget,
        )
        self.close = async_to_streamed_response_wrapper(
            blockchain_sessions.close,
        )
        self.provider = async_to_streamed_response_wrapper(
            blockchain_sessions.provider,
        )
        self.user = async_to_streamed_response_wrapper(
            blockchain_sessions.user,
        )
