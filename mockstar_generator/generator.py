import pandas as pd
import numpy as np
import json

class MockDataGenerator:
    def __init__(self, metadata_file):
        # Load metadata from JSON file
        with open(metadata_file, 'r') as f:
            self.metadata = json.load(f)

    def generate_table(self, table_name):
        meta = self.metadata[table_name]
        num_records = meta['num_records']
        columns = {}
        for col_name, col_expr in meta['columns'].items():
            if isinstance(col_expr, list):
                # Handle list of values directly
                columns[col_name] = np.random.choice(col_expr, size=num_records)
            else:
                # Evaluate the expression for generating data
                columns[col_name] = eval(col_expr)
                columns[col_name] = exec(col_expr)
        return pd.DataFrame(columns)

    def generate_all_tables(self):
        tables = {}
        for table_name in self.metadata:
            tables[table_name] = self.generate_table(table_name)
        return tables
