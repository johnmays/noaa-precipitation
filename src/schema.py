import pandas as pd

partial_GSOY_schema = pd.DataFrame(
    {
        "Column" : [
            "DATE",
            "PRCP",
            "SNOW",
            "DYFG",
            "DYHF",
            "DYTS",
            "EMXP",
            "DP01",
            "DP10",
            "DP1X",
            "DSNW"
        ],
        "Description" : [
            "year AD",
            "total annual precipitation in inches",
            "total annual snowfall in inches",
            "number of days with fog",
            "number of days with 'heavy' fog",
            "number of days with thunderstorms",
            "highest daily total of precipitation in inches",
            "number of days with over 0.01 inches of unspecified \
            precipitation, probably rain w/o snow",
            "number of days with over 0.10 inches of unspecified \
            precipitation, probably rain w/o snow",
            "number of days with over 1.00 inches of unspecified \
            precipitation, probably rain w/o snow",
            "number of days with over 1.00 inches of snowfall"
        ]
    }
).set_index("Column")

city_schema = pd.DataFrame({
    "City": ["Seattle", "Miami", "New York City", "White Plains", "Brookhaven",
             "Syracuse", "Buffalo", "Erie", "Pittsburgh", "San Francisco",
             "West Lafayette", "Cleveland", "Portland", "Detroit", "Forks",
             "Boston", "Madison", "Woods Hole", "Monterey", "Richland",
             "Cincinnati", "Rochester", "Astoria", "Annette", "Columbus",
             "New Orleans", "Houston", "Port Arthur", "Lake Jackson", "Sequim",
             "Spokane", "Quillayute", "Aberdeen", "Hoquiam", "Conneaut",
             "Driggs", "Norton", "Dunkirk", "West Palm", "Presque Isle",
             "Brassau Dam", "Chicago"],
    "State": ["WA", "FL", "NY", "NY", "NY", "NY", "NY", "PA", "PA", "CA", "IN",
              "OH", "OR", "MI", "WA", "MA", "WI", "MA", "CA", "WA", "OH", "NY",
              "OR", "AK", "OH", "LA", "TX", "TX", "TX", "WA", "WA", "WA", "WA",
              "WA", "OH", "ID", "VA", "NY", "FL", "ME", "ME", "IL"],
    "Station": ['USW00094290', 'USW00012839', 'USW00094728', 'USW00094745',
                'USW00054790', 'USW00014771', 'USW00014733', 'USW00014860',
                'USW00014762', 'USW00023272', 'USC00129430', 'USW00014820',
                'USC00356750', 'CA006139520', 'USC00452914', 'USW00014739',
                'USC00470273', 'US1MABA0003', 'USW00023259', 'USW00024163',
                'USW00093812', 'USC00309049', 'USW00094224', 'USW00025325',
                'USW00014821', 'USW00012916', 'USW00012960', 'USW00012917',
                'USW00012976', 'USC00457544', 'USW00024157', 'USW00094240',
                'USC00450008', 'USW00094225', 'USW00004857', 'USC00480140',
                'USC00449215', 'USW00014747', 'USW00012844', 'USW00014607',
                'USC00170814', 'USC00111577'],
    "Size": ["City", "City", "City", "City", "Town",
             "City", "City", "Erie", "City", "City",
             "Town", "City", "City", "City", "Town",
             "City", "City", "Town", "Town", "Town",
             "City", "City", "Town", "Town", "City",
             "City", "City", "Town", "Town", "Town",
             "City", "Town", "Town", "Town", "Town",
             "Town", "Town", "Town", "Town", "Town",
             "Town", "City"]
})


cities_stations = {
    "Seattle": "USW00094290",
    "Miami": "USW00012839", # USW00092811
    "New York City": "USW00094728",
    "White Plains": "USW00094745", # techinically Westchester County, NY
    "Brookhaven": "USW00054790",
    "Syracuse": "USW00014771",
    "Buffalo": "USW00014733",
    "Erie": "USW00014860",
    "Pittsburgh": "USW00014762",
    "San Francisco": "USW00023272",
    "West Lafayette": "USC00129430",
    "Cleveland": "USW00014820",
    "Portland": "USC00356750",
    "Detroit": "CA006139520", # USW00014822, # USC00202016
    "Forks": "USC00452914",
    "Boston": "USW00014739",
    "Madison": "USC00470273",
    "Woods Hole": "US1MABA0003", # US1MABA0013 | technically Falmouth, MA
    "Monterey": "USW00023259",
    "Richland": "USW00024163", # USC00457015
    "Cincinnati": "USW00093812",
    "Rochester": "USC00309049", # USW0001476
    "Astoria": "USW00094224", # (Oregon)
    "Annette": "USW00025325", # technically Ketchikan, AK
    "Columbus": "USW00014821",
    "New Orleans": "USW00012916",
    "Houston": "USW00012960",
    "Port Arthur": "USW00012917", # (Texas)
    "Lake Jackson": "USW00012976",
    "Sequim": "USC00457544", # (Washington)
    "Spokane": "USW00024157",
    "Quillayute": "USW00094240",
    "Aberdeen": "USC00450008",
    "Hoquiam": "USW00094225",
    "Conneaut": "USW00004857", # (Ohio)
    "Driggs": "USC00480140", # USC00102676 | technically Alta, Wyoming
    "Norton": "USC00449215", # technically Wise, Virginia
    # NO COMPLETE DATA IN VICINITY:
    # "Seaside": "USC00357641", # (Oregon) 
    "Dunkirk": "USW00014747", # US1NYCQ0009 | (New York)
    "West Palm": "USW00012844", # (Florida)
    "Presque Isle": "USW00014607", # technically Caribou, Maine
    "Brassau Dam": "USC00170814" # (Maine)
}