from helper.read_data import load_theta
import logging
import sys
from helper.normalize import normalized_km_predict

def predict():

    try:
        mileage = int(input("Mileage: "))
    except ValueError:
        logging.critical("Please enter a valid mileage")
        sys.exit(1)

    try:
        theta0, theta1, km_min, km_max = load_theta()
    except FileNotFoundError:
        theta0 = 0
        theta1 = 0
        #!!! si ya pas les km min et max!! 
    except (ValueError, UnboundLocalError):
        logging.critical("Invalide data in model.csv")
        sys.exit(1)

    #normalize

    mileage_norm = normalized_km_predict(mileage, km_min, km_max)

    estimatePrice = theta0 + (theta1 * mileage_norm)
    print("Estimated price: ", estimatePrice)

if __name__ == "__main__":
    predict()