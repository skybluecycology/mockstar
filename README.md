# Mock Data Generator

## Requirement

This library generates mock data for fact and dimension tables based on metadata. Allow for list override for the eval/lambda functions in the meta data.

mock_data_generator/
│
├── mock_data_generator/
│   ├── __init__.py
│   ├── generator.py
│
├── setup.py
├── README.md
└── metadata.json

## Installation

```bash
pip install .

```

## Usage

```python
from mock_data_generator import MockDataGenerator

# Initialize the generator with a metadata file
generator = MockDataGenerator('metadata.json')

# Generate all tables
tables = generator.generate_all_tables()

# Access individual tables
customers = tables['customers']
products = tables['products']
dates = tables['dates']
fact_table = tables['fact']

# Example of joining tables
fact_with_customers = fact_table.merge(customers, on='CustomerID')
fact_with_full_data = fact_with_customers.merge(products, on='ProductID').merge(dates, on='DateKey')

print(fact_with_full_data.head())
```

## Explanation
Package Structure: The code is organized into a package with a module for generating mock data.

Metadata Handling: The MockDataGenerator class reads metadata from a JSON file and uses it to generate tables.

Installation and Usage: The setup.py file allows you to install the package, and the README.md file provides usage instructions.

This setup allows you to share the library easily and use it in different projects by simply importing the MockDataGenerator class and providing a metadata file.
