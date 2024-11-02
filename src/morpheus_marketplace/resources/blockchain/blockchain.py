# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .eth import (
    EthResource,
    AsyncEthResource,
    EthResourceWithRawResponse,
    AsyncEthResourceWithRawResponse,
    EthResourceWithStreamingResponse,
    AsyncEthResourceWithStreamingResponse,
)
from .mor import (
    MorResource,
    AsyncMorResource,
    MorResourceWithRawResponse,
    AsyncMorResourceWithRawResponse,
    MorResourceWithStreamingResponse,
    AsyncMorResourceWithStreamingResponse,
)
from .bids import (
    BidsResource,
    AsyncBidsResource,
    BidsResourceWithRawResponse,
    AsyncBidsResourceWithRawResponse,
    BidsResourceWithStreamingResponse,
    AsyncBidsResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from ...types import blockchain_approve_params
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .allowance import (
    AllowanceResource,
    AsyncAllowanceResource,
    AllowanceResourceWithRawResponse,
    AsyncAllowanceResourceWithRawResponse,
    AllowanceResourceWithStreamingResponse,
    AsyncAllowanceResourceWithStreamingResponse,
)
from .providers import (
    ProvidersResource,
    AsyncProvidersResource,
    ProvidersResourceWithRawResponse,
    AsyncProvidersResourceWithRawResponse,
    ProvidersResourceWithStreamingResponse,
    AsyncProvidersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .token.token import TokenResource, AsyncTokenResource
from .latest_block import (
    LatestBlockResource,
    AsyncLatestBlockResource,
    LatestBlockResourceWithRawResponse,
    AsyncLatestBlockResourceWithRawResponse,
    LatestBlockResourceWithStreamingResponse,
    AsyncLatestBlockResourceWithStreamingResponse,
)
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from .models.models import ModelsResource, AsyncModelsResource
from ..._base_client import make_request_options
from .sessions.sessions import SessionsResource, AsyncSessionsResource
from .providers.providers import ProvidersResource, AsyncProvidersResource

__all__ = ["BlockchainResource", "AsyncBlockchainResource"]


class BlockchainResource(SyncAPIResource):
    @cached_property
    def eth(self) -> EthResource:
        return EthResource(self._client)

    @cached_property
    def mor(self) -> MorResource:
        return MorResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def bids(self) -> BidsResource:
        return BidsResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def providers(self) -> ProvidersResource:
        return ProvidersResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

    @cached_property
    def allowance(self) -> AllowanceResource:
        return AllowanceResource(self._client)

    @cached_property
    def latest_block(self) -> LatestBlockResource:
        return LatestBlockResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlockchainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BlockchainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockchainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return BlockchainResourceWithStreamingResponse(self)

    def approve(
        self,
        *,
        amount: str,
        spender: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve allowance

        Args:
          amount: Amount to approve

          spender: Spender Ethereum address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/blockchain/approve",
            body=maybe_transform(
                {
                    "amount": amount,
                    "spender": spender,
                },
                blockchain_approve_params.BlockchainApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBlockchainResource(AsyncAPIResource):
    @cached_property
    def eth(self) -> AsyncEthResource:
        return AsyncEthResource(self._client)

    @cached_property
    def mor(self) -> AsyncMorResource:
        return AsyncMorResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def bids(self) -> AsyncBidsResource:
        return AsyncBidsResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        return AsyncProvidersResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

    @cached_property
    def allowance(self) -> AsyncAllowanceResource:
        return AsyncAllowanceResource(self._client)

    @cached_property
    def latest_block(self) -> AsyncLatestBlockResource:
        return AsyncLatestBlockResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlockchainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockchainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockchainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/srt0422/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBlockchainResourceWithStreamingResponse(self)

    async def approve(
        self,
        *,
        amount: str,
        spender: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve allowance

        Args:
          amount: Amount to approve

          spender: Spender Ethereum address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/blockchain/approve",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "spender": spender,
                },
                blockchain_approve_params.BlockchainApproveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BlockchainResourceWithRawResponse:
    def __init__(self, blockchain: BlockchainResource) -> None:
        self._blockchain = blockchain

        self.approve = to_raw_response_wrapper(
            blockchain.approve,
        )

    @cached_property
    def eth(self) -> EthResourceWithRawResponse:
        return EthResourceWithRawResponse(self._blockchain.eth)

    @cached_property
    def mor(self) -> MorResourceWithRawResponse:
        return MorResourceWithRawResponse(self._blockchain.mor)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._blockchain.models)

    @cached_property
    def bids(self) -> BidsResourceWithRawResponse:
        return BidsResourceWithRawResponse(self._blockchain.bids)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._blockchain.sessions)

    @cached_property
    def providers(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self._blockchain.providers)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._blockchain.balance)

    @cached_property
    def allowance(self) -> AllowanceResourceWithRawResponse:
        return AllowanceResourceWithRawResponse(self._blockchain.allowance)

    @cached_property
    def latest_block(self) -> LatestBlockResourceWithRawResponse:
        return LatestBlockResourceWithRawResponse(self._blockchain.latest_block)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._blockchain.token)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._blockchain.transactions)


class AsyncBlockchainResourceWithRawResponse:
    def __init__(self, blockchain: AsyncBlockchainResource) -> None:
        self._blockchain = blockchain

        self.approve = async_to_raw_response_wrapper(
            blockchain.approve,
        )

    @cached_property
    def eth(self) -> AsyncEthResourceWithRawResponse:
        return AsyncEthResourceWithRawResponse(self._blockchain.eth)

    @cached_property
    def mor(self) -> AsyncMorResourceWithRawResponse:
        return AsyncMorResourceWithRawResponse(self._blockchain.mor)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._blockchain.models)

    @cached_property
    def bids(self) -> AsyncBidsResourceWithRawResponse:
        return AsyncBidsResourceWithRawResponse(self._blockchain.bids)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._blockchain.sessions)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self._blockchain.providers)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._blockchain.balance)

    @cached_property
    def allowance(self) -> AsyncAllowanceResourceWithRawResponse:
        return AsyncAllowanceResourceWithRawResponse(self._blockchain.allowance)

    @cached_property
    def latest_block(self) -> AsyncLatestBlockResourceWithRawResponse:
        return AsyncLatestBlockResourceWithRawResponse(self._blockchain.latest_block)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._blockchain.token)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._blockchain.transactions)


class BlockchainResourceWithStreamingResponse:
    def __init__(self, blockchain: BlockchainResource) -> None:
        self._blockchain = blockchain

        self.approve = to_streamed_response_wrapper(
            blockchain.approve,
        )

    @cached_property
    def eth(self) -> EthResourceWithStreamingResponse:
        return EthResourceWithStreamingResponse(self._blockchain.eth)

    @cached_property
    def mor(self) -> MorResourceWithStreamingResponse:
        return MorResourceWithStreamingResponse(self._blockchain.mor)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._blockchain.models)

    @cached_property
    def bids(self) -> BidsResourceWithStreamingResponse:
        return BidsResourceWithStreamingResponse(self._blockchain.bids)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._blockchain.sessions)

    @cached_property
    def providers(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self._blockchain.providers)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._blockchain.balance)

    @cached_property
    def allowance(self) -> AllowanceResourceWithStreamingResponse:
        return AllowanceResourceWithStreamingResponse(self._blockchain.allowance)

    @cached_property
    def latest_block(self) -> LatestBlockResourceWithStreamingResponse:
        return LatestBlockResourceWithStreamingResponse(self._blockchain.latest_block)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._blockchain.token)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._blockchain.transactions)


class AsyncBlockchainResourceWithStreamingResponse:
    def __init__(self, blockchain: AsyncBlockchainResource) -> None:
        self._blockchain = blockchain

        self.approve = async_to_streamed_response_wrapper(
            blockchain.approve,
        )

    @cached_property
    def eth(self) -> AsyncEthResourceWithStreamingResponse:
        return AsyncEthResourceWithStreamingResponse(self._blockchain.eth)

    @cached_property
    def mor(self) -> AsyncMorResourceWithStreamingResponse:
        return AsyncMorResourceWithStreamingResponse(self._blockchain.mor)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._blockchain.models)

    @cached_property
    def bids(self) -> AsyncBidsResourceWithStreamingResponse:
        return AsyncBidsResourceWithStreamingResponse(self._blockchain.bids)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._blockchain.sessions)

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self._blockchain.providers)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._blockchain.balance)

    @cached_property
    def allowance(self) -> AsyncAllowanceResourceWithStreamingResponse:
        return AsyncAllowanceResourceWithStreamingResponse(self._blockchain.allowance)

    @cached_property
    def latest_block(self) -> AsyncLatestBlockResourceWithStreamingResponse:
        return AsyncLatestBlockResourceWithStreamingResponse(self._blockchain.latest_block)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._blockchain.token)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._blockchain.transactions)
