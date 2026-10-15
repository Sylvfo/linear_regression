from helper.min_max import ft_min, ft_max
import csv

def normalized_km_train(km: list[int]) -> tuple[list[float], float, float]:
    min_km = ft_min(km)
    max_km = ft_max(km)
    print(f"min {min_km} max {max_km}")
    #handle errors
    if min_km == max_km:
        #raise ValueError("Cannot normalize: min_km == max_km")
        return
    norm_km = [(x - min_km) / (max_km - min_km) for x in km]
    return norm_km, min_km, max_km

def normalized_km_predict(km:float, min_km, max_km) -> float:
    print(f"min {min_km} max {max_km}")
    #handle errors
    if min_km == max_km:
        #raise ValueError("Cannot normalize: min_km == max_km")
        return
    norm_km = (km - min_km) / (max_km - min_km)
    return norm_km


"""
def rescale_km(km: list[float], km_min :float, km_max: float) -> list[float]:
    rescaled_km = [x * (km_max - km_min) + km_min for x in km]
    return rescaled_km
"""
