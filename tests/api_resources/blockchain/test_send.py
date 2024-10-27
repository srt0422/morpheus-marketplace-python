# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain import SendEthResponse, SendMorResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_eth(self, client: MorpheusMarketplace) -> None:
        send = client.blockchain.send.eth(
            amount="amount",
            to="to",
        )
        assert_matches_type(SendEthResponse, send, path=["response"])

    @parametrize
    def test_raw_response_eth(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.send.with_raw_response.eth(
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(SendEthResponse, send, path=["response"])

    @parametrize
    def test_streaming_response_eth(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.send.with_streaming_response.eth(
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(SendEthResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mor(self, client: MorpheusMarketplace) -> None:
        send = client.blockchain.send.mor(
            amount="amount",
            to="to",
        )
        assert_matches_type(SendMorResponse, send, path=["response"])

    @parametrize
    def test_raw_response_mor(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.send.with_raw_response.mor(
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(SendMorResponse, send, path=["response"])

    @parametrize
    def test_streaming_response_mor(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.send.with_streaming_response.mor(
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(SendMorResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSend:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_eth(self, async_client: AsyncMorpheusMarketplace) -> None:
        send = await async_client.blockchain.send.eth(
            amount="amount",
            to="to",
        )
        assert_matches_type(SendEthResponse, send, path=["response"])

    @parametrize
    async def test_raw_response_eth(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.send.with_raw_response.eth(
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(SendEthResponse, send, path=["response"])

    @parametrize
    async def test_streaming_response_eth(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.send.with_streaming_response.eth(
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(SendEthResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mor(self, async_client: AsyncMorpheusMarketplace) -> None:
        send = await async_client.blockchain.send.mor(
            amount="amount",
            to="to",
        )
        assert_matches_type(SendMorResponse, send, path=["response"])

    @parametrize
    async def test_raw_response_mor(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.send.with_raw_response.mor(
            amount="amount",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(SendMorResponse, send, path=["response"])

    @parametrize
    async def test_streaming_response_mor(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.send.with_streaming_response.mor(
            amount="amount",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(SendMorResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True
