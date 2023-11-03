import requests
import yfinance as yf
import pandas as pd
import matplotlib 
from sqlalchemy import create_engine


def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data for specific ticker between start_date and end_date."""
    return yf.download(ticker, start=start_date, end=end_date)

# Fetch data for Tesla and Mercedes
tesla_data = fetch_stock_data('TSLA', '2021-11-01', '2023-11-02')
mercedes_data = fetch_stock_data('MBGAF', '2021-11-01', '2023-11-02')


def check_dates(tesla, mercedes):
    # Find if there are dates that do not exist in either datasets
    print("Mercedes not in Tesla:", mercedes.index.difference(tesla.index))
    print("Tesla not in Mercedes:", tesla.index.difference(mercedes.index))

check_dates(tesla_data, mercedes_data)


def check_missing_values(dataframe):
    """Return columns with missing values and their count."""
    return dataframe.isnull().sum()

print("Missing values in Tesla data:")
print(check_missing_values(tesla_data))

print("\nMissing values in Mercedes data:")
print(check_missing_values(mercedes_data))


def check_duplicates(dataframe):
    #Return the number of duplicate rows.
    return dataframe.duplicated().sum()

print("Duplicate rows in Tesla data:", check_duplicates(tesla_data))
print("Duplicate rows in Mercedes data:", check_duplicates(mercedes_data))


def calculate_daily_returns(dataframe):
    # The percentage change in stock price from the previous day. Calculate and add daily returns to the dataframe.
    dataframe['Daily Return'] = dataframe['Adj Close'].pct_change() * 100

calculate_daily_returns(tesla_data)
calculate_daily_returns(mercedes_data)


#Checking data type before loading to a structured database 
print(tesla_data.dtypes)
print(mercedes_data.dtypes)


#Add a stockname column to each DataFrame to distinguish between Tesla and Mercedes after I merge it 
tesla_data['StockName'] = 'Tesla'
mercedes_data['StockName'] = 'Mercedes'


#Concatenate the two DataFrames vertically, as they have the same structure. Drop First row as daily return cannot be calculated 
combined_data = pd.concat([tesla_data, mercedes_data])
combined_data = combined_data.dropna(subset=['Daily Return'])


# Doing a final check of the combined dataframe
print(combined_data.head(10))
print(combined_data.tail(10))


# Turning the Date index into a datw column
combined_data.reset_index(inplace=True)
print(combined_data.columns)


# Changing the date column to a datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'], errors='coerce')


# Function to create SQL engine and upload DataFrame
def upload_to_sql(df, table_name, server, database, username, password):
    conn_str = (
        f'mssql+pyodbc://{username}:{password}@{server}/{database}'
        f'?driver=ODBC+Driver+18+for+SQL+Server'
    )
    engine = create_engine(conn_str, echo=False)
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

upload_to_sql(
    df=combined_data,
    table_name='StockData',
    server='myserversd.database.windows.net',
    database='mydbsd',
    username='myserveradminlogin',
    password='RemoteControl1!'
)


combined_data.to_csv('combined_data.csv', index=False)
















