# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain import (
    Allowance,
    AllowanceApproveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAllowance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        allowance = client.blockchain.allowance.retrieve(
            spender="spender",
        )
        assert_matches_type(Allowance, allowance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.allowance.with_raw_response.retrieve(
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowance = response.parse()
        assert_matches_type(Allowance, allowance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.allowance.with_streaming_response.retrieve(
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowance = response.parse()
            assert_matches_type(Allowance, allowance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: MorpheusMarketplace) -> None:
        allowance = client.blockchain.allowance.approve(
            amount="amount",
            spender="spender",
        )
        assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.allowance.with_raw_response.approve(
            amount="amount",
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowance = response.parse()
        assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.allowance.with_streaming_response.approve(
            amount="amount",
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowance = response.parse()
            assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAllowance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        allowance = await async_client.blockchain.allowance.retrieve(
            spender="spender",
        )
        assert_matches_type(Allowance, allowance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.allowance.with_raw_response.retrieve(
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowance = await response.parse()
        assert_matches_type(Allowance, allowance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.allowance.with_streaming_response.retrieve(
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowance = await response.parse()
            assert_matches_type(Allowance, allowance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        allowance = await async_client.blockchain.allowance.approve(
            amount="amount",
            spender="spender",
        )
        assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.allowance.with_raw_response.approve(
            amount="amount",
            spender="spender",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allowance = await response.parse()
        assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.allowance.with_streaming_response.approve(
            amount="amount",
            spender="spender",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allowance = await response.parse()
            assert_matches_type(AllowanceApproveResponse, allowance, path=["response"])

        assert cast(Any, response.is_closed) is True
