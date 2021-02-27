import pandas as pd
from pandas.core.frame import DataFrame


def read_csv() -> DataFrame:
    return pd.read_csv('chicago_taxi_trips_2016_12.csv',
                       parse_dates=True,
                       infer_datetime_format=True)


def main() -> None:
    df = read_csv()

    numerics_df = df.select_dtypes(include='number')
    categoricals_df = df.select_dtypes(exclude='number')

    numerics_stats = pd.DataFrame(numerics_df.describe(include='all'))
    categoricals_stats = pd.DataFrame(categoricals_df.describe(include='all'))

    numerics = {
        'total_number_of_values': len(numerics_df),
        'percentage_of_missing_values': 100-(numerics_stats.loc['count']/len(numerics_df))*100,
        'cardinality': numerics_df.nunique(),
        'minimum_values': numerics_stats.loc['min'],
        'maximum_values': numerics_stats.loc['max'],
        'first_quartile': numerics_stats.loc['25%'],
        'third_quartile': numerics_stats.loc['75%'],
        'average': numerics_stats.loc['mean'],
        'median': numerics_stats.loc['50%'],
        'standard_deviation': numerics_stats.loc['std']
    }

    categoricals = {
        'total_number_of_values': len(categoricals_df),
        'percentage_of_missing_values': 100-(categoricals_stats.loc['count']/len(categoricals_df))*100,
        'cardinality': categoricals_df.nunique(),
        'mode': categoricals_df.mode()
    }

    """ print(numerics, end='\n\n')
    print(categoricals, end='\n\n') """


if (__name__ == '__main__'):
    main()
