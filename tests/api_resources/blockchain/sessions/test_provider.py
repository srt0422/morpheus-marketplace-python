# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import SessionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProvider:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MorpheusMarketplace) -> None:
        provider = client.blockchain.sessions.provider.list(
            provider="provider_xyz789",
        )
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MorpheusMarketplace) -> None:
        provider = client.blockchain.sessions.provider.list(
            provider="provider_xyz789",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.sessions.provider.with_raw_response.list(
            provider="provider_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.sessions.provider.with_streaming_response.list(
            provider="provider_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(SessionList, provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProvider:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider = await async_client.blockchain.sessions.provider.list(
            provider="provider_xyz789",
        )
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider = await async_client.blockchain.sessions.provider.list(
            provider="provider_xyz789",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.sessions.provider.with_raw_response.list(
            provider="provider_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(SessionList, provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.sessions.provider.with_streaming_response.list(
            provider="provider_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(SessionList, provider, path=["response"])

        assert cast(Any, response.is_closed) is True
