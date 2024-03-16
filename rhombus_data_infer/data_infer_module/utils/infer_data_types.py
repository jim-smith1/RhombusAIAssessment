import pandas as pd

def infer_and_convert_data_types(df):
    '''
    Helper and utility function for infering the datatypes for the columns in a pandas dataframe.
    :param df: a pandas dataframe
    :return: a pandas dataframe with the column datatypes infered.
    '''
    for col in df.columns:
        # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            df[col] = df_converted
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass

        # Check if the column should be categorical
        unique_values = df[col].nunique()
        total_values = len(df[col])
        if unique_values / total_values < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])
            continue

        # If none of the above conditions are met, consider it as a string
        df[col] = df[col].astype("string")

    return df
