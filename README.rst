NOAA Precipitation Data: Exploring Rainy Weather in the U.S.
============================================================ 
.. image:: ./assets/nyc_1.jpg
  :width: 600
  :alt: New York City Street with rain and fog
*A rainy & foggy afternoon in NYC (src: Wikimedia Commons)*

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
     - Median no. of rainy days per year from 2011-2021
   * - Rochester, NY
     - 179.5
   * - Syracuse, NY
     - 177.0
   * - Seattle, WA
     - 176.0
   * - Buffalo, NY
     - 167.0
   * - Cleveland, OH
     - 163.0

But if you consider any size urban area (towns, cities, etc.), the list is completely different:

.. list-table:: Rainiest Towns & Cities by Days of Rainfall
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median no. of rainy days per year from 2011-2021
   * - Annette, AK
     - 237.0
   * - Forks, WA
     - 231.0
   * - Quillayute, WA
     - 200.0
   * - Astoria, OR
     - 199.0
   * - Aberdeen, WA
     - 195.0

But what about other ways to quantify "rainiest"?  Does the amount of rain count for nothing.  The town ranking doesn't change that much, but the major cities' sure does:

.. list-table:: Rainiest Cities by Total Rainfall
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median mm of rain per year from 2011-2021
   * - New Orleans, LA
     - 1734.50
   * - Miami, FL
     - 1676.00
   * - Houston, TX
     - 1293.00
   * - New York City, NY
     - 1177.30
   * - Cincinnati, OH
     - 1166.30

But what about the most total precipitation?  If we include snow, looking at towns and cities:

.. list-table:: Cities with the Most Total Precipitation
   :widths: 35 60
   :header-rows: 1

   * - City
     - Median mm of total precipitation per year from 2011-2021
   * - Presque Isle, ME
     - 4278.70
   * - Syracuse, NY
     - 4008.80
   * - Driggs, ID
     - 3840.00
   * - Annette, AK
     - 3826.20
   * - Brassau Dam, ME
     - 3543.80

See more extensive tables in `the main notebook. <./src/city_comparison.ipynb>`_

Here are all of the cities (without Annette) on a U.S. Map:

.. image:: ./assets/precipitation_map_01.png
  :width: 800
  :alt: Map of the continental U.S. with rainy cities shown

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
