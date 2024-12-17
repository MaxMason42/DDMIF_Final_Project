import pandas as pd
import datetime as dt
import argparse
import os
import wrds
from typing import List, Optional
from settings.default import WRDS_TICKERS #Change based on the assets you want to download and test

def get_wrds_connection(username: Optional[str] = None) -> wrds.Connection:
    return wrds.Connection(wrds_username=username)

def download_stock_data(
    start_date: str = "2016-01-01",
    end_date: Optional[str] = None,
    output_dir: str = os.path.join("data", "wrds")
) -> None:
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Connect to WRDS
    db = get_wrds_connection()
    
    for ticker in WRDS_TICKERS:
        permno = None
        if ticker == "BG":
            permno = 89138
        elif ticker == "LEN":
            print("NEED PERMNO")
            permno = 52708
        elif ticker == "META":
            permno = 13407
        elif ticker == "MS":
            permno = 69032

        print(f"Downloading data for {ticker}")
        try:
            # Query CRSP data
            if ticker != "BG" and ticker != "LEN" and ticker != "META" and ticker != "MS":
                query = f"""
                    SELECT date, prc, cfacpr
                    FROM crsp.dsf
                    WHERE permno IN (
                        SELECT permno
                        FROM crsp.dsenames
                        WHERE ticker = '{ticker}'
                    )
                    AND date >= '{start_date}'
                    {f"AND date <= '{end_date}'" if end_date else ""}
                    ORDER BY date
                """
            else:
                print("This is BG or LEN or META or MS")
                query = f"""
                    SELECT date, prc, cfacpr
                    FROM crsp.dsf
                    WHERE permno = {permno}
                    AND date >= '{start_date}'
                    {f"AND date <= '{end_date}'" if end_date else ""}
                    ORDER BY date
                """
            
            data = db.raw_sql(query)
            
            # Process and save data
            if not data.empty:
                # Calculate adjusted price
                # Note: prc is negative if it's a bid/ask average
                data['prc'] = data['prc'].abs()
                
                # If cfacpr (cumulative factor for adjusting prices) is available, use it
                if 'cfacpr' in data.columns and not data['cfacpr'].isna().all():
                    data['Adj_Close'] = data['prc'] / data['cfacpr']
                else:
                    raise Exception("No adjustment factor found.")
                
                # Rename columns and set index
                data = data.rename(columns={'date': 'Date'})
                data.set_index('Date', inplace=True)
                
                # Save to CSV
                output_file = os.path.join(output_dir, f"{ticker}.csv")
                data[['Adj_Close']].to_csv(output_file)
                print(f"Saved data to {output_file}")
            else:
                print(f"No data found for {ticker}")
                
        except Exception as ex:
            print(f"Error downloading {ticker}: {str(ex)}")
    
    # Close WRDS connection
    db.close()


if __name__ == "__main__":
    download_stock_data()