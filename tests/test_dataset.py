import unittest
from unittest.mock import patch
from scripts.repo_first_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    Class to test the dataset input in different ways
    """

    def setUp(self):
        """
        Path to dataset
        """
        self.path = "datasets/BooksDatasetClean.csv"

    def test_extension_fail(self):
        """
        Test for the extension of the dataset
        """
        with patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.side_effect = FileNotFoundError("Mocked FileNotFoundError")
            with self.assertRaises(FileNotFoundError) as cm:
                load_dataset(self.path)
            self.assertEqual(str(cm.exception), "Mocked FileNotFoundError")

    def test_dataset_is_loaded(self):
        """
        Test line to load the dataset
        """
        df = load_dataset(self.path)
        self.assertEqual(df.shape[0], 103063)  # Expected number of rows

if __name__ == "__main__":
    unittest.main()

    # path.rsplit(".")
