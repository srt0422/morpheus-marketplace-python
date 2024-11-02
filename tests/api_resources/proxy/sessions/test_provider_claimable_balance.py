# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.proxy.sessions import ClaimableBalance

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviderClaimableBalance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        provider_claimable_balance = client.proxy.sessions.provider_claimable_balance.retrieve(
            "id",
        )
        assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.proxy.sessions.provider_claimable_balance.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_claimable_balance = response.parse()
        assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.proxy.sessions.provider_claimable_balance.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_claimable_balance = response.parse()
            assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxy.sessions.provider_claimable_balance.with_raw_response.retrieve(
                "",
            )


class TestAsyncProviderClaimableBalance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        provider_claimable_balance = await async_client.proxy.sessions.provider_claimable_balance.retrieve(
            "id",
        )
        assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.proxy.sessions.provider_claimable_balance.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_claimable_balance = await response.parse()
        assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.proxy.sessions.provider_claimable_balance.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_claimable_balance = await response.parse()
            assert_matches_type(ClaimableBalance, provider_claimable_balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxy.sessions.provider_claimable_balance.with_raw_response.retrieve(
                "",
            )
