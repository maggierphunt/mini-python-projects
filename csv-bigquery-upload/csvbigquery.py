from google.cloud import bigquery
import pandas as pd


class CSVBigQuery:
    def __init__(self, csv_path: str, table_name: str):
        self.bigquery_client = bigquery.Client()
        self.csv_path = csv_path
        self.table_name = table_name

    @staticmethod
    def read_csv(csv_path: str) -> pd.DataFrame:
        try:
            data_frame = pd.read_csv(csv_path)

            return data_frame
        except Exception as e:
            raise RuntimeError(f'Error reading file - {e}')

    @staticmethod
    def format_row_vales(data_frame: pd.DataFrame) -> list:

        row_values = []

        for row in data_frame.values:
            this_row = list(row)
            for i in this_row:
                index = this_row.index(i)
                if isinstance(i, str):
                    this_row[index] = f"'{i}'"
                else:
                    this_row[index] = str(i)
            this_row_string = ', '.join(this_row)
            row_values.append(this_row_string)

        return row_values

    @staticmethod
    def return_columns_list(data_frame: pd.DataFrame) -> str:

        columns = list(data_frame.columns)
        columns_list_string = ', '.join(columns)
        return columns_list_string

    @staticmethod
    def create_sql_query(self, columns_list: str, row_values: list) -> str:

        values_to_add_string = '(' + '), '.join(row_values) + ')'

        query_sql: str = (
            f"INSERT INTO `{self.table_name}` ({self.columns_list_string}) VALUES ({values_to_add_string})"

        )

        return query_sql

    def execute_query(self, query: str):
        try:
            query_job = self.bigquery_client.query(self.create_sql_query().query_SQL)
            query_job.result()
            print(f"Data from CSV uploaded to Bigquery table {self.table_name}")
        except Exception as e:
            raise RuntimeError(f"Error uploading to Bigquery table {self.table_name} - {e}")

    def csv_to_bigquery(self):
        data_frame = self.read_csv(self.csv_path)
        columns_list = self.return_columns_list(data_frame)
        row_values = self.format_row_vales(data_frame)
        query = self.create_sql_query(columns_list, row_values)
        self.execute_query(query)


csv_path = input("Please paste the path to your csv file >> ")
table_name = input("Please provide the destination table path in BigQuery e.g. project.data.table. >>")
csv_bigquery = CSVBigQuery(csv_path, table_name)
csv_bigquery.load_csv_to_bigquery()
