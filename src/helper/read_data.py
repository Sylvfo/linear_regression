import csv
import sys

def save_theta(theta0, theta1):
    with open("model.csv", "w") as file:
        file.write(f"{theta0},{theta1}\n")


def load_theta():

    with open("model.csv", "r") as file:
            theta0, theta1 = file.readline().strip().split(",")
    return float(theta0), float(theta1)