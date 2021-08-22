from selenium import webdriver

from paths import APP_PATH


class BaseWebScrapper:
    """Selenium-based web scrapper"""

    def __init__(self, os: str = 'macos', headless: bool = False):
        self._login = None
        self._os = os
        self._headless = headless

        self._driver = self._open_webdriver()

    def _get_chromedriver_path(self, os: str):
        """Get appropriate path of chromedriver by given os

        Args:
            os (str):

        Returns:
            driverLoc (str):
        """
        if os == 'linux64':
            # TODO : Something is not working well with linux64
            filename = 'chromedriver_linux64'
        elif os == 'macos64':
            filename = 'chromedriver_macos64'
        else:
            raise NotImplementedError(f'{os} not supported')

        driverLoc = str(APP_PATH / filename)

        return driverLoc

    def _open_webdriver(self):
        """Open selenium from predefined path"""
        driverLoc = self._get_chromedriver_path(self._os)

        options = webdriver.ChromeOptions()
        if self._headless is True:
            options.add_argument("--headless")

        return webdriver.Chrome(driverLoc, chrome_options=options)
