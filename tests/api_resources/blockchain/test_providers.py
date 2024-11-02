# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Provider
from morpheus_marketplace.types.blockchain import ProviderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MorpheusMarketplace) -> None:
        provider = client.blockchain.providers.create(
            endpoint="https://provider.example.com",
            stake="2000",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.with_raw_response.create(
            endpoint="https://provider.example.com",
            stake="2000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.with_streaming_response.create(
            endpoint="https://provider.example.com",
            stake="2000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: MorpheusMarketplace) -> None:
        provider = client.blockchain.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: MorpheusMarketplace) -> None:
        provider = client.blockchain.providers.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        )
        assert provider is None

    @parametrize
    def test_raw_response_delete(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.with_raw_response.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert provider is None

    @parametrize
    def test_streaming_response_delete(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.with_streaming_response.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert provider is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.providers.with_raw_response.delete(
                "",
            )


class TestAsyncProviders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider = await async_client.blockchain.providers.create(
            endpoint="https://provider.example.com",
            stake="2000",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.with_raw_response.create(
            endpoint="https://provider.example.com",
            stake="2000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.with_streaming_response.create(
            endpoint="https://provider.example.com",
            stake="2000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider = await async_client.blockchain.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider = await async_client.blockchain.providers.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        )
        assert provider is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.with_raw_response.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert provider is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.with_streaming_response.delete(
            "0x1234567890abcdef1234567890abcdef12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert provider is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.providers.with_raw_response.delete(
                "",
            )
