from helper.read_data import load_theta
import logging
import sys

def predict():

    try:
        mileage = int(input("Mileage: "))
    except ValueError:
        logging.critical("Please enter a valid mileage")
        sys.exit(1)

    try:
        theta0, theta1 = load_theta()
    except FileNotFoundError:
        theta0 = 0
        theta1 = 0
    except (ValueError, UnboundLocalError):
        logging.critical("Invalide data in model.csv")
        sys.exit(1)
    
    estimatePrice = theta0 + (theta1 * mileage)    
    print("Estimated price: ", estimatePrice)

if __name__ == "__main__":
    predict()