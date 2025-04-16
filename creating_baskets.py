import os
import pandas as pd
from collections import defaultdict

def CreateBaskets():
    '''
    Declare global variables ... data_directory & initialize market_baskets dict
    Unique swimmers will be identified by NAME & CLUB in case some swimmers share same names
    '''
    data_dir = 'data'
    market_baskets = defaultdict(list)

    '''
    loop over all csv files in the /data directory, get the event name by just dropping the .csv tag
    then read this csv into a pandas dataframe for pandas data manipulation libraries

    with swimmer name and swimemr club, append that files event into the swimmer club pair market basket

    throw exception if something goes wrong
    '''
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            event_name = filename.replace('.csv', '')
            file_path = os.path.join(data_dir, filename)

            try:
                df = pd.read_csv(file_path)
                df.columns = [col.strip() for col in df.columns]

                for _, row in df.iterrows():
                    swimmer = str(row.get("Swimmer", "")).strip()
                    club = str(row.get("Club", "")).strip()
                    if swimmer and club:
                        market_baskets[(swimmer, club)].append(event_name)

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    '''
    convert baskets to list of dicts for DataFrame that we'll write to a csv file
    '''
    basket_rows = [
        {"Swimmer": swimmer, "Club": club, "Events": ",".join(events)}
        for (swimmer, club), events in market_baskets.items()
    ]

    #print(market_baskets)

    '''
    throw an output for sanity check, if no errors write market baskets to a csv file
    '''
    #output_df = pd.DataFrame(basket_rows)
    #output_df.to_csv("market_baskets.csv", index=False)
    #print("Market baskets written to market_baskets.csv ✅")
    return market_baskets
