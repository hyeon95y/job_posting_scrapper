import pytest
from scrapper.source.naver_cafe import NaverCafeScrapper

@pytest.fixture(scope='module')
def naver_cafe_scrapper():
    return NaverCafeScrapper()

def test_open_page(naver_cafe_scrapper):
    
    naver_cafe_scrapper.open_page()