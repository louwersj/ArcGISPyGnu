# ArcGISPyGnu

ArcGISPyGnu is a Python library for interacting with ArcGIS REST APIs. 


When trying to test the functionality of this Python library without having direct access to a test environment you could
use https://sampleserver6.arcgisonline.com/arcgis/rest

---

## Installation
WARNING : we are curretly in the first stages of development and due to this we have not released ArcGISPyGnu to the wider Python community and you CANNOT install ArcGISPyGnu using pip/pip3 at this very moment. For those who like to be part of the development / test efforts you can manually fork the code from github and use it locally.   
<!--
You can install the package via pip:

```bash
pip install ArcGISPyGnu
```
-->
---

## Functionality overview 
1. [restGetVersion](#restGetVersion)
2. [getVersion](#getVersion)
3. [restGetFolders](#restGetFolders)
4. [getFolders](#getFolders)
5. [restGetServices](#restgetServices)
4. [getServices](#getServices)
---
### restGetVersion
Fetches the version information from an ArcGIS REST API endpoint.
#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getVersion

#### parameters 
baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
#### Returns
str: The version information of the ArcGIS REST API or a message indicating the version information is not available.
#### Raises
SystemExit: If the URL is not valid or contains a query string or fragment.
Example
```python
version = restGetVersion("http://example.com/arcgis/rest/")
print(version)  # Output: 10.91 (or a similar version number)
```
---

### restGetFolders
Fetches the list of folders from an ArcGIS REST API endpoint. Folders in the ArcGIS REST API are essential for 
organizing and managing GIS resources. They help users categorize various services, maps, and data, facilitating easier 
navigation and maintenance. By grouping related resources, folders not only streamline the user experience but also aid 
in setting permissions and access controls, ensuring that sensitive information is protected. Additionally, a 
well-structured folder system enhances the efficiency of managing large datasets and services, allowing for quicker 
updates and deployments. Overall, folders play a crucial role in maintaining an organized, secure, and user-friendly 
environment within the ArcGIS ecosystem.

#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getServices

#### Parameters
baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
#### Returns
list: A list of folder names from the ArcGIS REST API or a message indicating the folders are not available.
#### Raises
SystemExit: If the URL is not valid or contains a query string or fragment.
#### Example
```python
folders = restGetFolders("http://example.com/arcgis/rest/")
print(folders)  # Output: ["AAA", "BBB", "CCC", "DDD"]
````
---

### restGetServices
Fetches the list of services from an ArcGIS REST API endpoint.
In the ArcGIS REST API, service types are categorized to facilitate different types of geographic and spatial operations, each designed to meet specific business needs and applications. These service types include Map Services, Feature Services, Image Services, Geocode Services, and Network Analysis Services, among others.

Map Services are primarily used for displaying geographic data in a web map. They allow users to access and interact with pre-rendered maps, which can be customized to show various layers and data points. This service type is ideal for applications that require rich, interactive maps, such as dashboards or client-facing applications that visualize spatial information.

Feature Services provide access to the underlying data of geographic features, such as points, lines, and polygons. These services support querying, editing, and updating of spatial data, making them crucial for applications that require real-time data interaction and management, like field data collection or dynamic data visualization.

Image Services are used to deliver raster data, such as satellite imagery or aerial photos. They enable applications to access and analyze large image datasets, providing capabilities for high-resolution imagery and raster analytics. This service type is particularly valuable for remote sensing, land cover analysis, and environmental monitoring.

Geocode Services offer address and location-based services, translating addresses into geographic coordinates and vice versa. This type of service is essential for applications that require address search, location-based querying, and route planning, such as customer relationship management (CRM) systems or logistics applications.

Network Analysis Services are used for tasks related to transportation networks, such as route finding, service area calculations, and network connectivity analysis. These services are key for optimizing routes, managing transportation logistics, and performing spatial analysis on network structures.

Each service type within the ArcGIS REST API is designed to handle specific aspects of spatial data and operations, allowing businesses to tailor their GIS solutions to meet particular needs, whether for mapping, data management, imagery analysis, geocoding, or network optimization.

#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getServices

#### Parameters
baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
####Returns
list: A list of dictionaries, each containing information about a service. Each dictionary has the following keys:
* name (str): The name of the service.
* type (str): The type of the service (e.g., MapServer, FeatureServer).

* Example raw retrun
```json
[
 {
  "name": "911CallsHotspot",
  "type": "GPServer"
 },
 {
  "name": "CommunityAddressing",
  "type": "MapServer"
 }
]

```
#### Examples
Printing Service Names
```python
services = getServices("http://example.com/arcgis/rest/")
if isinstance(services, list):
    for service in services:
        if isinstance(service, dict) and "name" in service:
            print(service["name"])
        else:
            print("Unexpected service format:", service)
else:
    print("Error or unexpected data returned:", services)

```
Printing Both Service Names and Types
```python
services = getServices("http://example.com/arcgis/rest/")
if isinstance(services, list):
    for service in services:
        if isinstance(service, dict) and "name" in service and "type" in service:
            print(f"Name: {service['name']}, Type: {service['type']}")
        else:
            print("Unexpected service format:", service)
else:
    print("Error or unexpected data returned:", services)

```
---

### restGetServiceByType

Fetches a list of service names from an ArcGIS REST API endpoint filtered by the specified service type.
#### Parameters
* baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment. The checkBaseUrl function from utils.py is used to validate and standardize this URL.
* serviceType (str): The type of services to filter by (e.g., "MapServer", "FeatureServer"). This parameter must be a string.
#### Returns
list: A list of service names that match the specified service type. Each item in the list is a string representing a service name. If no services match, an empty list is returned. Those service can be; Map Services, Feature Services, Image Services, Geocode Services or Network Analysis Services.  
#### Errors
* Invalid serviceType: If the serviceType parameter is not a string, the function will print an error message and exit.
* Invalid baseUrl: If the baseUrl is invalid, the function will print an error message and exit.
#### Examples
Fetching Services by Type  - fetch all services of type `MapServer`:
```Python
services = restGetServiceByType("http://example.com/arcgis/rest/services", "MapServer")
print(services)  # Output: ["SampleWorldCities/MapServer", "World/MapServer"]
```
Fetching Services by Type  - fetch all services of type `FeatureServer`
```python
services = restGetServiceByType("http://example.com/arcgis/rest/services", "FeatureServer")
print(services)  # Output: ["USA/FeatureServer"]
```