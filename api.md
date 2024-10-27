# Shared Types

```python
from morpheus_marketplace.types import Bid, Session
```

# Blockchain

## Models

Types:

```python
from morpheus_marketplace.types.blockchain import (
    Model,
    ModelListResponse,
    ModelDeleteResponse,
    ModelExistsResponse,
    ModelResetstatsResponse,
)
```

Methods:

- <code title="post /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/model_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/model.py">Model</a></code>
- <code title="get /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /blockchain/models/{id}">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">delete</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/model_delete_response.py">ModelDeleteResponse</a></code>
- <code title="get /blockchain/models/{id}/exists">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">exists</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/model_exists_response.py">ModelExistsResponse</a></code>
- <code title="post /blockchain/models/{id}/resetstats">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">resetstats</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/model_resetstats_response.py">ModelResetstatsResponse</a></code>
- <code title="post /blockchain/models/{id}/session">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/model_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

### Bids

Methods:

- <code title="get /blockchain/models/{id}/bids">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/models/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>
- <code title="get /blockchain/models/{id}/bids/active">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">active</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>
- <code title="get /blockchain/models/{id}/bids/rated">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">rated</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>

### Minstake

Types:

```python
from morpheus_marketplace.types.blockchain.models import MinStake, MinstakeSetResponse
```

Methods:

- <code title="get /blockchain/models/minstake">client.blockchain.models.minstake.<a href="./src/morpheus_marketplace/resources/blockchain/models/minstake.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/models/min_stake.py">MinStake</a></code>
- <code title="post /blockchain/models/minstake">client.blockchain.models.minstake.<a href="./src/morpheus_marketplace/resources/blockchain/models/minstake.py">set</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/models/minstake_set_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/models/minstake_set_response.py">MinstakeSetResponse</a></code>

### Stats

Types:

```python
from morpheus_marketplace.types.blockchain.models import ModelStats
```

Methods:

- <code title="get /blockchain/models/{id}/stats">client.blockchain.models.stats.<a href="./src/morpheus_marketplace/resources/blockchain/models/stats.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/models/model_stats.py">ModelStats</a></code>

## Bids

Types:

```python
from morpheus_marketplace.types.blockchain import (
    BidCreateResponse,
    BidRetrieveResponse,
    BidDeleteResponse,
)
```

Methods:

- <code title="post /blockchain/bids">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/bid_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/bid_create_response.py">BidCreateResponse</a></code>
- <code title="get /blockchain/bids/{id}">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/bid_retrieve_response.py">BidRetrieveResponse</a></code>
- <code title="delete /blockchain/bids/{id}">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">delete</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/bid_delete_response.py">BidDeleteResponse</a></code>
- <code title="post /blockchain/bids/{id}/session">client.blockchain.bids.<a href="./src/morpheus_marketplace/resources/blockchain/bids.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/bid_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

## Sessions

Types:

```python
from morpheus_marketplace.types.blockchain import SessionRetrieveResponse, SessionCloseResponse
```

Methods:

- <code title="post /blockchain/sessions">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/session_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="get /blockchain/sessions/{id}">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/session_retrieve_response.py">SessionRetrieveResponse</a></code>
- <code title="post /blockchain/sessions/{id}/close">client.blockchain.sessions.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/sessions.py">close</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/session_close_response.py">SessionCloseResponse</a></code>

### User

Types:

```python
from morpheus_marketplace.types.blockchain.sessions import UserListResponse
```

Methods:

- <code title="get /blockchain/sessions/user">client.blockchain.sessions.user.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/user.py">list</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/sessions/user_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/sessions/user_list_response.py">UserListResponse</a></code>

### Provider

Types:

```python
from morpheus_marketplace.types.blockchain.sessions import ProviderListResponse
```

Methods:

- <code title="get /blockchain/sessions/provider">client.blockchain.sessions.provider.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/provider.py">list</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/sessions/provider_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/sessions/provider_list_response.py">ProviderListResponse</a></code>

### Budget

Types:

```python
from morpheus_marketplace.types.blockchain.sessions import BudgetListResponse
```

Methods:

- <code title="get /blockchain/sessions/budget">client.blockchain.sessions.budget.<a href="./src/morpheus_marketplace/resources/blockchain/sessions/budget.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/sessions/budget_list_response.py">BudgetListResponse</a></code>

## Providers

Types:

```python
from morpheus_marketplace.types.blockchain import (
    Provider,
    ProviderListResponse,
    ProviderDeleteResponse,
)
```

Methods:

- <code title="post /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/provider_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/provider.py">Provider</a></code>
- <code title="get /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/provider_list_response.py">ProviderListResponse</a></code>
- <code title="delete /blockchain/providers/{id}">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">delete</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/provider_delete_response.py">ProviderDeleteResponse</a></code>

### Bids

Methods:

- <code title="get /blockchain/providers/{id}/bids">client.blockchain.providers.bids.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/providers/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>

#### Active

Methods:

- <code title="get /blockchain/providers/{id}/bids/active">client.blockchain.providers.bids.active.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids/active.py">list</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>

## Balance

Types:

```python
from morpheus_marketplace.types.blockchain import Balance
```

Methods:

- <code title="get /blockchain/balance">client.blockchain.balance.<a href="./src/morpheus_marketplace/resources/blockchain/balance.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/balance.py">Balance</a></code>

## Allowance

Types:

```python
from morpheus_marketplace.types.blockchain import Allowance, AllowanceApproveResponse
```

Methods:

- <code title="get /blockchain/allowance">client.blockchain.allowance.<a href="./src/morpheus_marketplace/resources/blockchain/allowance.py">retrieve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/allowance_retrieve_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/allowance.py">Allowance</a></code>
- <code title="post /blockchain/allowance">client.blockchain.allowance.<a href="./src/morpheus_marketplace/resources/blockchain/allowance.py">approve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/allowance_approve_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/allowance_approve_response.py">AllowanceApproveResponse</a></code>

## Send

Types:

```python
from morpheus_marketplace.types.blockchain import SendEthResponse, SendMorResponse
```

Methods:

- <code title="post /blockchain/send/eth">client.blockchain.send.<a href="./src/morpheus_marketplace/resources/blockchain/send.py">eth</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/send_eth_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/send_eth_response.py">SendEthResponse</a></code>
- <code title="post /blockchain/send/mor">client.blockchain.send.<a href="./src/morpheus_marketplace/resources/blockchain/send.py">mor</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/send_mor_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/send_mor_response.py">SendMorResponse</a></code>

## LatestBlock

Types:

```python
from morpheus_marketplace.types.blockchain import LatestBlock
```

Methods:

- <code title="get /blockchain/latestBlock">client.blockchain.latest_block.<a href="./src/morpheus_marketplace/resources/blockchain/latest_block.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/latest_block.py">LatestBlock</a></code>

## Token

### Supply

Types:

```python
from morpheus_marketplace.types.blockchain.token import TokenSupply
```

Methods:

- <code title="get /blockchain/token/supply">client.blockchain.token.supply.<a href="./src/morpheus_marketplace/resources/blockchain/token/supply.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/token/token_supply.py">TokenSupply</a></code>

## Transactions

Types:

```python
from morpheus_marketplace.types.blockchain import TransactionList
```

Methods:

- <code title="get /blockchain/transactions">client.blockchain.transactions.<a href="./src/morpheus_marketplace/resources/blockchain/transactions.py">list</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/transaction_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/transaction_list.py">TransactionList</a></code>

# Proxy

## Sessions

Types:

```python
from morpheus_marketplace.types.proxy import (
    SessionProviderClaimResponse,
    SessionProviderClaimableBalanceResponse,
)
```

Methods:

- <code title="post /proxy/sessions/initiate">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">initiate</a>(\*\*<a href="src/morpheus_marketplace/types/proxy/session_initiate_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="post /proxy/sessions/{id}/providerClaim">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">provider_claim</a>(id, \*\*<a href="src/morpheus_marketplace/types/proxy/session_provider_claim_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/proxy/session_provider_claim_response.py">SessionProviderClaimResponse</a></code>
- <code title="get /proxy/sessions/{id}/providerClaimableBalance">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">provider_claimable_balance</a>(id) -> <a href="./src/morpheus_marketplace/types/proxy/session_provider_claimable_balance_response.py">SessionProviderClaimableBalanceResponse</a></code>
