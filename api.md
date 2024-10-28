# Shared Types

```python
from morpheus_marketplace.types import Bid, Budget, Session, SessionList
```

# Blockchain

Types:

```python
from morpheus_marketplace.types import Balance
```

Methods:

- <code title="post /blockchain/approve">client.blockchain.<a href="./src/morpheus_marketplace/resources/blockchain/blockchain.py">approve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_approve_params.py">params</a>) -> None</code>
- <code title="post /blockchain/send/eth">client.blockchain.<a href="./src/morpheus_marketplace/resources/blockchain/blockchain.py">eth_send</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_eth_send_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/balance.py">Balance</a></code>
- <code title="post /blockchain/send/mor">client.blockchain.<a href="./src/morpheus_marketplace/resources/blockchain/blockchain.py">mor_send</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_mor_send_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/balance.py">Balance</a></code>

## Models

Types:

```python
from morpheus_marketplace.types.blockchain import Model, ModelListResponse
```

Methods:

- <code title="post /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/model_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/model.py">Model</a></code>
- <code title="get /blockchain/models">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /blockchain/models/{id}">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">delete</a>(id) -> None</code>
- <code title="post /blockchain/models/{id}/session">client.blockchain.models.<a href="./src/morpheus_marketplace/resources/blockchain/models/models.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/model_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

### Bids

Types:

```python
from morpheus_marketplace.types.blockchain.models import (
    BidListResponse,
    BidActiveResponse,
    BidRatedResponse,
)
```

Methods:

- <code title="get /blockchain/models/{id}/bids">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/models/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/models/bid_list_response.py">BidListResponse</a></code>
- <code title="get /blockchain/models/{id}/bids/active">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">active</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/models/bid_active_response.py">BidActiveResponse</a></code>
- <code title="get /blockchain/models/{id}/bids/rated">client.blockchain.models.bids.<a href="./src/morpheus_marketplace/resources/blockchain/models/bids.py">rated</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/models/bid_rated_response.py">BidRatedResponse</a></code>

### Stats

Types:

```python
from morpheus_marketplace.types.blockchain.models import ModelStats
```

Methods:

- <code title="get /blockchain/models/{id}/stats">client.blockchain.models.stats.<a href="./src/morpheus_marketplace/resources/blockchain/models/stats.py">list</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/models/model_stats.py">ModelStats</a></code>

## Providers

Types:

```python
from morpheus_marketplace.types.blockchain import Provider, ProviderListResponse
```

Methods:

- <code title="post /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/provider_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/provider.py">Provider</a></code>
- <code title="get /blockchain/providers">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/provider_list_response.py">ProviderListResponse</a></code>
- <code title="delete /blockchain/providers/{id}">client.blockchain.providers.<a href="./src/morpheus_marketplace/resources/blockchain/providers/providers.py">delete</a>(id) -> None</code>

### Bids

Types:

```python
from morpheus_marketplace.types.blockchain.providers import BidListResponse
```

Methods:

- <code title="get /blockchain/providers/{id}/bids">client.blockchain.providers.bids.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids/bids.py">list</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain/providers/bid_list_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/providers/bid_list_response.py">BidListResponse</a></code>

#### Active

Types:

```python
from morpheus_marketplace.types.blockchain.providers.bids import ActiveListResponse
```

Methods:

- <code title="get /blockchain/providers/{id}/bids/active">client.blockchain.providers.bids.active.<a href="./src/morpheus_marketplace/resources/blockchain/providers/bids/active.py">list</a>(id) -> <a href="./src/morpheus_marketplace/types/blockchain/providers/bids/active_list_response.py">ActiveListResponse</a></code>

## Balance

Methods:

- <code title="get /blockchain/balance">client.blockchain.balance.<a href="./src/morpheus_marketplace/resources/blockchain/balance.py">retrieve</a>() -> <a href="./src/morpheus_marketplace/types/balance.py">Balance</a></code>

## Allowance

Types:

```python
from morpheus_marketplace.types.blockchain import AllowanceRetrieveResponse
```

Methods:

- <code title="get /blockchain/allowance">client.blockchain.allowance.<a href="./src/morpheus_marketplace/resources/blockchain/allowance.py">retrieve</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain/allowance_retrieve_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/blockchain/allowance_retrieve_response.py">AllowanceRetrieveResponse</a></code>

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

- <code title="get /blockchain/transactions">client.blockchain.transactions.<a href="./src/morpheus_marketplace/resources/blockchain/transactions.py">list</a>() -> <a href="./src/morpheus_marketplace/types/blockchain/transaction_list.py">TransactionList</a></code>

# BlockchainBids

Methods:

- <code title="post /blockchain/bids">client.blockchain_bids.<a href="./src/morpheus_marketplace/resources/blockchain_bids.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_bid_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>
- <code title="get /blockchain/bids/{id}">client.blockchain_bids.<a href="./src/morpheus_marketplace/resources/blockchain_bids.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/bid.py">Bid</a></code>
- <code title="delete /blockchain/bids/{id}">client.blockchain_bids.<a href="./src/morpheus_marketplace/resources/blockchain_bids.py">delete</a>(id) -> None</code>
- <code title="post /blockchain/bids/{id}/session">client.blockchain_bids.<a href="./src/morpheus_marketplace/resources/blockchain_bids.py">session</a>(id, \*\*<a href="src/morpheus_marketplace/types/blockchain_bid_session_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>

# BlockchainSessions

Methods:

- <code title="post /blockchain/sessions">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">create</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_session_create_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="get /blockchain/sessions/{id}">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">retrieve</a>(id) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="get /blockchain/sessions/budget">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">budget</a>() -> <a href="./src/morpheus_marketplace/types/shared/budget.py">Budget</a></code>
- <code title="post /blockchain/sessions/{id}/close">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">close</a>(id) -> None</code>
- <code title="get /blockchain/sessions/provider">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">provider</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_session_provider_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session_list.py">SessionList</a></code>
- <code title="get /blockchain/sessions/user">client.blockchain_sessions.<a href="./src/morpheus_marketplace/resources/blockchain_sessions.py">user</a>(\*\*<a href="src/morpheus_marketplace/types/blockchain_session_user_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session_list.py">SessionList</a></code>

# Proxy

## Sessions

Types:

```python
from morpheus_marketplace.types.proxy import ClaimableBalance
```

Methods:

- <code title="post /proxy/sessions/initiate">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">initiate</a>(\*\*<a href="src/morpheus_marketplace/types/proxy/session_initiate_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/shared/session.py">Session</a></code>
- <code title="post /proxy/sessions/{id}/providerClaim">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">provider_claim</a>(id, \*\*<a href="src/morpheus_marketplace/types/proxy/session_provider_claim_params.py">params</a>) -> <a href="./src/morpheus_marketplace/types/proxy/claimable_balance.py">ClaimableBalance</a></code>
- <code title="get /proxy/sessions/{id}/providerClaimableBalance">client.proxy.sessions.<a href="./src/morpheus_marketplace/resources/proxy/sessions.py">provider_claimable_balance</a>(id) -> <a href="./src/morpheus_marketplace/types/proxy/claimable_balance.py">ClaimableBalance</a></code>
