import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    join = pd.merge(
        customers,
        orders,
        how="left",
        left_on="id",
        right_on="customerId"
    )
    join.rename(columns={"name":"Customers"},inplace="True")
    return join[join["customerId"].isna()][["Customers"]]