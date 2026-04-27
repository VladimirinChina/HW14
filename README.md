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

## New Functionality

In this stage, the project was extended using object-oriented programming principles, particularly inheritance and type validation.

1. Added Product Subclasses

Two new classes were implemented:

- Smartphone
- LawnGrass

Both classes inherit from the base Product class and extend it with additional attributes:

Smartphone:

- efficiency — performance
- model — model
- memory — memory
- color — color

LawnGrass:

- country — country of origin
- germination_period — germination period
- color — color

This approach avoids code duplication and keeps shared logic within the base Product class.

2. Restricted Product Addition Operation

The __add__ method in the Product class was updated:

- Products can now be added only if they belong to the same class
- Attempting to add different product types (e.g., Smartphone and LawnGrass) raises a TypeError

This ensures correct and predictable behavior when calculating total value.

3. Safe Product Addition to Category

The add_product method in the Category class was improved:

- Only instances of Product or its subclasses can be added
- Passing any other type raises a TypeError

Type checking is implemented using isinstance, preventing invalid objects from being added to categories.

4. Testing

Tests were added and updated using pytest:

- Validation of new subclasses
- Verification of correct product addition behavior
- Ensuring TypeError is raised for invalid operations
- Validation of protected category addition logic

All previously implemented tests pass successfully, ensuring backward compatibility.

## Latest Updates
- Abstract Logic: Implemented BaseProduct abstract base class to enforce core product structure using abc.

- Logging Mixin: Integrated PrintMixin to automatically log object creation details via __repr__.

- Order System: Added Order class with a shared abstract root for both Order and Category.

- Testing: Achieved >75% test coverage for new functionality using pytest.