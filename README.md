# Tesla Stock Data ETL Project

## Overview
This project involves an ETL process for extracting stock price data for Tesla and Mercedes (for comparison analysis) from Yahoo Finance, transforming it using Pandas and loading it into an Azure SQL database. The final data supports visualisation in Power BI for insightful analysis.

## Data Source
The stock data for Tesla (TSLA) and Mercedes (MBGAF) covers the period from November 1, 2021, to November 2, 2023 and is sourced from Yahoo Finance.

## Technologies Used
Visual Studio Code for scripting
Python with Pandas for data manipulation
SQLAlchemy for interfacing with the database
Azure SQL Database as the data repository
Power BI for dashboard creation (data exported from Azure SQL DB)

## Installation
To set up the project, you need Python installed along with the following libraries: requests, yfinance, pandas, matplotlib and sqlalchemy. Use pip to install these libraries.

## Usage
Run the script to initiate the ETL process, which involves data extraction from Yahoo Finance, data transformation including cleaning and calculating daily returns and loading the data into an Azure SQL database.
Ensure you have configured your database credentials correctly in the script before running the process.

## Output
The ETL script outputs a table named 'StockData' in your Azure SQL database.

## Running the Script
The main Python script 'ETL_script.py' should be executed in an environment where all dependencies have been installed. Ensure your Azure SQL database is accessible and the credentials in the script are updated accordingly.

## Conclusion
After executing the script, you'll have a set of clean, organized data that can be further analyzed in Power BI to uncover trends and patterns in the stock performance of Tesla and Mercedes over the selected timeframe.