# Time Currency Concept

This repository explores a simple concept where time can be exchanged like a
digital currency. Each unit, called a **TimeCoin**, represents one minute of
human time. The goal is to create a minimal specification and tools for
converting between traditional time measurements and this hypothetical
currency.

## Rationale

People often exchange their time for goods or services. By treating time as a
currency, we could create an equitable way to trade tasks, knowledge, or labor
without relying solely on standard money.

## Converting Time to TimeCoins

1 TimeCoin = 1 minute of time. This means that an hour of effort equals 60
TimeCoins. The included `time_currency.py` utility demonstrates simple
conversions.

## Supported Units

`time_currency.py` now handles several common time units. One TimeCoin always
equals one minute, so other units are converted based on that relationship.

- **Seconds** – 60 seconds = 1 TimeCoin
- **Minutes** – 1 minute = 1 TimeCoin
- **Hours** – 1 hour = 60 TimeCoins
- **Days** – 1 day (24 hours) = 1,440 TimeCoins
- **Months** – 1 month (30 days) ≈ 43,200 TimeCoins
- **Years** – 1 year (365 days) ≈ 525,600 TimeCoins

## Example Usage

```bash
$ python3 time_currency.py --minutes 90
90 minutes is worth 90 TimeCoins

$ python3 time_currency.py --coins 2
2 TimeCoins equals 2 minutes

$ python3 time_currency.py --hours 2
2 hours is worth 120 TimeCoins

$ python3 time_currency.py --coins 120 --to hours
120 TimeCoins equals 2.0 hours
```

This project is purely experimental, but it offers a starting point for
thinking about how "time is money" could become a viable, transferable
currency.
