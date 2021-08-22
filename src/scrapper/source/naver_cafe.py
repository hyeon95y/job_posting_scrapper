# Original code from
# https://riverkangg.github.io/크롤링/crawling-2naverCafe/
# Get appropriate chromedriver from
# https://chromedriver.chromium.org/downloads

import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from paths import APP_PATH

from scrapper.source._config_naver_cafe import NAVER_ID, NAVER_PASSWORD

class NaverCafeScrapper:
    def __init__(self, os : str = 'macos64', headless=bool:False):
        # 로그인 정보
        self._login = {"id" : NAVER_ID   # 네이버 아이디
                ,"pw" : NAVER_PASSWORD  # 네이버 비밀번호
                }
        print(NAVER_ID, NAVER_PASSWORD)

        self._os = os 
        self._headless = headless        
        self._driver = self._open_webdriver()

    def _get_chromedriver_path(self, os:str) :
        if os == 'linux64':
            # TODO : Something is not working well with linux64
            filename = 'chromedriver_linux64'
        elif os == 'macos64' :
            filename = 'chromedriver_macos64'

        driverLoc = str(APP_PATH / filename)

        return driverLoc
    
    def _open_webdriver(self) :
        # 크롬 웹 드라이버의 경로를 설정
        driverLoc = self._get_chromedriver_path(self._os)
        print(driverLoc)
        
        options = webdriver.ChromeOptions()
        # 브라우저 숨기기
        if self.headless is True : 
            options.add_argument("--headless") 
        
        self._driver = webdriver.Chrome(driverLoc, chrome_options=options)

    def open_page(self, url:str=None) :
        url = 'https://cafe.naver.com/iloveconsulting?iframe_url=/ArticleList.nhn%3Fsearch.clubid=18633550%26search.menuid=143%26search.boardtype=L'
        
        
        return