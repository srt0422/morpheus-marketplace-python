# Shared Types

```python
from morpheus_marketplace.types import (
    Allowance,
    Balance,
    BidList,
    LatestBlock,
    Provider,
    Session,
    SessionList,
    TokenSupply,
)
```

# Blockchain

Methods:

- <code title="post /blockchain/approve">client.blockchain.<a href="./src/morpheus_marketplace/resources/blockchain/blockchain.py">approve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_approve_params.py">params</a>) -> None</code>

## Eth

Methods:

- <code title="post /blockchain/send/eth">client.blockchain.eth.<a href="./src/morpheus_marketplace/resources/blockchain/eth.py">send</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/eth_send_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/balance.py">Balance</a></code>

## Mor

Methods:

- <code title="post /blockchain/send/mor">client.blockchain.mor.<a href="./src/morpheus_marketplace/resources/blockchain/mor.py">send</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/mor_send_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/balance.py">Balance</a></code>

## Models

Types:

```python
from morpheus_marketplace.types.blockchain import Model, Stats, ModelListResponse
```

Methods:

- <code title="post /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/model_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/model.py">Model</a></code>
- <code title="get /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /blockchain/models/{id}">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">delete</a>(id) -> None</code>
- <code title="post /blockchain/models/{id}/session">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/model_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

### Bids

Methods:

- <code title="get /blockchain/models/{id}/bids">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/models/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/bid_list.py">BidList</a></code>
- <code title="get /blockchain/models/{id}/bids/active">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">active</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid_list.py">BidList</a></code>
- <code title="get /blockchain/models/{id}/bids/rated">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">rated</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid_list.py">BidList</a></code>

### Stats

Methods:

- <code title="get /blockchain/models/{id}/stats">client.blockchain.models.stats.<a href="./src/morpheus_marketplace/resources/blockchain/models/stats.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/stats.py">Stats</a></code>

## Bids

Types:

```python
from morpheus_marketplace.types.blockchain import Bid
```

Methods:

- <code title="post /blockchain/bids">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/bid_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/bid.py">Bid</a></code>
- <code title="get /blockchain/bids/{id}">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/bid.py">Bid</a></code>
- <code title="delete /blockchain/bids/{id}">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">delete</a>(id) -> None</code>
- <code title="post /blockchain/bids/{id}/session">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/bid_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

## Sessions

Methods:

- <code title="post /blockchain/sessions">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/session_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="get /blockchain/sessions/{id}">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="post /blockchain/sessions/{id}/close">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">close</a>(id) -> None</code>

### Budget

Types:

```python
from morpheus_marketplace.types.blockchain.sessions import Budget
```

Methods:

- <code title="get /blockchain/sessions/budget">client.blockchain.sessions.budget.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/budget.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/sessions/budget.py">Budget</a></code>

### User

Methods:

- <code title="get /blockchain/sessions/user">client.blockchain.sessions.user.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/user.py">list</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/sessions/user_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session_list.py">SessionList</a></code>

### Provider

Methods:

- <code title="get /blockchain/sessions/provider">client.blockchain.sessions.provider.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/provider.py">list</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/sessions/provider_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session_list.py">SessionList</a></code>

## Providers

Types:

```python
from morpheus_marketplace.types.blockchain import ProviderListResponse
```

Methods:

- <code title="post /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/provider_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/provider.py">Provider</a></code>
- <code title="get /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/provider_list_response.py">ProviderListResponse</a></code>
- <code title="delete /blockchain/providers/{id}">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">delete</a>(id) -> None</code>

### Bids

Methods:

- <code title="get /blockchain/providers/{id}/bids">client.blockchain.providers.bids.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/providers/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/bid_list.py">BidList</a></code>
- <code title="get /blockchain/providers/{id}/bids/active">client.blockchain.providers.bids.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids.py">active</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid_list.py">BidList</a></code>

## Balance

Methods:

- <code title="get /blockchain/balance">client.blockchain.balance.<a href="./src/morpheus_marketplace/resources/blockchain/balance.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/shared/balance.py">Balance</a></code>

## Allowance

Methods:

- <code title="get /blockchain/allowance">client.blockchain.allowance.<a href="./src/morpheus_marketplace/resources/blockchain/allowance.py">retrieve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/allowance_retrieve_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/allowance.py">Allowance</a></code>

## LatestBlock

Methods:

- <code title="get /blockchain/latestBlock">client.blockchain.latest_block.<a href="./src/morpheus_marketplace/resources/blockchain/latest_block.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/shared/latest_block.py">LatestBlock</a></code>

## Token

### Supply

Methods:

- <code title="get /blockchain/token/supply">client.blockchain.token.supply.<a href="./src/morpheus_marketplace/resources/blockchain/token/supply.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/shared/token_supply.py">TokenSupply</a></code>

## Transactions

Types:

```python
from morpheus_marketplace.types.blockchain import TransactionList
```

Methods:

- <code title="get /blockchain/transactions">client.blockchain.transactions.<a href="./src/morpheus_marketplace/resources/blockchain/transactions.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/transaction_list.py">TransactionList</a></code>

# Proxy

## Sessions

Methods:

- <code title="post /proxy/sessions/initiate">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions/sessions.py">initiate</a>(\*\*<a href="src/morpheus_marketplace/types/proxy/session_initiate_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="post /proxy/sessions/{id}/providerClaim">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions/sessions.py">provider_claim</a>(id, \*\*<a href="src/morpheus_marketplace/types/proxy/session_provider_claim_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/proxy/sessions/claimable_balance.py">ClaimableBalance</a></code>

### ProviderClaimableBalance

Types:

```python
from morpheus_marketplace.types.proxy.sessions import ClaimableBalance
```

Methods:

- <code title="get /proxy/sessions/{id}/providerClaimableBalance">client.proxy.sessions.provider_claimable_balance.<a href="./src/morpheus_marketplace/resources/proxy/sessions/provider_claimable_balance.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/proxy/sessions/claimable_balance.py">ClaimableBalance</a></code>
