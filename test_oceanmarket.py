# test_oceanmarket.py
"""
Tests for OceanMarket module.
"""

import unittest
from oceanmarket import OceanMarket

class TestOceanMarket(unittest.TestCase):
    """Test cases for OceanMarket class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OceanMarket()
        self.assertIsInstance(instance, OceanMarket)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OceanMarket()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
