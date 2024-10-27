# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain.token import TokenSupply

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSupply:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        supply = client.blockchain.token.supply.retrieve()
        assert_matches_type(TokenSupply, supply, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.token.supply.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supply = response.parse()
        assert_matches_type(TokenSupply, supply, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.token.supply.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supply = response.parse()
            assert_matches_type(TokenSupply, supply, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSupply:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        supply = await async_client.blockchain.token.supply.retrieve()
        assert_matches_type(TokenSupply, supply, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.token.supply.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supply = await response.parse()
        assert_matches_type(TokenSupply, supply, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.token.supply.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supply = await response.parse()
            assert_matches_type(TokenSupply, supply, path=["response"])

        assert cast(Any, response.is_closed) is True
