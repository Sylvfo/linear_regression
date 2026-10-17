# ft_linear_regression

Predict the price of a car from its mileage, using a linear regression trained with gradient descent.

```
estimatePrice(mileage) = θ0 + θ1 * mileage
```

## Install

Requires Python 3.

```sh
make install
```

This creates a virtual environment in `venv/` and installs the dependencies from `requirements.txt`. You don't need to activate it: the Makefile calls `venv/bin/python3` directly.

## Usage

### 1. Train the model

```sh
make train
```

Reads `src/data/data.csv`, runs gradient descent and saves the result to `model.csv`:

```
7990.75686379576,-4609.917007825483
km_min: 22899, km_max: 240000
```

- line 1: `θ0,θ1`
- line 2: min and max mileage of the dataset, used for normalization

### 2. Predict a price

```sh
make predict
```

```
Mileage: 67000
Estimated price: 7054
```

If `model.csv` doesn't exist yet, θ0 and θ1 are set to 0, so the prediction is 0.

## How it works

### 1. The model

The price is modelled as a straight line:

```
estimatePrice(km) = θ0 + θ1 * km
```

- `θ0`: the price of a car with 0 km (intercept)
- `θ1`: how much the price changes per km (slope, negative here)

Training means finding the θ0 and θ1 that make the line fit the data as closely as possible.

### 2. The cost: how wrong is the line?

The error is measured with the **mean squared error** over the `m` cars of the dataset:

```
cost = (1/m) * Σ (estimatePrice(km[i]) - price[i])²
```

The smaller the cost, the better the line. Squaring makes every error positive and punishes big errors more.

### 3. Normalization

Mileages go up to 240 000, while prices are around 5 000. With such different scales, the gradient for θ1 is huge and the descent diverges unless the learning rate is tiny (and training very slow).

So mileages are first scaled between 0 and 1:

```
km_norm = (km - km_min) / (km_max - km_min)
```

`km_min` and `km_max` are saved in `model.csv`, because `predict` must normalize the user's mileage **the same way** before using θ0 and θ1.

### 4. Gradient descent

θ0 and θ1 start at 0. At each epoch, we compute in which direction the cost goes down, and take a small step that way:

```
tmpθ0 = learningRate * (1/m) * Σ (estimatePrice(km[i]) - price[i])
tmpθ1 = learningRate * (1/m) * Σ (estimatePrice(km[i]) - price[i]) * km[i]

θ0 = θ0 - tmpθ0
θ1 = θ1 - tmpθ1
```

Both θ are updated **at the same time**, from the values of the previous epoch.

| Parameter | Value |
|---|---|
| learning rate | 0.05 |
| epochs | 2000 |

The cost curve (`plots/training_cost.png`) shows the descent: it drops fast, then flattens out when θ0 and θ1 stop changing.

### 5. Prediction

`predict` reads θ0, θ1, `km_min` and `km_max` from `model.csv`, normalizes the mileage entered by the user, and applies the formula.

## Bonus

Graphs are saved in `plots/`:

| File | Content |
|---|---|
| `price_vs_mileage.png` | the dataset (price vs mileage) |
| `regression_line.png` | the dataset with the regression line |
| `training_cost.png` | the cost (mean squared error) at each epoch |

## Makefile

| Rule | Action |
|---|---|
| `make install` | create the venv and install the dependencies |
| `make train` | train the model |
| `make predict` | predict a price |
| `make` | train, then predict |
| `make flake` | check the code style with flake8 |
| `make fclean` | remove `model.csv` and `plots/` |
| `make re` | `fclean` + `make` |

## Project structure

```
src/
├── train/train.py        # gradient descent
├── predict/predict.py    # price prediction
├── helper/               # read/save data, normalization, min/max
├── bonus/graphs.py       # plots
└── data/data.csv         # dataset
```


