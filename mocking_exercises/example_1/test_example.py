import unittest

from unittest import mock

from example_main import (
     retrieve_height_data,
     compute_height_stats
)


class TestExampleMain(unittest.TestCase):

    @mock.patch('example_main.retrieve_height_data')
    def test_compute_height_stats(self, mock_height_list):
        print('test_compute_height_stats')
        mock_height_list.return_value = [6, 6, 6, 6, 6, 6]
        height_mean, height_std = compute_height_stats()

        self.assertListEqual([height_mean, height_std],
                             [6, 0])

if __name__ == "__main__":
    unittest.main()









