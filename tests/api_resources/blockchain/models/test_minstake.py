# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain.models import MinStake, MinstakeSetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMinstake:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        minstake = client.blockchain.models.minstake.retrieve()
        assert_matches_type(MinStake, minstake, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.minstake.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        minstake = response.parse()
        assert_matches_type(MinStake, minstake, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.minstake.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            minstake = response.parse()
            assert_matches_type(MinStake, minstake, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set(self, client: MorpheusMarketplace) -> None:
        minstake = client.blockchain.models.minstake.set(
            min_stake="minStake",
        )
        assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.minstake.with_raw_response.set(
            min_stake="minStake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        minstake = response.parse()
        assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.minstake.with_streaming_response.set(
            min_stake="minStake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            minstake = response.parse()
            assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMinstake:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        minstake = await async_client.blockchain.models.minstake.retrieve()
        assert_matches_type(MinStake, minstake, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.minstake.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        minstake = await response.parse()
        assert_matches_type(MinStake, minstake, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.minstake.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            minstake = await response.parse()
            assert_matches_type(MinStake, minstake, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set(self, async_client: AsyncMorpheusMarketplace) -> None:
        minstake = await async_client.blockchain.models.minstake.set(
            min_stake="minStake",
        )
        assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.minstake.with_raw_response.set(
            min_stake="minStake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        minstake = await response.parse()
        assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.minstake.with_streaming_response.set(
            min_stake="minStake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            minstake = await response.parse()
            assert_matches_type(MinstakeSetResponse, minstake, path=["response"])

        assert cast(Any, response.is_closed) is True
