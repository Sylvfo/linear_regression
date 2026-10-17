#!/usr/bin/env python3
from helper.min_max import ft_min, ft_max


def normalized_km_train(km: list[int]) -> tuple[list[float], float, float]:
    min_km = ft_min(km)
    max_km = ft_max(km)
    # handle errors
    if min_km == max_km:
        raise ValueError("all km values are identical")
    norm_km = [(x - min_km) / (max_km - min_km) for x in km]
    return norm_km, min_km, max_km


def normalized_km_predict(km: float, min_km, max_km) -> float:
    # handle errors
    if min_km == max_km:
        raise ValueError("all km values are identical")
    norm_km = (km - min_km) / (max_km - min_km)
    return norm_km
