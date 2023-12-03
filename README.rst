NOAA Precipitation Data:
========================
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

Resources:
==========
- `Precipitation Data Overview <https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00947/html>`_ on the NOAA website
- `Data Access Homepage <https://www.ncei.noaa.gov/access>`_ on the NOAA website
- `GSOY data search <https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-year>`_ on the NOAA site
- `Weather Stations & their locations <https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt>`_ on the NOAA site
- `Information on the WMS standart <https://www.ogc.org/standard/wms/>`_ from the OGC
- `WMS GetCapabilities request <https://www.sciencebase.gov/catalogMaps/mapping/ows/4f70b219e4b058caae3f8e19?service=wms&request=getcapabilities&version=1.3.0>`_ for the **USGS** **NBD**
- `OWSLib Documentation <https://owslib.readthedocs.io/en/latest/>`_ (helpful python library)
