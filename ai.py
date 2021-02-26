import pandas
from pandas.core.frame import DataFrame


def read_csv() -> DataFrame:
    return pandas.read_csv('chicago_taxi_trips_2016_12.csv',
                           parse_dates=True,
                           infer_datetime_format=True)


def main() -> None:
    df = read_csv()
    print(df.head)


if (__name__ == '__main__'):
    main()
