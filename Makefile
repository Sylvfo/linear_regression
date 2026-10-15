DATA_SET = src/data/data.csv

PYTHON = PYTHONPATH=src venv/bin/python3
PIP = venv/bin/pip
FLAKE = venv/bin/flake8

all: train predict 

install:
	python3 -m venv venv
	$(PIP) install -r requirements.txt

train:
	$(PYTHON) src/train/train.py $(DATA_SET)

predict:
	$(PYTHON) src/predict/predict.py

flake:
	$(FLAKE) src

fclean:
	rm -f model.csv
	rm -rf plots

re: fclean all

.PHONY: all install train predict flake fclean re
