import csv
import sys

def save_theta(theta0, theta1):
    with open("model.csv", "w") as file:
        file.write(f"{theta0},{theta1}\n")


def load_theta():

    with open("model.csv", "r") as file:
            theta0, theta1 = file.readline().strip().split(",")
    return float(theta0), float(theta1)

def read_data(data_set_path: str) -> tuple[list[int], list[int]]:
    km = []
    price = [] 
    with open(data_set_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #for name in fields:
            km.append(int(row["km"]))
            price.append(int(row["price"]))
    
    return km, price