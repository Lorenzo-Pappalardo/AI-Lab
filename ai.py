import pandas
from pandas.core.frame import DataFrame


def read_csv() -> DataFrame:
    return pandas.read_csv('chicago_taxi_trips_2016_12.csv',
                           parse_dates=True,
                           infer_datetime_format=True)


def main() -> None:
    df = read_csv()
    total_rows = len(df)

    missing_values = []
    for row in df.columns:
        null_rows = df[row].isnull().sum()
        missing_values.append((null_rows/total_rows)*100)

    cardinality = df.nunique()

    max = df.max()
    min = df.min()

    first_quantile = df.quantile(.25)
    third_quantile = df.quantile(.75)

    mean = df.mean()
    median = df.median()
    standard_deviation = df.std()


if (__name__ == '__main__'):
    main()
