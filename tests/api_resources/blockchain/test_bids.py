# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Session
from morpheus_marketplace.types.blockchain import Bid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBids:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.bids.create(
            model_id="model_12345",
            price_per_second="0.005",
        )
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.bids.with_raw_response.create(
            model_id="model_12345",
            price_per_second="0.005",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.bids.with_streaming_response.create(
            model_id="model_12345",
            price_per_second="0.005",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert_matches_type(Bid, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.bids.retrieve(
            "id",
        )
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.bids.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.bids.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert_matches_type(Bid, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.bids.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_delete(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.bids.delete(
            "id",
        )
        assert bid is None

    @parametrize
    def test_raw_response_delete(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.bids.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert bid is None

    @parametrize
    def test_streaming_response_delete(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.bids.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert bid is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.bids.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_session(self, client: MorpheusMarketplace) -> None:
        bid = client.blockchain.bids.session(
            id="id",
            session_duration="3600",
        )
        assert_matches_type(Session, bid, path=["response"])

    @parametrize
    def test_raw_response_session(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.bids.with_raw_response.session(
            id="id",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = response.parse()
        assert_matches_type(Session, bid, path=["response"])

    @parametrize
    def test_streaming_response_session(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.bids.with_streaming_response.session(
            id="id",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = response.parse()
            assert_matches_type(Session, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_session(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.bids.with_raw_response.session(
                id="",
                session_duration="3600",
            )


class TestAsyncBids:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.bids.create(
            model_id="model_12345",
            price_per_second="0.005",
        )
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.bids.with_raw_response.create(
            model_id="model_12345",
            price_per_second="0.005",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.bids.with_streaming_response.create(
            model_id="model_12345",
            price_per_second="0.005",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert_matches_type(Bid, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.bids.retrieve(
            "id",
        )
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.bids.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert_matches_type(Bid, bid, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.bids.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert_matches_type(Bid, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.bids.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.bids.delete(
            "id",
        )
        assert bid is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.bids.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert bid is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.bids.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert bid is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.bids.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        bid = await async_client.blockchain.bids.session(
            id="id",
            session_duration="3600",
        )
        assert_matches_type(Session, bid, path=["response"])

    @parametrize
    async def test_raw_response_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.bids.with_raw_response.session(
            id="id",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bid = await response.parse()
        assert_matches_type(Session, bid, path=["response"])

    @parametrize
    async def test_streaming_response_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.bids.with_streaming_response.session(
            id="id",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bid = await response.parse()
            assert_matches_type(Session, bid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.bids.with_raw_response.session(
                id="",
                session_duration="3600",
            )
