# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import BidList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBids:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.providers.bids.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.providers.bids.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
            limit=10,
            offset=0,
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.bids.with_raw_response.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.bids.with_streaming_response.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert_matches_type(BidList, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.providers.bids.with_raw_response.list(
                id="",
            )

    @parametrize
    def test_method_active(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.providers.bids.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    def test_raw_response_active(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.providers.bids.with_raw_response.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    def test_streaming_response_active(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.providers.bids.with_streaming_response.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert_matches_type(BidList, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_active(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.providers.bids.with_raw_response.active(
                "",
            )


class TestAsyncBids:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.providers.bids.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.providers.bids.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
            limit=10,
            offset=0,
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.bids.with_raw_response.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.bids.with_streaming_response.list(
            id="4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert_matches_type(BidList, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.providers.bids.with_raw_response.list(
                id="",
            )

    @parametrize
    async def test_method_active(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.providers.bids.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    async def test_raw_response_active(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.providers.bids.with_raw_response.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert_matches_type(BidList, bid, path=["response"])

    @parametrize
    async def test_streaming_response_active(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.providers.bids.with_streaming_response.active(
            "4592d8f8d7b001e72cb26a73e4fa1806a51ac79d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert_matches_type(BidList, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_active(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.providers.bids.with_raw_response.active(
                "",
            )
