# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bids import (
    BidsResource,
    AsyncBidsResource,
    BidsResourceWithRawResponse,
    AsyncBidsResourceWithRawResponse,
    BidsResourceWithStreamingResponse,
    AsyncBidsResourceWithStreamingResponse,
)
from .send import (
    SendResource,
    AsyncSendResource,
    SendResourceWithRawResponse,
    AsyncSendResourceWithRawResponse,
    SendResourceWithStreamingResponse,
    AsyncSendResourceWithStreamingResponse,
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
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
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
from .sessions.sessions import SessionsResource, AsyncSessionsResource
from .providers.providers import ProvidersResource, AsyncProvidersResource

__all__ = ["BlockchainResource", "AsyncBlockchainResource"]


class BlockchainResource(SyncAPIResource):
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
    def send(self) -> SendResource:
        return SendResource(self._client)

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

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return BlockchainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockchainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return BlockchainResourceWithStreamingResponse(self)


class AsyncBlockchainResource(AsyncAPIResource):
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
    def send(self) -> AsyncSendResource:
        return AsyncSendResource(self._client)

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

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockchainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockchainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/morpheus-marketplace-python#with_streaming_response
        """
        return AsyncBlockchainResourceWithStreamingResponse(self)


class BlockchainResourceWithRawResponse:
    def __init__(self, blockchain: BlockchainResource) -> None:
        self._blockchain = blockchain

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
    def send(self) -> SendResourceWithRawResponse:
        return SendResourceWithRawResponse(self._blockchain.send)

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
    def send(self) -> AsyncSendResourceWithRawResponse:
        return AsyncSendResourceWithRawResponse(self._blockchain.send)

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
    def send(self) -> SendResourceWithStreamingResponse:
        return SendResourceWithStreamingResponse(self._blockchain.send)

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
    def send(self) -> AsyncSendResourceWithStreamingResponse:
        return AsyncSendResourceWithStreamingResponse(self._blockchain.send)

    @cached_property
    def latest_block(self) -> AsyncLatestBlockResourceWithStreamingResponse:
        return AsyncLatestBlockResourceWithStreamingResponse(self._blockchain.latest_block)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._blockchain.token)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._blockchain.transactions)
