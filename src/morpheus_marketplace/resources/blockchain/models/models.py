# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .bids import (
    BidsResource,
    AsyncBidsResource,
    BidsResourceWithRawResponse,
    AsyncBidsResourceWithRawResponse,
    BidsResourceWithStreamingResponse,
    AsyncBidsResourceWithStreamingResponse,
)
from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .minstake import (
    MinstakeResource,
    AsyncMinstakeResource,
    MinstakeResourceWithRawResponse,
    AsyncMinstakeResourceWithRawResponse,
    MinstakeResourceWithStreamingResponse,
    AsyncMinstakeResourceWithStreamingResponse,
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
from ....types.blockchain import model_create_params, model_session_params
from ....types.shared.session import Session
from ....types.blockchain.model import Model
from ....types.blockchain.model_list_response import ModelListResponse
from ....types.blockchain.model_delete_response import ModelDeleteResponse
from ....types.blockchain.model_exists_response import ModelExistsResponse
from ....types.blockchain.model_resetstats_response import ModelResetstatsResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def bids(self) -> BidsResource:
        return BidsResource(self._client)

    @cached_property
    def minstake(self) -> MinstakeResource:
        return MinstakeResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        fee: str,
        ipfs_id: str,
        model_id: str,
        name: str,
        stake: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Model:
        """
        Registers a new model on the blockchain.

        Args:
          fee: Fee amount required for model usage.

          ipfs_id: IPFS hash storing the model’s data.

          model_id: Unique identifier for the model.

          name: Name of the model.

          stake: Stake amount for the model.

          tags: Descriptive tags for categorizing the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/blockchain/models",
            body=maybe_transform(
                {
                    "fee": fee,
                    "ipfs_id": ipfs_id,
                    "model_id": model_id,
                    "name": name,
                    "stake": stake,
                    "tags": tags,
                },
                model_create_params.ModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Model,
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
    ) -> ModelListResponse:
        """Fetches a list of all models available on the blockchain."""
        return self._get(
            "/blockchain/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListResponse,
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
    ) -> ModelDeleteResponse:
        """
        Removes a model from the blockchain by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/blockchain/models/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelDeleteResponse,
        )

    def exists(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelExistsResponse:
        """
        Checks if a model exists on the blockchain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/blockchain/models/{id}/exists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelExistsResponse,
        )

    def resetstats(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelResetstatsResponse:
        """
        Resets the statistics of a model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/blockchain/models/{id}/resetstats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelResetstatsResponse,
        )

    def session(
        self,
        id: str,
        *,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Opens a session with a specific model, associating it with a provider on the
        blockchain.

        Args:
          session_duration: The duration of the session in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/blockchain/models/{id}/session",
            body=maybe_transform({"session_duration": session_duration}, model_session_params.ModelSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def bids(self) -> AsyncBidsResource:
        return AsyncBidsResource(self._client)

    @cached_property
    def minstake(self) -> AsyncMinstakeResource:
        return AsyncMinstakeResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        fee: str,
        ipfs_id: str,
        model_id: str,
        name: str,
        stake: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Model:
        """
        Registers a new model on the blockchain.

        Args:
          fee: Fee amount required for model usage.

          ipfs_id: IPFS hash storing the model’s data.

          model_id: Unique identifier for the model.

          name: Name of the model.

          stake: Stake amount for the model.

          tags: Descriptive tags for categorizing the model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/blockchain/models",
            body=await async_maybe_transform(
                {
                    "fee": fee,
                    "ipfs_id": ipfs_id,
                    "model_id": model_id,
                    "name": name,
                    "stake": stake,
                    "tags": tags,
                },
                model_create_params.ModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Model,
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
    ) -> ModelListResponse:
        """Fetches a list of all models available on the blockchain."""
        return await self._get(
            "/blockchain/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListResponse,
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
    ) -> ModelDeleteResponse:
        """
        Removes a model from the blockchain by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/blockchain/models/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelDeleteResponse,
        )

    async def exists(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelExistsResponse:
        """
        Checks if a model exists on the blockchain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/blockchain/models/{id}/exists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelExistsResponse,
        )

    async def resetstats(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelResetstatsResponse:
        """
        Resets the statistics of a model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/blockchain/models/{id}/resetstats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelResetstatsResponse,
        )

    async def session(
        self,
        id: str,
        *,
        session_duration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Opens a session with a specific model, associating it with a provider on the
        blockchain.

        Args:
          session_duration: The duration of the session in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/blockchain/models/{id}/session",
            body=await async_maybe_transform(
                {"session_duration": session_duration}, model_session_params.ModelSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.create = to_raw_response_wrapper(
            models.create,
        )
        self.list = to_raw_response_wrapper(
            models.list,
        )
        self.delete = to_raw_response_wrapper(
            models.delete,
        )
        self.exists = to_raw_response_wrapper(
            models.exists,
        )
        self.resetstats = to_raw_response_wrapper(
            models.resetstats,
        )
        self.session = to_raw_response_wrapper(
            models.session,
        )

    @cached_property
    def bids(self) -> BidsResourceWithRawResponse:
        return BidsResourceWithRawResponse(self._models.bids)

    @cached_property
    def minstake(self) -> MinstakeResourceWithRawResponse:
        return MinstakeResourceWithRawResponse(self._models.minstake)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._models.stats)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.create = async_to_raw_response_wrapper(
            models.create,
        )
        self.list = async_to_raw_response_wrapper(
            models.list,
        )
        self.delete = async_to_raw_response_wrapper(
            models.delete,
        )
        self.exists = async_to_raw_response_wrapper(
            models.exists,
        )
        self.resetstats = async_to_raw_response_wrapper(
            models.resetstats,
        )
        self.session = async_to_raw_response_wrapper(
            models.session,
        )

    @cached_property
    def bids(self) -> AsyncBidsResourceWithRawResponse:
        return AsyncBidsResourceWithRawResponse(self._models.bids)

    @cached_property
    def minstake(self) -> AsyncMinstakeResourceWithRawResponse:
        return AsyncMinstakeResourceWithRawResponse(self._models.minstake)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._models.stats)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.create = to_streamed_response_wrapper(
            models.create,
        )
        self.list = to_streamed_response_wrapper(
            models.list,
        )
        self.delete = to_streamed_response_wrapper(
            models.delete,
        )
        self.exists = to_streamed_response_wrapper(
            models.exists,
        )
        self.resetstats = to_streamed_response_wrapper(
            models.resetstats,
        )
        self.session = to_streamed_response_wrapper(
            models.session,
        )

    @cached_property
    def bids(self) -> BidsResourceWithStreamingResponse:
        return BidsResourceWithStreamingResponse(self._models.bids)

    @cached_property
    def minstake(self) -> MinstakeResourceWithStreamingResponse:
        return MinstakeResourceWithStreamingResponse(self._models.minstake)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._models.stats)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.create = async_to_streamed_response_wrapper(
            models.create,
        )
        self.list = async_to_streamed_response_wrapper(
            models.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            models.delete,
        )
        self.exists = async_to_streamed_response_wrapper(
            models.exists,
        )
        self.resetstats = async_to_streamed_response_wrapper(
            models.resetstats,
        )
        self.session = async_to_streamed_response_wrapper(
            models.session,
        )

    @cached_property
    def bids(self) -> AsyncBidsResourceWithStreamingResponse:
        return AsyncBidsResourceWithStreamingResponse(self._models.bids)

    @cached_property
    def minstake(self) -> AsyncMinstakeResourceWithStreamingResponse:
        return AsyncMinstakeResourceWithStreamingResponse(self._models.minstake)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._models.stats)
