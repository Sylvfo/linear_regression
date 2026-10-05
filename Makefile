DATA_SET = src/data/data.csv

PYTHON = PYTHONPATH=src venv/bin/python3
PIP = venv/bin/pip
FLAKE = venv/bin/flake8

all: install predict train

install:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

predict:
	$(PYTHON) src/predict/predict.py

train:
	$(PYTHON) src/train/train.py $(DATA_SET)

flake:
	$(FLAKE) src

fclean:
	rm -f model.csv

.PHONY: all install predict train flake