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
from ....types.blockchain.sessions.budget_list_response import BudgetListResponse

__all__ = ["BudgetResource", "AsyncBudgetResource"]


class BudgetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return BudgetResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetListResponse:
        """Fetches the total budget for sessions on the current day."""
        return self._get(
            "/blockchain/sessions/budget",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetListResponse,
        )


class AsyncBudgetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBudgetResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BudgetListResponse:
        """Fetches the total budget for sessions on the current day."""
        return await self._get(
            "/blockchain/sessions/budget",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetListResponse,
        )


class BudgetResourceWithRawResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.list = to_raw_response_wrapper(
            budget.list,
        )


class AsyncBudgetResourceWithRawResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.list = async_to_raw_response_wrapper(
            budget.list,
        )


class BudgetResourceWithStreamingResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.list = to_streamed_response_wrapper(
            budget.list,
        )


class AsyncBudgetResourceWithStreamingResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.list = async_to_streamed_response_wrapper(
            budget.list,
        )
