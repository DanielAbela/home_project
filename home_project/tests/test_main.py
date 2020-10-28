from unittest import TestCase

from main import validate_data, clean_up_data
import pandas as pd


class TestMain(TestCase):
    def test_validate_data_return_true(self):
        test_row = dict(Location="30, Monkhams Lane, Woodford Green, IG8 0NS", postcode="IG8 0NS")
        self.assertTrue(validate_data(test_row))

    def test_clean_up_data(self):
        test_df = pd.DataFrame(columns=['lat', 'long'], data=[[5.6987456, 4.2456895]])
        expected_df = pd.DataFrame(columns=['Latitude', 'Longitude'], data=[[5.699, 4.246]])
        actual_df = clean_up_data(test_df)
        pd.testing.assert_frame_equal(expected_df, actual_df)
