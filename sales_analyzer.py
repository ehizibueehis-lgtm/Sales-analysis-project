import pandas as pd
import os


class SalesAnalyzer:
    def __init__(self, file_path):
        #Initializes the analyzer with the raw dataset path.#
        self.file_path = file_path
        self.df = None

    def load_data(self):
        #Loads the dataset into a Pandas DataFrame.#
        self.df = pd.read_csv(self.file_path)
        print(f"Data loaded successfully. {len(self.df)} rows found.")
        return self.df

    def clean_data(self):
        """Executes all data cleaning and transformation steps."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # 1. Drop exact duplicates
        self.df.drop_duplicates(inplace=True)

        # 2. Clean and convert numeric/date columns
        self.df['qty'] = self.df['qty'].astype(str).str.replace('pcs', '')
        self.df['qty'] = pd.to_numeric(self.df['qty'], errors='coerce')
        self.df['price'] = pd.to_numeric(self.df['price'], errors='coerce')
        self.df['order_date'] = pd.to_datetime(self.df['order_date'], errors='coerce')

        # 3. Create derived column
        self.df['total_sales'] = self.df['qty'] * self.df['price']

        # 4. Standardize inconsistent categorical text
        self.df['payment_method'] = self.df['payment_method'].str.strip().str.title()
        self.df['payment_method'] = self.df['payment_method'].replace({'Bank Transfer': 'Transfer', 'Pos': 'POS'})

        self.df['status'] = self.df['status'].str.strip().str.title()
        self.df['status'] = self.df['status'].replace({'Complete': 'Completed', 'Return': 'Returned'})

        # 5. Handle missing values using the hybrid approach
        categorical_cols = ['product', 'region', 'customer_id', 'payment_method', 'status']
        self.df[categorical_cols] = self.df[categorical_cols].fillna('Unknown')
        self.df.dropna(subset=['order_date', 'qty', 'price'], inplace=True)

        print(f"Data cleaned. {len(self.df)} valid records remain.")
        return self.df

    def generate_summary(self):
        #Generates a high-level business summary.#
        if self.df is None:
            return "No data available."

        return {
            'Total Revenue': self.df['total_sales'].sum(),
            'Total Orders': len(self.df),
            'Average Order Value': self.df['total_sales'].mean()
        }

    def save_cleaned_data(self, output_dir='data', filename='cleaned_sales_data.csv'):
        #Saves the fully processed DataFrame to a CSV.#
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, filename)
        self.df.to_csv(file_path, index=False)
        print(f"Cleaned dataset saved to {file_path}")
