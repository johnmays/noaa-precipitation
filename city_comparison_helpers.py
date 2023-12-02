# Author: John Mays

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