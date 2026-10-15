import csv
import sys

def save_theta(path: str, theta0, theta1):
    with open(path, "w") as file:
        file.write(f"{theta0},{theta1}\n")

def load_theta():
    with open("model.csv", "r") as file:
            theta0, theta1 = file.readline().strip().split(",")
            km_min, km_max = file.readline().strip().split(",")
    km_min = float(km_min.split(":")[1].strip())
    km_max = float(km_max.split(":")[1].strip())
    print(km_min, km_max)
    return float(theta0), float(theta1), km_min, km_max

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

def save_normalization(path: str, km_min: float, km_max: float) -> None:
    with open(path, "a", newline="") as file:
        file.write(f"km_min: {km_min}, km_max: {km_max}")
        #writer = csv.writer(file)
        #writer.writerow(km_min: {km_min}, km_max {km_max})