# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Balance

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_send(self, client: MorpheusMarketplace) -> None:
        eth = client.blockchain.eth.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        )
        assert_matches_type(Balance, eth, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.eth.with_raw_response.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eth = response.parse()
        assert_matches_type(Balance, eth, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.eth.with_streaming_response.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eth = response.parse()
            assert_matches_type(Balance, eth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        eth = await async_client.blockchain.eth.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        )
        assert_matches_type(Balance, eth, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.eth.with_raw_response.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eth = await response.parse()
        assert_matches_type(Balance, eth, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.eth.with_streaming_response.send(
            amount="1.5",
            to="0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eth = await response.parse()
            assert_matches_type(Balance, eth, path=["response"])

        assert cast(Any, response.is_closed) is True
