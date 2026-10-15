def ft_min(values: list[int]) -> float:
    if not values:
        return float('nan')
    min_value = float('inf')
    for v in values:
        if v < min_value:
            min_value = v
    return min_value

def ft_max(values: list[int]) -> float:
    if not values:
        return float('nan')
    max_value = float('-inf')
    for v in values:
        if v > max_value:
            max_value = v
    return max_value
