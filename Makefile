DATA_SET = src/data/data.csv

PYTHON = PYTHONPATH=src .venv/bin/python3
PIP = .venv/bin/pip
FLAKE = .venv/bin/flake8

all: predict train

predict:
	$(PYTHON) src/predict/predict.py

train:
	$(PYTHON) src/train/train.py

flake:
	$(FLAKE) src

fclean:
	rm -f model.csv
	
.PHONY: all predict train flake