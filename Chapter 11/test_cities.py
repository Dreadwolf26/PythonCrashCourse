import unittest
from city_functions import city_country

class TestCities(unittest.TestCase):
    
    def test_city_country(self):
        test_city_country_combined = city_country("atlanta", "georgia", "30000")
        self.assertEqual(test_city_country_combined, "Atlanta, Georgia - 30000")

unittest.main()