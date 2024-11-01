import pandas as  pd

def import_data(filename):

    return pd.read_excel(filename)


def filter_data(data):

    filter1 = data["CustomerID"].isna()

    filter2 = data["Quantity"] < 0

    filter3 = data["UnitPrice"] < 0

    filtered_data = data[~filter1 & ~filter2 & ~filter3]

    return filtered_data