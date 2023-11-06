import json
import urllib.request
from unittest import TestCase
from unittest.mock import patch

API_URL = "http://worldclockapi.com/api/json/utc/now"
YMD_SEP_INDEX = 4
YMD_SEP = "-"
YMD_YEAR_SLICE = slice(0, 4)
DMY_SEP_INDEX = 2
DMY_SEP = "."
DMY_YEAR_SLICE = slice(6, 10)


def what_is_year_now() -> int:
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)
    datetime_str = resp_json["currentDateTime"]
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError("Invalid format")
    return int(year_str)


class TestWhatIsYearNow(TestCase):
    @patch("urllib.request.urlopen")
    def test_ymd_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            json.dumps({"currentDateTime": "2019-03-01"}).encode()
        )
        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_dmy_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            json.dumps({"currentDateTime": "01.03.2019"}).encode()
        )
        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_invalid_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            json.dumps({"currentDateTime": "2019/03/01"}).encode()
        )
        with self.assertRaises(ValueError):
            what_is_year_now()
