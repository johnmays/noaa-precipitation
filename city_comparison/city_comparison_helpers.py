# Author: John Mays

import pandas as pd

def check_years(city_schema, csv_dir = '../data/GSOY/', rng=(2012,2021)):
    ''' Iterates through CSVs and tells me which places are missing
        which years.
    '''
    any_missing_flag = False # true if ANY years are missing in any data
    for _, row in city_schema.iterrows():
        city_df = pd.read_csv((csv_dir + row['Station'] + ".csv"))
        years = list(city_df["DATE"])
        missing_flag = False # true if years are missing in this city
        for year in range(rng[0], (rng[1]+1)):
            if year not in years:
                if missing_flag == False:
                    print(row['City'] + " is missing years:")
                    missing_flag = True
                    any_missing_flag = True
                print(year)
    if any_missing_flag == False:
        print("There are no missing years in the data.")
        


def total_concat(city_schema, columns, csv_dir = '../data/GSOY/',
                rng=(2012, 2022)):
    ''' Concatenates all of the individual cities' csvs together in one
    data frame, adding a "CITY" column & restricting to the years
    specified in (range)
    '''
    # initializing empty df:
    total_df = None
    # stitch all of the data frames together:
    for i, row in city_schema.iterrows():
        city_df = pd.read_csv((csv_dir + row['Station'] + ".csv"))
        city_df = city_df[city_df['DATE'].isin(range(rng[0], (rng[1] + 1)))]
        # add city name to DF:
        city_df["CITY"] = row['City']
        if i == 0:
            total_df = city_df
        else:
            total_df = pd.concat([total_df, city_df])
    # restrict df to important columns only: 
    total_df = total_df[(columns + ["CITY"])]
    return total_df

def series_comparison(series1:pd.Series, series2:pd.Series, titles=[]) -> None:
    ''' A method for printing two pandas series side by side
    
    Args:
        series1, series2::pd.Series: two pandas series of the same length
        titles(optional):
    Returns:
        None
    '''
    series1 = series1.to_string().split("\n")
    series2 = series2.to_string().split("\n")
    longest_string = max(map((lambda x: len(x)), series1))
    if titles != []:
        longest_string = max(longest_string, len(titles[0]))
        print(titles[0].ljust(longest_string, ' ') + " | " + titles[1])
    for i in range(len(series2)):
        print(series1[i].ljust(longest_string, ' ') + " | " + series2[i])  

def view_city(city_name, city_dict, columns, csv_dir = '../data/GSOY/', 
              rng=(2012, 2022)):
    '''
    '''
    csv_name = city_dict[city_name]
    city_df = pd.read_csv((csv_dir + csv_name + ".csv"))
    city_df = city_df[city_df['DATE'].isin(range(rng[0], (rng[1] + 1)))]
    city_df = city_df[columns]
    return city_df  