#!/usr/bin/env python3
from helper.read_data import load_model
import logging
import sys
from helper.normalize import normalized_km_predict


def predict():
    try:
        mileage = int(input("Mileage: "))
        if mileage < 0:
            raise ValueError("mileage cannot be negative")
    except ValueError as e:
        logging.critical(f"invalid mileage: {e}")
        sys.exit(1)

    try:
        theta0, theta1, km_min, km_max = load_model()
    except FileNotFoundError:
        theta0 = 0
        theta1 = 0
        km_min = 0
        km_max = 1
        logging.warning("model.csv not found, using theta0 = 0 and theta1 = 0")
    except ValueError as e:
        logging.critical(f"invalid model: {e}")
        sys.exit(1)    

    mileage_norm = normalized_km_predict(mileage, km_min, km_max)
    estimatePrice = theta0 + (theta1 * mileage_norm)
    print("Estimated price:", estimatePrice)


if __name__ == "__main__":
    predict()
