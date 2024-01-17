"""
Test loading of the dataset
"""

import unittest
from scripts.repo_first_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    Class to test the dataset input in different ways
    """

    def setUp(self):
        """
        Path to dataset
        """
        self.path = "datasets/BooksDatasetClean.cnkjnsv"

    def test_extension_fail(self):
        """
        Test for the extension of the dataset
        """
        with self.assertRaises(TypeError):
            load_dataset(self.path)

    def test_dataset_is_loaded(self):
        """
        Test line to load the dataset
        """
        df = load_dataset(self.path)
        df.shape
        self.assertEqual(df.shape[0])


if __name__ == "_main_":
    unittest.main()

    # path.rsplit(".")
