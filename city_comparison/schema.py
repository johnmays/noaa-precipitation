import pandas as pd

partial_GSOY_schema = pd.DataFrame(
    {
        "Column" : [
            "DATE",
            "LATITUDE",
            "LONGITUDE",
            "PRCP",
            "SNOW",
            "DYFG",
            "DYHF",
            "DYTS",
            "EMXP",
            "DP01",
            "DP10",
            "DP1X",
            "DSNW",
        ],
        "Description" : [
            "year AD",
            "",
            "",
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