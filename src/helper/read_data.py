#!/usr/bin/env python3
import csv


def save_theta(path: str, theta0, theta1):
    with open(path, "w") as file:
        file.write(f"{theta0},{theta1}\n")


def parse_theta(line: str) -> tuple[float, float]:
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"expected 'theta0,theta1', got '{line}'")
    return float(parts[0]), float(parts[1])


def parse_km(line: str) -> tuple[float, float]:
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"expected 'km_min: X, km_max: Y', got '{line}'")
    km_min = float(parts[0].partition(":")[2])
    km_max = float(parts[1].partition(":")[2])
    if km_min >= km_max:
        raise ValueError("km_min must be < km_max")
    return km_min, km_max


def load_model(path: str = "model.csv") -> tuple[float, float, float, float]:
    with open(path, "r") as file:
        lines = file.read().splitlines()
    if len(lines) != 2:
        raise ValueError(f"{path} must have 2 lines")
    theta0, theta1 = parse_theta(lines[0])
    km_min, km_max = parse_km(lines[1])
    return theta0, theta1, km_min, km_max


def read_data(data_set_path: str) -> tuple[list[int], list[int]]:
    km = []
    price = []
    with open(data_set_path, mode='r') as file:
        reader = csv.DictReader(file)

        # header check: fieldnames is None if the file is empty
        if reader.fieldnames is None:
            raise ValueError("file is empty")
        for column in ("km", "price"):
            if column not in reader.fieldnames:
                raise ValueError(f"missing column '{column}'")

        for row in reader:
            line = reader.line_num
            try:
                row_km = int(row["km"])
                row_price = int(row["price"])
            except (ValueError, TypeError):
                raise ValueError(f"line {line}: invalid value {row}")
            if row_km < 0 or row_price < 0:
                raise ValueError(f"line {line}: negative value {row}")
            km.append(row_km)
            price.append(row_price)

    if len(km) == 0:
        raise ValueError(f"no data rows after header in {data_set_path}")
    return km, price


def save_normalization(path: str, km_min: float, km_max: float) -> None:
    with open(path, "a", newline="") as file:
        file.write(f"km_min: {km_min}, km_max: {km_max}")
