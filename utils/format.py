import pandas as pd

def format_financial_table(df: pd.DataFrame, data_name: str, date_format: str) -> pd.DataFrame:
    """
    function used to turn format financial tables with two columns [date, data_name (currency)].

    example: format_financial_table(pd.DataFrame({'date': ['2020', '2021'], 'revenue': ['$12,342.31', '$3,234.12']}), 'revenue', '%Y)

    :param df: a pandas `DataFrame` with data
    :param data_name: a column name with currency data
    :param date_format: a `str` to format index dates
    :return: a formatted `DataFrame`
    """
    # formatting the dataframe
    df.columns = ['date', data_name]
    df['date'] =  pd.to_datetime(df['date'], format=date_format)
    df.set_index('date', inplace=True)
    df = columns_price_to_float(df, [data_name])
    df.sort_index(inplace=True)

    if data_name == 'revenue':
        # multiply since table revenue is in millions
        df[data_name] *= 1e6

    return df

def columns_price_to_float(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    function used to turn `DataFrame` columns of prices ($ and commas) into type `float`.

    example: columns_price_to_float(pd.DataFrame({'date': [1, 2], 'revenue': ['$12,342.31', '$3,234.12']}), ['revenue'])

    :param df: a pandas `DataFrame` with data
    :param columns: a `list` of column names in df
    :return: a `DataFrame` with the updates
    """
    for column in columns:
        df[column] = df[column].str.replace('$','', regex=True)
        df[column] = df[column].str.replace(',','', regex=True)
        df[column] = df[column].astype(float)
    return df