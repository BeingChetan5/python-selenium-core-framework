import os
import sys
import pytest
from test_settings import Settings
from conftest import setup, close_browser, get_data_from_csv, launch_browser


@pytest.mark.usefixtures("close_browser")
@pytest.mark.usefixtures("launch_browser")
@pytest.mark.usefixtures("setup")
class TestHome:

    def test_read_data_from_csv(self, get_data_from_csv):
        data = get_data_from_csv
        print("\n\nData in test file:", data)

    def test_open_browser_and_verify_home_screen(self):
        self.home_page.verify_home_screen()
