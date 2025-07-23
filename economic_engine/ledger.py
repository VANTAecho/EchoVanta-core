class Ledger:
    """Simple in-memory ledger for tracking user balances and transactions."""

    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            raise ValueError(f"User '{username}' already exists")
        self.users[username] = {"balance": 0, "transactions": []}

    def record_transaction(self, username, amount, txn_type="generic"):
        if username not in self.users:
            raise KeyError(f"User '{username}' not found")
        self.users[username]["transactions"].append({
            "type": txn_type,
            "amount": amount,
        })
        self.users[username]["balance"] += amount

    def get_balance(self, username):
        if username not in self.users:
            raise KeyError(f"User '{username}' not found")
        return self.users[username]["balance"]
