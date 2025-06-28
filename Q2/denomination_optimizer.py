from typing import List, Tuple, Dict
import itertools

def min_coins_needed(amount: int, denominations: List[int]) -> int:
    if amount == 0:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else float('inf')

def calculate_average_units(denominations: List[int], max_value: int) -> float:
    total_units = 0
    for value in range(1, max_value + 1):
        units_needed = min_coins_needed(value, denominations)
        if units_needed == float('inf'):
            return float('inf')
        total_units += units_needed
    return total_units / max_value

def get_coin_breakdown(amount: int, denominations: List[int]) -> Dict[int, int]:
    if amount == 0:
        return {}
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and dp[i - coin] != float('inf'):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    parent[i] = coin
    if dp[amount] == float('inf'):
        return {}
    result = {}
    current = amount
    while current > 0:
        coin = parent[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin
    return result

def generate_smart_candidates(unit_count: int, max_value: int) -> List[List[int]]:
    candidates = []
    if unit_count >= 1:
        powers_of_2 = []
        power = 1
        while len(powers_of_2) < unit_count and power <= max_value:
            powers_of_2.append(power)
            power *= 2
        if len(powers_of_2) == unit_count:
            candidates.append(powers_of_2)

        if unit_count >= 2:
            powers_of_3 = [1]
            power = 3
            while len(powers_of_3) < unit_count and power <= max_value:
                powers_of_3.append(power)
                power *= 3
            if len(powers_of_3) == unit_count:
                candidates.append(powers_of_3)

        if unit_count >= 3:
            fib = [1, 2]
            while len(fib) < unit_count:
                next_val = fib[-1] + fib[-2]
                if next_val > max_value:
                    break
                fib.append(next_val)
            if len(fib) == unit_count:
                candidates.append(fib)

        common_patterns = [
            [1, 2, 5, 10, 20, 50],
            [1, 2, 5, 10, 25, 50],
            [1, 3, 5, 15, 25, 50],
            [1, 2, 3, 6, 12, 24],
            [1, 2, 6, 12, 30, 60],
            [1, 3, 9, 27, 81],
            [1, 4, 16, 64],
            [1, 5, 25],
            [1, 2, 4, 10, 25],
            [1, 3, 7, 21],
            [1, 2, 3, 7, 14]
        ]

        for pattern in common_patterns:
            if len(pattern) == unit_count and all(x <= max_value for x in pattern):
                candidates.append(pattern)

    unique_candidates = []
    for cand in candidates:
        if cand not in unique_candidates:
            unique_candidates.append(cand)
    return unique_candidates

def find_optimal_denominations_fast(unit_count: int, max_value: int) -> Tuple[List[int], float]:
    candidates = generate_smart_candidates(unit_count, max_value)
    if unit_count <= 3 and max_value <= 20:
        for combo in itertools.combinations(range(1, max_value + 1), unit_count):
            candidates.append(list(combo))
    elif unit_count <= 4 and max_value <= 50:
        bases = [2, 3, 5]
        for base in bases:
            pattern = []
            power = 1
            while len(pattern) < unit_count and power <= max_value:
                pattern.append(power)
                power *= base
            if len(pattern) == unit_count:
                candidates.append(pattern)
                for i in range(len(pattern)):
                    for delta in [-1, 1, 2, -2]:
                        variant = pattern.copy()
                        new_val = variant[i] + delta
                        if new_val > 0 and new_val <= max_value and new_val not in variant:
                            variant[i] = new_val
                            variant.sort()
                            if variant not in candidates:
                                candidates.append(variant)

    best_avg = float('inf')
    best_denominations = None
    for denominations in candidates:
        if len(denominations) == unit_count:
            avg_units = calculate_average_units(denominations, max_value)
            if avg_units < best_avg:
                best_avg = avg_units
                best_denominations = denominations
    return best_denominations, best_avg
