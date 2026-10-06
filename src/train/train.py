#!/usr/bin/env python3
import sys
import logging
from helper.read_data import read_data
from helper.read_data import save_theta
from bonus.graphs import show_data_distribution
from bonus.graphs import show_data_line
from bonus.graphs import show_cost
import matplotlib.pyplot as graph
import numpy as np
import math
from helper.min_max import ft_min, ft_max

EPOCH = 1000
LEARNING_RATE = 0.005

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

    theta0 = 0 # bias 
    theta1 = 0 # weights

    nb_data = len(price)
    print(nb_data)
    #error management!!
    if nb_data == 0:
        return
    
    norm_km = normalized_km(km)

    history_cost = []
    history_iterations = []
    for n in range(EPOCH):
        gradient0,gradient1 = gradient_function(norm_km, price, theta0, theta1)
        
        #update thetas
        theta0 -= LEARNING_RATE * gradient0
        theta1 -= LEARNING_RATE * gradient1

        #bonus
        cost = cost_function(norm_km, price, theta0, theta1)
        print(f"error_cost1 {cost}\n")
        history_cost.append(cost)
        history_iterations.append(n)

    show_cost(history_iterations, history_cost)
    return theta0, theta1

def estim_price(km, theta0, theta1) -> float:
    return theta0 +(theta1 * km)

def gradient_function(km, price, theta0, theta1) -> tuple [float, float]:
    gradient0 = 0
    gradient1 = 0
    nb_data = len(price)
    for i in range(nb_data):
        estimate_price = estim_price(km[i], theta0, theta1)
        gradient0 += estimate_price - price[i]
        gradient1 += (estimate_price - price[i]) * km[i]
    gradient0 /= nb_data
    gradient1 /= nb_data
    return gradient0, gradient1

def normalized_km(km: list[int]) -> list[float]:
    min_km = ft_min(km)
    max_km = ft_max(km)
    print(f"min {min_km} max {max_km}")
    #handle errors
    if min_km == max_km:
        return
    norm_km = [(x - min_km) / (max_km - min_km) for x in km]
    return norm_km

#bonus
def cost_function(km, price, theta0, theta1):
    cost = 0
    nb_data = len(price)
    for i in range(nb_data):
        estimate_price = estim_price(km[i], theta0, theta1)
        #cost += math.sqrt(estimate_price - price[i])
        cost += (estimate_price - price[i]) ** 2
    return cost/ nb_data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.critical("Miss data set")
        sys.exit(1)

    train(sys.argv[1])


    """
    1 predict result
    2 calculate error
    3 gradient
    4repeat n time


def update_thetas(error_cost0, error_cost1) -> tuple[float, float]:
    theta0 -= LEARNING_RATE * error_cost0
    theta1 -= LEARNING_RATE * error_cost1
    return theta0, theta1


def gradient_function0(km, price, theta0, theta1) -> float:
    error_cost = 0
    nb_data = len(price)
    for i in range(nb_data):
        error_cost += estim_price(km[i], theta0, theta1) - price[i]
    error_cost /= nb_data
    print (error_cost)
    return error_cost

def gradient_function1(km, price, theta0, theta1) -> float:
    error_cost = 0
    nb_data = len(price)
    for i in range(nb_data):
        error_cost += (estim_price(km[i], theta0, theta1) - price[i]) * km[i]
    error_cost /= nb_data
    return error_cost 


        """