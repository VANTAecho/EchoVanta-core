#!/usr/bin/env python3
"""Convert between TimeCoins and several time units."""

import argparse

RATE = 1  # 1 TimeCoin per minute
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_MONTH = 30
DAYS_IN_YEAR = 365


def minutes_to_coins(minutes: float) -> float:
    return minutes / RATE


def seconds_to_coins(seconds: float) -> float:
    return minutes_to_coins(seconds / SECONDS_IN_MINUTE)


def hours_to_coins(hours: float) -> float:
    return minutes_to_coins(hours * MINUTES_IN_HOUR)


def days_to_coins(days: float) -> float:
    return hours_to_coins(days * HOURS_IN_DAY)


def months_to_coins(months: float) -> float:
    return days_to_coins(months * DAYS_IN_MONTH)


def years_to_coins(years: float) -> float:
    return days_to_coins(years * DAYS_IN_YEAR)


def coins_to_minutes(coins: float) -> float:
    return coins * RATE


def coins_to_seconds(coins: float) -> float:
    return coins_to_minutes(coins) * SECONDS_IN_MINUTE


def coins_to_hours(coins: float) -> float:
    return coins_to_minutes(coins) / MINUTES_IN_HOUR


def coins_to_days(coins: float) -> float:
    return coins_to_hours(coins) / HOURS_IN_DAY


def coins_to_months(coins: float) -> float:
    return coins_to_days(coins) / DAYS_IN_MONTH


def coins_to_years(coins: float) -> float:
    return coins_to_days(coins) / DAYS_IN_YEAR


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert between TimeCoins and various time units")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--seconds", type=float, help="Seconds to convert to TimeCoins")
    group.add_argument("--minutes", type=float, help="Minutes to convert to TimeCoins")
    group.add_argument("--hours", type=float, help="Hours to convert to TimeCoins")
    group.add_argument("--days", type=float, help="Days to convert to TimeCoins")
    group.add_argument("--months", type=float, help="Months (30 days) to convert to TimeCoins")
    group.add_argument("--years", type=float, help="Years (365 days) to convert to TimeCoins")
    group.add_argument("--coins", type=float, help="TimeCoins to convert to time")
    parser.add_argument("--to", choices=["seconds", "minutes", "hours", "days", "months", "years"],
                        default="minutes", help="Unit to convert TimeCoins into (default: minutes)")
    args = parser.parse_args()

    if args.seconds is not None:
        coins = seconds_to_coins(args.seconds)
        print(f"{args.seconds} seconds is worth {coins} TimeCoins")
    elif args.minutes is not None:
        coins = minutes_to_coins(args.minutes)
        print(f"{args.minutes} minutes is worth {coins} TimeCoins")
    elif args.hours is not None:
        coins = hours_to_coins(args.hours)
        print(f"{args.hours} hours is worth {coins} TimeCoins")
    elif args.days is not None:
        coins = days_to_coins(args.days)
        print(f"{args.days} days is worth {coins} TimeCoins")
    elif args.months is not None:
        coins = months_to_coins(args.months)
        print(f"{args.months} months is worth {coins} TimeCoins")
    elif args.years is not None:
        coins = years_to_coins(args.years)
        print(f"{args.years} years is worth {coins} TimeCoins")
    else:
        if args.to == "seconds":
            value = coins_to_seconds(args.coins)
            print(f"{args.coins} TimeCoins equals {value} seconds")
        elif args.to == "minutes":
            value = coins_to_minutes(args.coins)
            print(f"{args.coins} TimeCoins equals {value} minutes")
        elif args.to == "hours":
            value = coins_to_hours(args.coins)
            print(f"{args.coins} TimeCoins equals {value} hours")
        elif args.to == "days":
            value = coins_to_days(args.coins)
            print(f"{args.coins} TimeCoins equals {value} days")
        elif args.to == "months":
            value = coins_to_months(args.coins)
            print(f"{args.coins} TimeCoins equals {value} months")
        elif args.to == "years":
            value = coins_to_years(args.coins)
            print(f"{args.coins} TimeCoins equals {value} years")


if __name__ == "__main__":
    main()
