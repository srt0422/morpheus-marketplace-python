# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from morpheus_marketplace import MorpheusMarketplace, AsyncMorpheusMarketplace
from morpheus_marketplace.types.shared import Session
from morpheus_marketplace.types.blockchain import SessionCloseResponse, SessionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MorpheusMarketplace) -> None:
        session = client.blockchain.sessions.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.sessions.with_raw_response.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.sessions.with_streaming_response.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MorpheusMarketplace) -> None:
        session = client.blockchain.sessions.retrieve(
            "id",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_close(self, client: MorpheusMarketplace) -> None:
        session = client.blockchain.sessions.close(
            "id",
        )
        assert_matches_type(SessionCloseResponse, session, path=["response"])

    @parametrize
    def test_raw_response_close(self, client: MorpheusMarketplace) -> None:
        response = client.blockchain.sessions.with_raw_response.close(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCloseResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_close(self, client: MorpheusMarketplace) -> None:
        with client.blockchain.sessions.with_streaming_response.close(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCloseResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: MorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.blockchain.sessions.with_raw_response.close(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.blockchain.sessions.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.sessions.with_raw_response.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.sessions.with_streaming_response.create(
            approval="approval",
            approval_sig="approvalSig",
            stake="stake",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.blockchain.sessions.retrieve(
            "id",
        )
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        session = await async_client.blockchain.sessions.close(
            "id",
        )
        assert_matches_type(SessionCloseResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        response = await async_client.blockchain.sessions.with_raw_response.close(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCloseResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        async with async_client.blockchain.sessions.with_streaming_response.close(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCloseResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncMorpheusMarketplace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.blockchain.sessions.with_raw_response.close(
                "",
            )
