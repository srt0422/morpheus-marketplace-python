# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.blockchain.models import ModelStats

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        stat = client.blockchain.models.stats.retrieve(
            "id",
        )
        assert_matches_type(ModelStats, stat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.stats.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(ModelStats, stat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.stats.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(ModelStats, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.models.stats.with_raw_response.retrieve(
                "",
            )


class TestAsyncStats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        stat = await async_client.blockchain.models.stats.retrieve(
            "id",
        )
        assert_matches_type(ModelStats, stat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.stats.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(ModelStats, stat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.stats.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(ModelStats, stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.models.stats.with_raw_response.retrieve(
                "",
            )
