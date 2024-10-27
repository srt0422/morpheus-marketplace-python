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
from ....types.blockchain.sessions import user_list_params
from ....types.blockchain.sessions.user_list_response import UserListResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        user: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Retrieves a list of all active and closed sessions associated with a specific
        user.

        Args:
          user: Ethereum address of the user.

          limit: Limit for pagination.

          offset: Offset for pagination.

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
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        user: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Retrieves a list of all active and closed sessions associated with a specific
        user.

        Args:
          user: Ethereum address of the user.

          limit: Limit for pagination.

          offset: Offset for pagination.

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
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_raw_response_wrapper(
            user.list,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_raw_response_wrapper(
            user.list,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_streamed_response_wrapper(
            user.list,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_streamed_response_wrapper(
            user.list,
        )
