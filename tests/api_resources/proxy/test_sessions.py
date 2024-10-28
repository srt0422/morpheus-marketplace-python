# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.proxy import ClaimableBalance
from morpheus_marketplace.types.shared import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_initiate(self, client: MorpheusMarketplace) -> None:
        session = client.proxy.sessions.initiate(
            model_id="model_12345",
            session_duration="3600",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_initiate(self, client: MorpheusMarketplace) -> None:
        response = client.proxy.sessions.with_raw_response.initiate(
            model_id="model_12345",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_initiate(self, client: MorpheusMarketplace) -> None:
        with client.proxy.sessions.with_streaming_response.initiate(
            model_id="model_12345",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_provider_claim(self, client: MorpheusMarketplace) -> None:
        session = client.proxy.sessions.provider_claim(
            id="id",
            claim="claim_abc123",
        )
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    def test_raw_response_provider_claim(self, client: MorpheusMarketplace) -> None:
        response = client.proxy.sessions.with_raw_response.provider_claim(
            id="id",
            claim="claim_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    def test_streaming_response_provider_claim(self, client: MorpheusMarketplace) -> None:
        with client.proxy.sessions.with_streaming_response.provider_claim(
            id="id",
            claim="claim_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ClaimableBalance, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provider_claim(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxy.sessions.with_raw_response.provider_claim(
                id="",
                claim="claim_abc123",
            )

    @parametrize
    def test_method_provider_claimable_balance(self, client: MorpheusMarketplace) -> None:
        session = client.proxy.sessions.provider_claimable_balance(
            "id",
        )
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    def test_raw_response_provider_claimable_balance(self, client: MorpheusMarketplace) -> None:
        response = client.proxy.sessions.with_raw_response.provider_claimable_balance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    def test_streaming_response_provider_claimable_balance(self, client: MorpheusMarketplace) -> None:
        with client.proxy.sessions.with_streaming_response.provider_claimable_balance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ClaimableBalance, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provider_claimable_balance(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.proxy.sessions.with_raw_response.provider_claimable_balance(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_initiate(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.proxy.sessions.initiate(
            model_id="model_12345",
            session_duration="3600",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.proxy.sessions.with_raw_response.initiate(
            model_id="model_12345",
            session_duration="3600",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.proxy.sessions.with_streaming_response.initiate(
            model_id="model_12345",
            session_duration="3600",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_provider_claim(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.proxy.sessions.provider_claim(
            id="id",
            claim="claim_abc123",
        )
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    async def test_raw_response_provider_claim(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.proxy.sessions.with_raw_response.provider_claim(
            id="id",
            claim="claim_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    async def test_streaming_response_provider_claim(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.proxy.sessions.with_streaming_response.provider_claim(
            id="id",
            claim="claim_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ClaimableBalance, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provider_claim(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxy.sessions.with_raw_response.provider_claim(
                id="",
                claim="claim_abc123",
            )

    @parametrize
    async def test_method_provider_claimable_balance(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.proxy.sessions.provider_claimable_balance(
            "id",
        )
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    async def test_raw_response_provider_claimable_balance(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.proxy.sessions.with_raw_response.provider_claimable_balance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ClaimableBalance, session, path=["response"])

    @parametrize
    async def test_streaming_response_provider_claimable_balance(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.proxy.sessions.with_streaming_response.provider_claimable_balance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ClaimableBalance, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provider_claimable_balance(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.proxy.sessions.with_raw_response.provider_claimable_balance(
                "",
            )
