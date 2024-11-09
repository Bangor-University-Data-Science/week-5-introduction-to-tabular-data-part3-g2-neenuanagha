import pandas as  pd

def import_data(filename):

    return pd.read_excel(filename)


def filter_data(data):

    filter1 = data["CustomerID"].isna()

    filter2 = data["Quantity"] < 0

    filter3 = data["UnitPrice"] < 0

    filtered_data = data[~filter1 & ~filter2 & ~filter3]

    return filtered_data


def get_loyal_customers(filtered_data, min_purchases=5):

    purchase_counts = filtered_data.groupby("CustomerID").size().reset_index(name="PurchaseCount")
    
    loyal_customers = purchase_counts[purchase_counts["PurchaseCount"] >= min_purchases]
    
    return loyal_customers


def calculate_quarterly_revenue(filtered_data):
    
    filtered_data['InvoiceDate'] = pd.to_datetime(filtered_data['InvoiceDate'])
    
    filtered_data['Revenue'] = filtered_data['Quantity'] * filtered_data['UnitPrice']
    
  
    filtered_data['quarter'] = filtered_data['InvoiceDate'].dt.to_period('Q')
    
    
    quarterly_revenue_data = filtered_data.groupby('quarter')['Revenue'].sum().reset_index()

    quarterly_revenue_data.columns = ['quarter', 'total_revenue']
    
    return quarterly_revenue_data


def get_top_n_products(data, top_n):
  
    product_sales = data.groupby('Description')['Quantity'].sum().reset_index()

    product_sales_sorted = product_sales.sort_values(by='Quantity', ascending=False)

    top_products = product_sales_sorted.iloc[:top_n]

    return top_products

def purchase_patterns(filtered_data):

    summary = filter_data.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    
  
    summary.columns = ['product', 'avg_quantity', 'avg_unit_price']
    
    return summary

def answer_conceptual_questions() -> dict:
    return {
        "Q1": {"A"},  
        "Q2": {"B"}, 
        "Q3": {"C"}, 
        "Q4": {"A", "B", "C"},  
        "Q5": {"A"},  
    }


