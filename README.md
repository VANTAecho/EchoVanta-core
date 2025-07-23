# EchoVanta Core

This repository contains a minimal implementation of the `Ledger` class
used to track user balances and record transactions.

## Usage Example

```python
from economic_engine.ledger import Ledger

ledger = Ledger()
ledger.add_user("Vanta")
ledger.record_transaction("Vanta", amount=1000000, txn_type="divine deposit")
print(ledger.get_balance("Vanta"))  # -> 1000000
```
