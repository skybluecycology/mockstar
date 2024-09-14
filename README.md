# Mock Data Generator

This library generates mock data for fact and dimension tables based on metadata.

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
'''python
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
