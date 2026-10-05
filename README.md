python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/main.py

source .venv/bin/activate

## Install

```sh
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

The `Makefile` calls `venv/bin/python3` directly, so activating the venv is only
needed when running things by hand:

```sh
source venv/bin/activate
```