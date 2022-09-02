# Soniox Python Client Library

This is a client library for the [Soniox](https://soniox.com/) speech
recognition service. Please see the [tutorials](https://soniox.com/docs).

### Requirements

Python 3.6 or higher.

### Usage

See [soniox_examples/python](https://github.com/soniox/soniox_examples/tree/master/python).

### Development

Create and enter venv:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install packages:

```
python3 -m pip install -U pip
python3 -m pip install -U setuptools wheel
python3 -m pip install -r requirements.txt
```

Build library:

```
python3 -m build
```

Publish to PyPI:

```
python3 -m pip install -U twine
python3 -m twine upload dist/*
```
