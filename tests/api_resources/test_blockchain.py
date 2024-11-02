# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlockchain:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_approve(self, client: MorpheusMarketplace) -> None:
        blockchain = client.blockchain.approve(
            amount="500",
            spender="spender",
        )
        assert blockchain is None

    @parametrize
    def test_raw_response_approve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.with_raw_response.approve(
            amount="500",
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain = response.parse()
        assert blockchain is None

    @parametrize
    def test_streaming_response_approve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.with_streaming_response.approve(
            amount="500",
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain = response.parse()
            assert blockchain is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBlockchain:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain = await async_client.blockchain.approve(
            amount="500",
            spender="spender",
        )
        assert blockchain is None

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.with_raw_response.approve(
            amount="500",
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain = await response.parse()
        assert blockchain is None

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.with_streaming_response.approve(
            amount="500",
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain = await response.parse()
            assert blockchain is None

        assert cast(Any, response.is_closed) is True
