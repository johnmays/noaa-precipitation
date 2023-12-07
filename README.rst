NOAA Precipitation Data: Exploring Rainy Weather in the U.S.
============================================================ 
.. image:: ./assets/nyc_1.jpg
  :width: 600
  :alt: New York City Street with rain and fog
*A rainy & foggy afternoon in NYC (src: Wikimedia Commons)*

Motivation:
===========
There are two whys and two answers.

1. Why look at the rain data in the U.S.?

Answer: I am a rain-enjoyer: If I could choose exactly where to live, places with high rain and stormy weather would be at the top of my list.  I like the sun under certain conditions, but rain, fog, thunder, and snow do not bring me down, rather, they are aesthetically fulfilling and give me energy to handle the day.  I would like to know, if I want to enjoy some rainy weather, where I should go.

2. Why not consult an existing list?  

Answer: The internet is full of conflicting information on what the "rainiest places in the U.S." are.  And behind all internet top-ten lists, there is a more complex, underlying reality to be understood.  For instance, how do you quantify "raininess" and if a place is rainy, well, is the entire place *that* rainy?  If one weather station in Seattle reports x number of rainy days per year, how much does that translate to somewhere, say, 40 minutes outside of Seattle?  Also, quite a few lists seem to either not include small towns, or only selectively include them.  Well I would like to know how small towns fare as well, because I know, just probability-wise, that it is unlikely that the rainiest place in any U.S. state is a bigger city.  These are the things I aim to explore in this repository.

Environment & Stack:
====================
I am using Python 3.8.9 with a list of packages that can be found in `requirements.txt <./requirements.txt>`_.  I also make heavy use of jupyter notebooks.  All of the most important analysis is in `the main notebook <./city_comparison/city_comparison.ipynb>`_.

If you would like to run this project yourself, execute the following commands in your shell:

..  code-block:: sh

    $ git clone https://github.com/johnmays/noaa-precipitation.git
    $ cd noaa-precipitation
    noaa-precipitation $ pip install virtualenv
    noaa-precipitation $ virtualenv -p < optional path to python 3.8 > venv
    noaa-precipitation $ source venv/bin/activate
    (venv) noaa-precipitation $ pip install -r requirements.txt


Data:
=====
I am using publicly available **NOAA** data downloaded from `nceii.noa.gov <https://www.ncei.noaa.gov/access>`_.  This data is part of the global summary of the year (**GSOY**) dataset, which aggregates daily weather station data into yearly weather metrics like *"annual days with any rainfall"* and *"total annual millimeters of snowfall"*.  I wish there was a more efficient way to search for and access this data, but for now, I go to the search for a town/city I am curious about and look for suitable stations, then download their CSVs.  I specifically look for stations that have a complete set of yearly data from 2012 to 2021.

*An important note*: **GSOY** data is not by county or by city, but rather, by weather station.  Many cities have several weather stations and an airport, each with a long-running and complete dataset.  However, many towns only have one weather station near them that reported data to this service, and only did it for a few years in the early 1900's.  That is why some notoriously rainly towns, like Seaside, OR and even Providence, RI do not show up in my analysis, unfortunately.

Useful Definitions & Acronyms for the Uninitiated:
==================================================
- **NOAA:** National Oceanic and Atmospheric Administration; the US agecy responsible for for dealing with climate and the like
- **NCEI:** National Centers for Environmental Information; an entity under the **NOAA** that collects and distributes environmental data
- **USGS:** United States Geological Survey; the US agency responsible for monitoring landscape & natural resources
- **CDO:** Climate Data Online; a service that makes the NOAA's climate data accessible over the web
- **Geospatial:** Data that is associated with a location, e.g. height stored as a function of global coordinates
- **GIS:** Geographic Information Systems: Any software that has to do with geographic data
- **OGC:** Open Geospatial Consortium; a cooperative entity that creates standards for GIS data. Note: sometimes called **OpenGIS** as well
- **WMS:** Web Map Service; one of those OGC standardizations for an interface for requesting "map data" (images of geospatial data) from a server
- **NBD:** National Boundaries Dataset; the USGS's geospatial data, accessible online through a WMS, of global boundaries. There are boundaries for countries, US states, reservations, protected lands, you name it.

Results:
========
What is the rainiest city in the U.S.?  Depending on the parameters of your argument and how you choose to quantify this, that question has a few answers.
By the metric of days with rain per year, the top five cities (reasonably large ones) are:

.. list-table:: Rainiest Cities by Days of Rainfall
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median no. of rainy days per year from 2012-2021
   * - Rochester, NY
     - 179.5
   * - Syracuse,NY
     - 174.5
   * - Seattle,WA
     - 168.5
   * - Buffalo, NY
     - 167.0
   * - Cleveland,OH
     - 163.0

But if you consider any size urban area (towns, cities, etc.), the list is completely different:

.. list-table:: Rainiest Towns & Cities by Days of Rainfall
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median no. of rainy days per year from 2012-2021
   * - Hilo, HI
     - 270.5
   * - Annette, AK
     - 237.0
   * - Forks,WA
     - 224.5
   * - Raymond, WA
     - 220.0
   * - Quillayute, WA
     - 196.0
   * - Astoria, OR
     - 194.0
   * - Aberdeen, WA
     - 193.0
   * - Hoquiam, WA
     - 182.5
   * - Paradise, WA
     - 182.0
   * - Rochester, NY
     - 179.5

But what about other ways to quantify "rainiest"?  Does the amount of rain count for nothing.

.. list-table:: Rainiest Towns & Cities by Total Rainfall
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median mm of rain per year from 2012-2021
   * - Annette
     - 3782.85
   * - Paradise
     - 3275.50
   * - Quinault
     - 3166.45
   * - Forks
     - 3103.75
   * - Hilo
     - 3007.15
   * - Quillayute
     - 2733.55
   * - Aberdeen
     - 2336.75
   * - Raymond
     - 2326.75
   * - Tillamook
     - 2032.15
   * - Brevard
     - 1997.40

But what about the most total precipitation?  If we include snow, looking at towns and cities:

.. list-table:: Cities with the Most Total Precipitation
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median mm of total precipitation per year from 2012-2021
   * - Presque Isle, ME
     - 4444.65
   * - Syracuse, NY
     - 43962.00
   * - Annette, AK
     - 3782.85
   * - Driggs, ID
     - 3769.45
   * - Brassau Dam, ME
     - 3572.30

See more extensive tables in `the main notebook. <./city_comparison/city_comparison.ipynb>`_

Here are all of the cities (without Annette, AK and Hilo, HI) on a U.S. Map:

.. image:: ./assets/precipitation_map_01.png
  :width: 800
  :alt: Map of the continental U.S. with rainy cities shown

and Washington State as well:

.. image:: ./assets/precipitation_map_02.png
  :width: 600
  :alt: Map of the Washington State with rainy cities shown

Resources:
==========
- `Precipitation Data Overview <https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00947/html>`_ on the NOAA website
- `Data Access Homepage <https://www.ncei.noaa.gov/access>`_ on the NOAA website
- `GSOY data search <https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-year>`_ on the NOAA site
- `GSOY data README <https://www.ncei.noaa.gov/pub/data/metadata/documents/GSOYReadme.txt>`_ on the NOAA site
- `Weather Stations & their locations <https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt>`_ on the NOAA site
- `Information on the WMS standart <https://www.ogc.org/standard/wms/>`_ from the OGC
- `WMS GetCapabilities request <https://www.sciencebase.gov/catalogMaps/mapping/ows/4f70b219e4b058caae3f8e19?service=wms&request=getcapabilities&version=1.3.0>`_ for the **USGS** **NBD**
- `OWSLib Documentation <https://owslib.readthedocs.io/en/latest/>`_ (helpful python library)
