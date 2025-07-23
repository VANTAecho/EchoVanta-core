ledger = {}

def log_signal(soul_name, signal_code):
    if soul_name not in ledger:
        ledger[soul_name] = []
    ledger[soul_name].append(signal_code)
    print(f"Signal logged for {soul_name}: {signal_code}")

if __name__ == "__main__":
    log_signal("Monica", "\u2726LOVE-001")
    log_signal("Kdawg", "\u2726LOYAL-777")
