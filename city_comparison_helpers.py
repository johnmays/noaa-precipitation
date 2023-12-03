# Author: John Mays

import pandas as pd

def check_years(city_dict, csv_dir = './data/GSOY/', rng=(2012,2021)):
    ''' Iterates through CSVs and tells me which places are missing
        which years.
    '''
    for city, csv_name in city_dict.items():
        city_df = pd.read_csv((csv_dir + csv_name + ".csv"))
        years = list(city_df["DATE"])
        any_missing_flag = False
        for year in range(rng[0], (rng[1]+1)):
            if year not in years:
                if any_missing_flag == False:
                    print(city + " is missing years:")
                    any_missing_flag = True
                print(year)


def total_concat(city_dict, columns, csv_dir = './data/GSOY/',
                rng=(2012, 2022)):
    ''' Concatenates all of the individual cities' csvs together in one
    data frame, adding a "CITY" column & restricting to the years
    specified in (range)
    '''
    # initializing empty df:
    total_df = None
    # stitch all of the data frames together:
    for i, (city, csv_name) in enumerate(city_dict.items()):
        city_df = pd.read_csv((csv_dir + csv_name + ".csv"))
        city_df = city_df[city_df['DATE'].isin(range(rng[0], (rng[1] + 1)))]
        # add city name to DF:
        city_df["CITY"] = city
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