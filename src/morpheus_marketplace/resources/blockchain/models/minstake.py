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
from ....types.blockchain.models import minstake_set_params
from ....types.blockchain.models.min_stake import MinStake
from ....types.blockchain.models.minstake_set_response import MinstakeSetResponse

__all__ = ["MinstakeResource", "AsyncMinstakeResource"]


class MinstakeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MinstakeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return MinstakeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MinstakeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return MinstakeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinStake:
        """Retrieves the current minimum stake required for models."""
        return self._get(
            "/blockchain/models/minstake",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MinStake,
        )

    def set(
        self,
        *,
        min_stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinstakeSetResponse:
        """
        Sets the minimum stake required for models.

        Args:
          min_stake: Minimum stake amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/models/minstake",
            body=maybe_transform({"min_stake": min_stake}, minstake_set_params.MinstakeSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MinstakeSetResponse,
        )


class AsyncMinstakeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMinstakeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMinstakeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMinstakeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncMinstakeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinStake:
        """Retrieves the current minimum stake required for models."""
        return await self._get(
            "/blockchain/models/minstake",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MinStake,
        )

    async def set(
        self,
        *,
        min_stake: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinstakeSetResponse:
        """
        Sets the minimum stake required for models.

        Args:
          min_stake: Minimum stake amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/models/minstake",
            body=await async_maybe_transform({"min_stake": min_stake}, minstake_set_params.MinstakeSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MinstakeSetResponse,
        )


class MinstakeResourceWithRawResponse:
    def __init__(self, minstake: MinstakeResource) -> None:
        self._minstake = minstake

        self.retrieve = to_raw_response_wrapper(
            minstake.retrieve,
        )
        self.set = to_raw_response_wrapper(
            minstake.set,
        )


class AsyncMinstakeResourceWithRawResponse:
    def __init__(self, minstake: AsyncMinstakeResource) -> None:
        self._minstake = minstake

        self.retrieve = async_to_raw_response_wrapper(
            minstake.retrieve,
        )
        self.set = async_to_raw_response_wrapper(
            minstake.set,
        )


class MinstakeResourceWithStreamingResponse:
    def __init__(self, minstake: MinstakeResource) -> None:
        self._minstake = minstake

        self.retrieve = to_streamed_response_wrapper(
            minstake.retrieve,
        )
        self.set = to_streamed_response_wrapper(
            minstake.set,
        )


class AsyncMinstakeResourceWithStreamingResponse:
    def __init__(self, minstake: AsyncMinstakeResource) -> None:
        self._minstake = minstake

        self.retrieve = async_to_streamed_response_wrapper(
            minstake.retrieve,
        )
        self.set = async_to_streamed_response_wrapper(
            minstake.set,
        )
