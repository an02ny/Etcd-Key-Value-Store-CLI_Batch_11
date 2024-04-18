import unittest
from unittest.mock import MagicMock,patch

from week2_code import list_keys, get_value, put_key_value, delete_key_value

class TestEtcdFunctions(unittest.TestCase):

   
    def setUp(self):
        # Mocking etcd client
        self.mock_etcd = MagicMock()

    def test_list_keys(self):
    # Test list_keys function
    # Assuming there are keys "k1", "k2", "k3" in etcd
         expected_keys = ["k1", "k2", "k3"]

    # Mocking the etcd.get_all() method
         self.mock_etcd.get_all.return_value = [("k1", {"key": "metadata1"}), ("k2", {"key": "metadata2"}), ("k3", {"key": "metadata3"})]
    
         with patch('week2_code.etcd3.client', return_value=self.mock_etcd):
             keys = list_keys()
             self.assertEqual(keys, expected_keys)


    def test_put_get_delete_key(self):
        # Test put, get, and delete functions
        # Put a key-value pair
        put_key_value("test_key", "test_value")
        # Get the value of the key
        value = get_value("test_key")
        self.assertEqual(value, "test_value")
        # Delete the key
        delete_key_value("test_key")
        # Ensure the key is deleted
        value_after_deletion = get_value("test_key")
        self.assertEqual(value_after_deletion, "\033[1mKey not found.\033[0m")

if __name__ == '__main__':
    unittest.main()
