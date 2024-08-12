# ArcGISPyGnu

ArcGISPyGnu is a Python library for interacting with ArcGIS REST APIs. The current version iof ArcGISPyGnu is intended 
to be used against public (anonymous) access API endpoints and due to this no authentication has bene build into the 
library. For those who need this feel free to add the functionality and share back to the project. 


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
5. [restGetServiceByType](#restGetServiceByType)
6. [restGetMapServerDetails](#restGetMapServerDetails)
7. [restGetMapServerData](restGetMapServerData)
8. [restGetMapServerAllData](restGetMapServerAllData)
---
### restGetVersion
Fetches the version information from an ArcGIS REST API endpoint.
#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getVersion

#### Arguments 
baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
#### Returns
str: The version information of the ArcGIS REST API or a message indicating the version information is not available.
#### Raises
SystemExit: If the URL is not valid or contains a query string or fragment.
Example
```python
version = restGetVersion("https://sampleserver6.arcgisonline.com/arcgis/rest")
print(version)  # Output: 10.91 (or a similar version number)
```
---

### `restGetFolders`
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

#### Arguments
baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
#### Returns
list: A list of folder names from the ArcGIS REST API or a message indicating the folders are not available.
#### Raises
SystemExit: If the URL is not valid or contains a query string or fragment.
#### Example
```python
folders = restGetFolders("https://sampleserver6.arcgisonline.com/arcgis/rest")
print(folders)  # Output: ["AAA", "BBB", "CCC", "DDD"]
````
---

### `restGetServices`
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

#### Arguments
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
services = getServices("https://sampleserver6.arcgisonline.com/arcgis/rest")
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
services = getServices("https://sampleserver6.arcgisonline.com/arcgis/rest")
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

### `restGetServiceByType`

Fetches a list of service names from an ArcGIS REST API endpoint filtered by the specified service type.
#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getServiceByType
#### Arguments
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
services = restGetServiceByType("https://sampleserver6.arcgisonline.com/arcgis/rest", "MapServer")
print(services)  # Output: ["SampleWorldCities", "World"]
```
Fetching Services by Type  - fetch all services of type `FeatureServer`
```python
services = restGetServiceByType("https://sampleserver6.arcgisonline.com/arcgis/rest", "FeatureServer")
print(services)  # Output: ["USAData"]
```
---

### `restGetMapServerDetails`
The restGetMapServerDetails function fetches the details of a MapServer service from an ArcGIS REST API endpoint. This function validates the base URL, constructs the appropriate service URL, makes an HTTP request to retrieve the MapServer details in JSON format, and handles various HTTP errors gracefully.

#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* GetMapServerDetails

#### Arguments:
* baseUrl (str): The base URL of the ArcGIS REST API.
* serviceName (str): The name of the MapServer service.

#### Returns:
dict: The JSON details of the MapServer service. If the request fails, it prints an error message and exits the program.

#### Raises:
SystemExit: If an HTTP error occurs or a request exception is raised, the program will print an error message and exit.

#### Example Usage:
```python 
from core import restGetMapServerDetails

# Example base URL and service name
base_url = "https://sampleserver6.arcgisonline.com/arcgis/rest"
service_name = "MyMapService"

# Fetch the MapServer details
map_server_details = restGetMapServerDetails(base_url, service_name)

# Print the MapServer details
print(map_server_details)
```
----

### `restGetMapLayers`
Fetches the list of layers from a MapServer service and returns their names, IDs, and types.

#### synonyms
synonyms are provided for Python functions to streamline their usage and enhance convenience. These shorter names serve as aliases for the original, longer function names, making it easier to write and read code. Despite the abbreviated form, the functionality, error handling, and performance remain consistent with the original functions. Users can rely on these synonyms to perform tasks with the same accuracy and reliability, ensuring a seamless coding experience while maintaining compatibility with the full range of features and support provided by ArcGISPyGnu.
* getMapLayers

#### Arguments
* baseUrl (str): The base URL of the ArcGIS REST API.
* serviceName (str): The name of the MapServer service.

#### Returns
list: A list of dictionaries containing layer names, IDs, and types, or an error message if the request fails.

#### Example Usage
```python
# Example base URL and service name
base_url = "https://gisextern.dictu.nl/arcgis/rest/"
service_name = "Antenneregister/Antennes_extern"

# Fetch the layers
layers = restGetMapLayers(base_url, service_name)

# Print the layers
print(layers)
```

#### Error Handling
If an error occurs during the request, an error message will be printed using the printError function, and the function will return None.

----

### `restGetMapServerData`

Fetches data from a specific layer of a MapServer in an ArcGIS REST API. This function first verifies that the service is a MapServer before proceeding with the data retrieval.

#### arguments

- **`baseUrl`** (`str`): The base URL of the ArcGIS REST API.
  - Example: `https://sampleserver6.arcgisonline.com/arcgis/rest`

- **`serviceName`** (`str`): The name of the service to query.
  - Example: `YourServiceName`

- **`layerId`** (`int`): The ID of the layer to query. Defaults to `0` if not specified.
  - Example: `0`

- **`where`** (`str`): The WHERE clause for filtering data. Defaults to `"1=1"` (no filtering).
  - Example: `"1=1"`

- **`outFields`** (`str`): The fields to include in the query. Defaults to `"*"` (all fields).
  - Example: `"*"`

#### Returns

- **`dict`**: The JSON response containing the queried data or an error message.
  - The JSON response typically includes attributes such as:
    - `features`: A list of feature objects with geometry and attributes.
    - `fields`: A list of field objects that describe the attributes.
    - `objectIdFieldName`: The name of the field used as the unique identifier for each feature.
    - `geometryType`: The type of geometry (e.g., Point, Polygon).
  - Example response:
    ```json
    {
      "features": [
        {
          "attributes": {
            "OBJECTID": 1,
            "Name": "Feature 1"
          },
          "geometry": {
            "x": -117.1956,
            "y": 34.0563
          }
        }
      ],
      "fields": [
        {
          "name": "OBJECTID",
          "type": "esriFieldTypeOID"
        },
        {
          "name": "Name",
          "type": "esriFieldTypeString"
        }
      ],
      "objectIdFieldName": "OBJECTID",
      "geometryType": "esriGeometryPoint"
    }
    ```

#### Errors

- **HTTP Errors**: Handles various HTTP errors by printing an error message.
  - Example: `404` (Not Found) if the layer or service does not exist.
- **Request Errors**: Handles request exceptions and prints an error message.
- **Unexpected Errors**: Catches unexpected exceptions and prints an error message.

#### Usage Example

```python
base_url = "https://sampleserver6.arcgisonline.com/arcgis/rest"
service_name = "MyMapService"
layer_id = 0

# Fetch data from the specified layer
data = restGetMapServerData(base_url, service_name, layer_id, where="1=1", outFields="*")

# Print the data
print(data)
```
---

### `restGetMapServerAllData`

Fetches all data from a specific layer of a MapServer in an ArcGIS REST API by calling `restGetMapServerData` with default parameters that retrieve all records and fields.

#### Arguments

- **`baseUrl`** (`str`): The base URL of the ArcGIS REST API.
  - Example: `https://sampleserver6.arcgisonline.com/arcgis/rest`

- **`serviceName`** (`str`): The name of the service to query.
  - Example: `YourServiceName`

- **`layerId`** (`int`): The ID of the layer to query. Defaults to `0` if not specified.
  - Example: `0`

#### Returns

- **`dict`**: The JSON response containing the queried data or an error message.
  - The JSON response typically includes attributes such as:
    - `features`: A list of feature objects with geometry and attributes.
    - `fields`: A list of field objects that describe the attributes.
    - `objectIdFieldName`: The name of the field used as the unique identifier for each feature.
    - `geometryType`: The type of geometry (e.g., Point, Polygon).
  - Example response:
    ```json
    {
      "features": [
        {
          "attributes": {
            "OBJECTID": 1,
            "Name": "Feature 1"
          },
          "geometry": {
            "x": -117.1956,
            "y": 34.0563
          }
        }
      ],
      "fields": [
        {
          "name": "OBJECTID",
          "type": "esriFieldTypeOID"
        },
        {
          "name": "Name",
          "type": "esriFieldTypeString"
        }
      ],
      "objectIdFieldName": "OBJECTID",
      "geometryType": "esriGeometryPoint"
    }
    ```

#### Errors

- **HTTP Errors**: Handles various HTTP errors by printing an error message.
  - Example: `404` (Not Found) if the layer or service does not exist.
- **Request Errors**: Handles request exceptions and prints an error message.
- **Unexpected Errors**: Catches unexpected exceptions and prints an error message.

#### Usage Example

```python
base_url = "https://sampleserver6.arcgisonline.com/arcgis/rest"
service_name = "MyMapService"
layer_id = 0

# Fetch all data from the specified layer with default parameters
all_data = restGetMapServerAllData(base_url, service_name, layer_id)

# Print the data
print(all_data)
```
---

### `restGetServiceType`

Fetches the type of a specified service in an ArcGIS REST API by querying the service endpoint to determine if it is a MapServer or another type of service.

#### Arguments

- **`baseUrl`** (`str`): The base URL of the ArcGIS REST API.
  - Example: `https://sampleserver6.arcgisonline.com/arcgis/rest`

- **`serviceName`** (`str`): The name of the service to query.
  - Example: `MyMapService`

#### Returns

- **`str`**: The type of the service.
  - Common service types include:
    - `"MapServer"`: Indicates a MapServer service.
    - `"FeatureServer"`: Indicates a FeatureServer service.
    - `"ImageServer"`: Indicates an ImageServer service.
    - `"GeocodeServer"`: Indicates a GeocodeServer service.
  - Example return value: `"MapServer"`

#### Errors

- **HTTP Errors**: Handles various HTTP errors by printing an error message.
  - Example: `404` (Not Found) if the service does not exist.
- **Request Errors**: Handles request exceptions and prints an error message.
- **Unexpected Errors**: Catches unexpected exceptions and prints an error message.

#### Usage Example

```python
base_url = "https://sampleserver6.arcgisonline.com/arcgis/rest"
service_name = "MyMapService"

# Fetch the type of the specified service
service_type = restGetServiceType(base_url, service_name)

# Print the service type
print(f"Service Type: {service_type}")
```
---

