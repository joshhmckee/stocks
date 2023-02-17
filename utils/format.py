import pandas as pd

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