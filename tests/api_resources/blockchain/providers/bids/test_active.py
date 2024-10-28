# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain.providers.bids import ActiveListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MorpheusMarketplace) -> None:
        active = client.blockchain.providers.bids.active.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        )
        assert_matches_type(ActiveListResponse, active, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.bids.active.with_raw_response.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active = response.parse()
        assert_matches_type(ActiveListResponse, active, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.bids.active.with_streaming_response.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active = response.parse()
            assert_matches_type(ActiveListResponse, active, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.providers.bids.active.with_raw_response.list(
                "",
            )


class TestAsyncActive:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        active = await async_client.blockchain.providers.bids.active.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        )
        assert_matches_type(ActiveListResponse, active, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.bids.active.with_raw_response.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active = await response.parse()
        assert_matches_type(ActiveListResponse, active, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.bids.active.with_streaming_response.list(
            "0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active = await response.parse()
            assert_matches_type(ActiveListResponse, active, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.providers.bids.active.with_raw_response.list(
                "",
            )
