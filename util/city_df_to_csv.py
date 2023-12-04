# Author: John Mays

import sys
import pandas as pd
sys.path.insert(0, '../city_comparison/')
import schema
destination = '../data/'
schema.city_schema.to_csv((destination + "cities.csv"))