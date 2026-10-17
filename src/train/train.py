#!/usr/bin/env python3
import sys
import logging
from helper.read_data import read_data, save_normalization, save_theta
from bonus.graphs import show_data_distribution, show_data_line, show_cost
from helper.normalize import normalized_km_train


EPOCH = 2000
LEARNING_RATE = 0.05


def train(data_set_path: str):
    try:
        km, price = read_data(data_set_path)
        norm_km, km_min, km_max = normalized_km_train(km)
    except IOError as ioe:
        logging.critical(f"Error opening file: {ioe}")
        sys.exit(1)
    except ValueError as e:
        logging.critical(f"invalid dataset: {e}")
        sys.exit(1)

    show_data_distribution(norm_km, price)
    theta0, theta1 = linear_regression(norm_km, price)
    show_data_line(norm_km, price, theta0, theta1)

    try:
        save_theta("model.csv", theta0, theta1)
        save_normalization("model.csv", km_min, km_max)
    except OSError:
        logging.critical("impossible to save model.csv: {e}")
        sys.exit(1)


def linear_regression(km: list[int], price: list[int]) -> tuple[float, float]:

    theta0 = 0  # bias
    theta1 = 0  # weights

    history_cost = []
    history_iterations = []
    for n in range(EPOCH):
        gradient0, gradient1 = gradient_function(km, price, theta0, theta1)

        # update thetas
        theta0 -= LEARNING_RATE * gradient0
        theta1 -= LEARNING_RATE * gradient1

        # bonus
        cost = cost_function(km, price, theta0, theta1)
        # print(f"error_cost1 {cost}\n")
        history_cost.append(cost)
        history_iterations.append(n)

    show_cost(history_iterations, history_cost)
    return theta0, theta1


def estim_price(km, theta0, theta1) -> float:
    return theta0 + (theta1 * km)


def gradient_function(km, price, theta0, theta1) -> tuple[float, float]:
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


# bonus
def cost_function(km, price, theta0, theta1):
    cost = 0
    nb_data = len(price)
    for i in range(nb_data):
        estimate_price = estim_price(km[i], theta0, theta1)
        cost += (estimate_price - price[i]) ** 2
    return cost / nb_data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.critical("usage: train.py <dataset.csv>")
        sys.exit(1)

    train(sys.argv[1])
