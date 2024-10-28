# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Budget, Session, SessionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlockchainSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        )
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert_matches_type(Session, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.retrieve(
            "id",
        )
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert_matches_type(Session, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_budget(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.budget()
        assert_matches_type(Budget, blockchain_session, path=["response"])

    @parametrize
    def test_raw_response_budget(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.budget()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert_matches_type(Budget, blockchain_session, path=["response"])

    @parametrize
    def test_streaming_response_budget(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.budget() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert_matches_type(Budget, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_close(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.close(
            "id",
        )
        assert blockchain_session is None

    @parametrize
    def test_raw_response_close(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.close(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert blockchain_session is None

    @parametrize
    def test_streaming_response_close(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.close(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert blockchain_session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain_sessions.with_raw_response.close(
                "",
            )

    @parametrize
    def test_method_provider(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.provider(
            provider="provider_xyz789",
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_method_provider_with_all_params(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.provider(
            provider="provider_xyz789",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_raw_response_provider(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.provider(
            provider="provider_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_streaming_response_provider(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.provider(
            provider="provider_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert_matches_type(SessionList, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_user(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.user(
            user="user_abc123",
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_method_user_with_all_params(self, client: MorpheusMarketplace) -> None:
        blockchain_session = client.blockchain_sessions.user(
            user="user_abc123",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_raw_response_user(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain_sessions.with_raw_response.user(
            user="user_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = response.parse()
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    def test_streaming_response_user(self, client: MorpheusMarketplace) -> None:
        with client.blockchain_sessions.with_streaming_response.user(
            user="user_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = response.parse()
            assert_matches_type(SessionList, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBlockchainSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        )
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.create(
            approval="approval_abc123",
            approval_sig="signature_xyz789",
            stake="500",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert_matches_type(Session, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.retrieve(
            "id",
        )
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert_matches_type(Session, blockchain_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert_matches_type(Session, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_budget(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.budget()
        assert_matches_type(Budget, blockchain_session, path=["response"])

    @parametrize
    async def test_raw_response_budget(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.budget()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert_matches_type(Budget, blockchain_session, path=["response"])

    @parametrize
    async def test_streaming_response_budget(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.budget() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert_matches_type(Budget, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.close(
            "id",
        )
        assert blockchain_session is None

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.close(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert blockchain_session is None

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.close(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert blockchain_session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain_sessions.with_raw_response.close(
                "",
            )

    @parametrize
    async def test_method_provider(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.provider(
            provider="provider_xyz789",
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_method_provider_with_all_params(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.provider(
            provider="provider_xyz789",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_raw_response_provider(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.provider(
            provider="provider_xyz789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_streaming_response_provider(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.provider(
            provider="provider_xyz789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert_matches_type(SessionList, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_user(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.user(
            user="user_abc123",
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_method_user_with_all_params(self, async_client: AsyncMorpheusMarketplace) -> None:
        blockchain_session = await async_client.blockchain_sessions.user(
            user="user_abc123",
            limit=10,
            offset=0,
        )
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_raw_response_user(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain_sessions.with_raw_response.user(
            user="user_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_session = await response.parse()
        assert_matches_type(SessionList, blockchain_session, path=["response"])

    @parametrize
    async def test_streaming_response_user(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain_sessions.with_streaming_response.user(
            user="user_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_session = await response.parse()
            assert_matches_type(SessionList, blockchain_session, path=["response"])

        assert cast(Any, response.is_closed) is True
