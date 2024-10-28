# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Session
from morpheus_marketplace.types.blockchain import Model, ModelListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MorpheusMarketplace) -> None:
        model = client.blockchain.models.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MorpheusMarketplace) -> None:
        model = client.blockchain.models.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
            tags=["machine learning", "image recognition"],
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.with_raw_response.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.with_streaming_response.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: MorpheusMarketplace) -> None:
        model = client.blockchain.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: MorpheusMarketplace) -> None:
        model = client.blockchain.models.delete(
            "id",
        )
        assert model is None

    @parametrize
    def test_raw_response_delete(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @parametrize
    def test_streaming_response_delete(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.models.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_session(self, client: MorpheusMarketplace) -> None:
        model = client.blockchain.models.session(
            id="id",
            session_duration="3600",
        )
        assert_matches_type(Session, model, path=["response"])

    @parametrize
    def test_raw_response_session(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.models.with_raw_response.session(
            id="id",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Session, model, path=["response"])

    @parametrize
    def test_streaming_response_session(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.models.with_streaming_response.session(
            id="id",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Session, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_session(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.models.with_raw_response.session(
                id="",
                session_duration="3600",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        model = await async_client.blockchain.models.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMorpheusMarketplace) -> None:
        model = await async_client.blockchain.models.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
            tags=["machine learning", "image recognition"],
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.with_raw_response.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.with_streaming_response.create(
            fee="0.01",
            ipfs_id="QmX...",
            model_id="mod-67890",
            name="Image Recognition Model",
            stake="1000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        model = await async_client.blockchain.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        model = await async_client.blockchain.models.delete(
            "id",
        )
        assert model is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.models.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        model = await async_client.blockchain.models.session(
            id="id",
            session_duration="3600",
        )
        assert_matches_type(Session, model, path=["response"])

    @parametrize
    async def test_raw_response_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.models.with_raw_response.session(
            id="id",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Session, model, path=["response"])

    @parametrize
    async def test_streaming_response_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.models.with_streaming_response.session(
            id="id",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Session, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_session(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.models.with_raw_response.session(
                id="",
                session_duration="3600",
            )
