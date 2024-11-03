# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Balance

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_send(self, client: MorpheusMarketplace) -> None:
        mor = client.blockchain.mor.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(Balance, mor, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.mor.with_raw_response.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mor = response.parse()
        assert_matches_type(Balance, mor, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.mor.with_streaming_response.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mor = response.parse()
            assert_matches_type(Balance, mor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMor:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        mor = await async_client.blockchain.mor.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(Balance, mor, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.mor.with_raw_response.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mor = await response.parse()
        assert_matches_type(Balance, mor, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.mor.with_streaming_response.send(
            amount="250",
            to="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mor = await response.parse()
            assert_matches_type(Balance, mor, path=["response"])

        assert cast(Any, response.is_closed) is True
