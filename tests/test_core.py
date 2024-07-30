import unittest
from ArcGISPyGnu.core import restGetVersion

class TestCore(unittest.TestCase):
    def test_rest_get_version(self):
        # Replace 'http://example.com/arcgis/rest/services' with a mock or a real endpoint for testing
        url = 'http://example.com/arcgis/rest/services'
        version = restGetVersion(url)
        self.assertIsInstance(version, str)

if __name__ == '__main__':
    unittest.main()
