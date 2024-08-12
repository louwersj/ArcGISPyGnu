import requests
from .utils import checkBaseUrl, printError


def restGetVersion(baseUrl):
    """
    Fetches the version information from an ArcGIS REST API endpoint.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.

    Returns:
        str: The version information.
    """
    # Validate the base URL using the checkBaseUrl function from utils
    validatedUrl = checkBaseUrl(baseUrl)

    try:
        response = requests.get(f"{validatedUrl}?f=json")
        response.raise_for_status()
        data = response.json()
        return data.get("currentVersion", "Version information not available.")
    except requests.RequestException as e:
        return f"An error occurred: {e}"


# Synonym function for restGetVersion
def getVersion(baseUrl):
    """
    synonym for restGetVersion
    """
    return restGetVersion(baseUrl)


def restGetFolders(baseUrl):
    """
    Fetches the list of folders from an ArcGIS REST API endpoint.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.

    Returns:
        list: A list of folder names, or a message indicating the folders are not available.
    """

    # Validate the base URL using the checkBaseUrl function from utils
    validatedUrl = checkBaseUrl(baseUrl)

    try:
        # Get the complete tree structure
        treeStructure = restGetTreeStructure(validatedUrl)

        # Extract folder names from the tree structure
        folders = []

        def extractFolders(folderData):
            """
            Recursively extract folder names from the tree structure.

            Args:
                folderData (dict): The JSON data of the current folder.

            """
            for folder in folderData.get("folders", []):
                folders.append(folder["name"])
                extractFolders(folder)  # Recurse into subfolders

        extractFolders(treeStructure)

        return folders if folders else "Folders information not available."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Folders information not available."


def getFolders(baseUrl):
    """
    synonym for restGetFolders
    """
    return restGetFolders(baseUrl)


def restGetServices(baseUrl):
    """
    Fetches the list of services from an ArcGIS REST API endpoint.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.

    Returns:
        list: A list of service dictionaries, or a message indicating the services are not available.
    """

    # Validate the base URL using the checkBaseUrl function from utils
    validatedUrl = checkBaseUrl(baseUrl)

    try:
        # Get the complete tree structure
        treeStructure = restGetTreeStructure(validatedUrl)

        # Extract services from the tree structure
        services = []

        def extractServices(folderData):
            """
            Recursively extract service information from the tree structure.

            Args:
                folderData (dict): The JSON data of the current folder.
            """
            services.extend(folderData.get("services", []))
            for folder in folderData.get("folders", []):
                extractServices(folder)  # Recurse into subfolders

        extractServices(treeStructure)

        return services if services else "Services information not available."
    except Exception as e:
        return f"An error occurred: {e}"


def getServices(baseUrl):
    """
    synonym for restGetServices
    """
    return restGetServices(baseUrl)


def restGetServiceTypes(baseUrl: str) -> list:
    """
    Fetches a distinct list of all service types from an ArcGIS REST API endpoint.

    This function calls `restGetServices` to retrieve the list of services and then extracts
    distinct service types from the response.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.

    Returns:
        list: A distinct list of service types found in the API response. If no types are found, an empty list is
        returned.
    """
    services = restGetServices(baseUrl)

    if isinstance(services, list):
        service_types = {service.get("type") for service in services if isinstance(service, dict) and "type" in service}
        return list(service_types)
    else:
        print("Error or unexpected data returned:", services)
        return []


def getServiceTypes(baseUrl):
    """
    synonym for restGetServiceTypes
    """
    return restGetServiceTypes(baseUrl)


def restGetServiceByType(baseUrl: str, serviceType: str) -> list:
    """
    Fetches a list of service names from an ArcGIS REST API endpoint filtered by the specified service type.

    This function calls `restGetServices` to retrieve the list of services and filters the results
    based on the specified service type.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API. It should not contain a path, query string, or fragment.
        serviceType (str): The type of services to filter by (e.g., "MapServer", "FeatureServer").

    Returns:
        list: A list of service names that match the specified service type. If no services match, an empty list is
        returned.
    """
    # Validate the base URL using the checkBaseUrl function from utils
    validatedUrl = checkBaseUrl(baseUrl)

    # Check if serviceType is a string
    if not isinstance(serviceType, str):
        print("Error: The serviceType argument must be a string.")
        sys.exit(1)

    services = restGetServices(validatedUrl)

    if isinstance(services, list):
        filtered_services = [
            service.get("name")
            for service in services
            if isinstance(service, dict) and service.get("type") == serviceType
        ]
        return filtered_services
    else:
        print("Error or unexpected data returned:", services)
        return []


def getServiceByType(baseUrl, serviceType):
    """
    synonym for restGetServiceByType
    """
    return restGetServiceByType(baseUrl, serviceType)


def restGetFolderContent(baseUrl, folderName):
    """
    Fetches the content of a specified folder from an ArcGIS REST API endpoint.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        folderName (str): The name of the folder to fetch the content from.

    Returns:
        dict: A dictionary containing the folder's services and subfolders.
    """
    try:
        # Validate the base URL
        validatedUrl = checkBaseUrl(baseUrl)

        # Ensure the folderName does not start with a slash
        cleanedFolderName = folderName.lstrip('/')
        folderUrl = f"{validatedUrl}/services/{cleanedFolderName}?f=json"
        response = requests.get(folderUrl)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred while fetching folder content for {folderName}: {e}")
        return None


def getFolderContent(baseUrl, folderName):
    """
    synonym for restGetFolderContent
    """
    return restGetFolderContent(baseUrl, folderName)


def restGetTreeStructure(baseUrl):
    """
    Creates a tree structure of the ArcGIS REST API folders and services.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.

    Returns:
        dict: A JSON-like dictionary representing the tree structure of the folders and services.
    """
    validatedUrl = checkBaseUrl(baseUrl)

    try:
        response = requests.get(f"{validatedUrl}/services?f=json")
        response.raise_for_status()
        rootData = response.json()
    except requests.RequestException as e:
        print(f"An error occurred while fetching the base URL content: {e}")
        sys.exit(1)

    def buildTree(folderData, currentPath):
        """
        Recursively builds the tree structure for each folder.

        Args:
            folderData (dict): The JSON data of the current folder.
            currentPath (str): The current folder path in the API.

        Returns:
            dict: A dictionary representing the folder and its contents.
        """
        result = {
            "name": currentPath,
            "services": folderData.get("services", []),
            "folders": []
        }

        for subfolder in folderData.get("folders", []):
            subfolderPath = f"{currentPath}/{subfolder}".lstrip('/')
            subfolderData = restGetFolderContent(validatedUrl, subfolderPath)
            if subfolderData:
                result["folders"].append(buildTree(subfolderData, f"/{subfolderPath}"))

        return result

    # Start building the tree structure from the root data with the root name as "/"
    treeStructure = buildTree(rootData, "/")

    return treeStructure


def getTreeStructure(baseUrl):
    """
    synonym for restGetTreeStructure
    """
    return restGetTreeStructure(baseUrl)


def restGetMapServerDetails(baseUrl, serviceName):
    """
    Fetches the details of a MapServer service from an ArcGIS REST API endpoint.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        serviceName (str): The name of the MapServer service.

    Returns:
        dict: The JSON details of the MapServer service, or an error message if the request fails.
    """
    try:
        # Validate the base URL
        validatedUrl = checkBaseUrl(baseUrl)

        # Construct the service URL
        serviceUrl = f"{validatedUrl}/services/{serviceName}/MapServer?f=pjson"

        # Make the request to fetch the service details
        response = requests.get(serviceUrl)

        # Handle specific HTTP errors
        if response.status_code in {400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416,
                                    417, 500, 501, 502, 503, 504, 505}:
            printError(f"httpError{response.status_code}", serviceUrl)
        else:
            # Raise an HTTPError for other status codes
            response.raise_for_status()

        # If no errors, return the JSON response
        return response.json()

    except requests.RequestException as e:
        error_message = f"An error occurred while fetching the MapServer details for {serviceName}: {e}"
        printError("requestException", error_message)


def getMapServerDetails(baseUrl, serviceName):
    """
    synonym for restGetMapServerDetails
    """
    return restGetMapServerDetails(baseUrl, serviceName)


def restGetMapLayers(baseUrl, serviceName):
    """
    Fetches the list of layers from a MapServer service and returns their names, IDs, and types.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        serviceName (str): The name of the MapServer service.

    Returns:
        list: A list of dictionaries containing layer names, IDs, and types, or an error message if the request fails.
    """
    try:
        # Get the MapServer details using restGetMapServerDetails
        mapServerDetails = restGetMapServerDetails(baseUrl, serviceName)

        # Extract layers information
        layers = mapServerDetails.get('layers', [])

        # Prepare the list of layers with their IDs, names, and types
        layerList = [{'id': layer['id'], 'name': layer['name'], 'type': layer.get('type', 'Unknown')} for layer in
                     layers]

        return layerList

    except Exception as e:
        # Handle any exception that might occur
        printError("customError", f"Failed to fetch map layers: {e}")


def getMapLayers(baseUrl, serviceName):
    """
    synonym for restGetMapServerDetails
    """
    return restGetMapLayers(baseUrl, serviceName)


def restGetMapServerData(baseUrl, serviceName, layerId, where, outFields):
    """
    Fetches data from a specified map layer in an ArcGIS REST API service based on specific query parameters.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        serviceName (str): The name of the service containing the layer.
        layerId (int): The ID of the layer to query.
        where (str): The SQL where clause to filter the data.
        outFields (str): The fields to return.

    Returns:
        list: A list of features (dictionaries) containing the data from the layer.
    """
    # Validate the base URL
    validatedUrl = checkBaseUrl(baseUrl)
    queryUrl = f"{validatedUrl}/services/{serviceName}/MapServer/{layerId}/query"

    # Parameters for the query
    params = {
        'where': where,
        'outFields': outFields,
        'f': 'json',
        'returnGeometry': 'true',
        'outSR': '4326',
        'resultOffset': 0,
        'resultRecordCount': 1000  # Adjust as needed based on the max record count
    }

    features = []
    while True:
        try:
            response = requests.get(queryUrl, params=params)
            response.raise_for_status()
            data = response.json()
            features.extend(data.get('features', []))
            if len(data.get('features', [])) < params['resultRecordCount']:
                break
            params['resultOffset'] += params['resultRecordCount']
        except requests.exceptions.HTTPError as e:
            printError("httpError", e.response.status_code, queryUrl)
            break
        except requests.exceptions.RequestException as e:
            printError("RequestException", str(e), queryUrl)
            break

    return features


def restGetMapServerAllData(baseUrl, serviceName, layerId):
    """
    Fetches all data from a specified map layer in an ArcGIS REST API service.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        serviceName (str): The name of the service containing the layer.
        layerId (int): The ID of the layer to query.

    Returns:
        list: A list of features (dictionaries) containing all the data from the layer.
    """
    return restGetMapServerData(baseUrl, serviceName, layerId, where="1=1", outFields="*")


def restGetServiceType(baseUrl, serviceName):
    """
    Fetches the service type for a specific service name from an ArcGIS REST API.

    Args:
        baseUrl (str): The base URL of the ArcGIS REST API.
        serviceName (str): The name of the service to retrieve the type for.

    Returns:
        str: The service type (e.g., MapServer, FeatureServer) if found, or a message indicating the service was not
        found.
    """
    # Fetch all services using the restGetServices function
    services = restGetServices(baseUrl)

    # Iterate over the services to find the matching serviceName
    for service in services:
        if service.get('name') == serviceName:
            return service.get('type', "Service type not available.")

    return f"Service '{serviceName}' not found."
