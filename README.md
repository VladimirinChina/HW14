# E-commerce Core Engine

A Python-based backend core for an e-commerce system, managing product catalogs and categories with automated tracking.
Implemented Product and Category models with encapsulation, product management, and JSON data loading.

## Features
- **OOP Architecture**: Robust `Product` and `Category` classes.
- **Auto-tracking**: Dynamic counting of total categories and unique products.
- **Data Loading**: Import catalog data directly from JSON files.
- **Quality Control**: Fully typed with `mypy`, styled with `flake8`, and sorted with `isort`.

## Tech Stack
- **Language**: Python 3.13+
- **Dependency Management**: [Poetry](https://python-poetry.org/)
- **Testing**: [Pytest](https://docs.pytest.org/) (95% coverage)

## Installation
```bash
git clone <your-repo-link>
cd <repo-name>
poetry install
```

## Usage

To run the main demonstration:
```bash
poetry run python main.py
```

## Development & Testing

Run tests:
```bash
poetry run pytest
```
Run linters:
```bash
# Style check
poetry run flake8 .
# Type check
poetry run mypy .
# Import sorting
poetry run isort .
```
