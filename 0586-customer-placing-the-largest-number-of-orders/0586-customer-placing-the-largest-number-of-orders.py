import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders.groupby("customer_number")["order_number"].count()
    return pd.DataFrame({
    "customer_number": [counts.idxmax()]
    })