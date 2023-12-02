# Author: John Mays
'''
    The goal of this function is to use precipitation data to score a
    location for how much a rain enjoyer would enjoy it.
    This is an extremely subjective judgement
    Some basic assumptions and arithmetic go into computing the score:
    - The raw data will be:
        - inches of rain by month
        - inches of snow by month
        - number of foggy days by month
        - number of thunderstorms per month
    - Although total precipitation counts more than uniformity...
    - Uniformity is certainly better than not. To give an example:
        - 12 in of rain would be better as 6 in for two months as
          opposed to 0 in one month and 12 the next.
        - uniformity should be measured by total precipitation
          not just one type (rain or snow)
    - The max score is 1.0 and the min score is 0.0
    - The max would be achieved by a place that achieved the recorded 
      maximum precipitation every month for 12 months of the year
    - Thunderstorm > rain = fog > snow
'''

'''
    Some important figures:

    Maximum rainfall recorded in a month: 366 in India
    Source: https://www.guinnessworldrecords.com/world-records/greatest-monthly-rainfall-
    Maximum snowfall recorded in a month: 390 in California
    Source: https://weather.com/safety/winter/news/five-snowfall-extremes-20130103
    Max no. of foggy or thunder-y days: 
        total number of days in the month (31,30,29,28)
'''

# pseudocode for now:
def RES():
    # list ~12 balance parameters either in lists or mayeb all caps
    for m in range(12):
        pass
        # rain, snow, thunder_days, fog_days = ...
    # calculate mean absolute variation for all 4 elements
    # use balancing parameter to weigh deviation against total (for all 4)
    # use balancing parameter to weigh between the 4 & sum
    # return sum
         