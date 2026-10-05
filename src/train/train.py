#!/usr/bin/env python3
import sys
import logging
from helper.read_data import read_data
from helper.read_data import save_theta
from bonus.graphs import show_data_distribution
from bonus.graphs import show_data_line
import matplotlib.pyplot as graph

def train(data_set_path: str):
    print("hey you let's train")
    try:
        km, price = read_data(data_set_path)
    except IOError as ioe:
        logging.critical(f"Error opening file: {ioe}")
        sys.exit(1)
    except ValueError as val:
        logging.critical(f"invalid literal for int() in data.csv")
        sys.exit(1)
    except TypeError as ty:
        logging.critical("not same number of inputs for km and price in data.csv")
        sys.exit(1)

    # not necessary?
    if len(km) != len(price):
        logging.critical("not same number of inputs for km and price in data.csv")
        sys.exit(1)

    show_data_distribution(km, price)
    theta0, theta1 = linear_regression(km, price)
    show_data_line(km, price, theta0, theta1)
    try:
        save_theta(theta0, theta1)
    except:
        logging.critical("impossible to save model.csv")
        sys.exit(1)

def linear_regression(km: list[int], price: list[int]) -> tuple[float, float] :

    #iciiiiiiiiiii :)
    tmp_theta0 = 3
    tmp_theta1 = 1
    print(km)
    print(price)


    #loss_function
    #gradient

    #update theta0 and 1
    theta0 = 100
    theta1 = 2
    return theta0, theta1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.critical("Miss data set")
        sys.exit(1)

    train(sys.argv[1])