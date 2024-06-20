from google.cloud import bigquery
import pandas as pd


class CSVBigQuery:
    def __init__(self, csv_path: str, table_name: str):
        self.bigquery_client = bigquery.Client()
        self.csv_path = input("Please paste the path to your csv file >> ")
        self.table_name = input("Please provide the destination table path in BigQuery e.g. project.data.table. >>")

    def read_csv(csv_path):
        data_frame = pd.read_csv(csv_path)

        return data_frame

    def return_row_vales(data_frame):

        row_values = []

        for row in data_frame.values:
            this_row = list(row)
            for i in this_row:
                index = this_row.index(i)
                if isinstance(i, str):
                    this_row[index] = "'" + i + "'"
                else:
                    this_row[index] = str(i)
            this_row_string = ', '.join(this_row)
            row_values.append(this_row_string)

        return row_values

    def return_columns_list(data_frame):

        columns = list(data_frame.columns)
        columns_list_string = ', '.join(columns)
        return columns_list_string

    def sql_query(columns_list_string, row_values, table_name):

        values_to_add_string = '(' + '), '.join(row_values) + ')'

        query_sql: str = (
            f"INSERT INTO `{table_name}` ({columns_list_string}) VALUES ({values_to_add_string})"

        )

        return query_sql

    query_job = bigquery_client.query(sql_query().query_SQL)
