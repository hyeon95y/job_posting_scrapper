import pytest

from scrapper.source.job_korea_ac_kr import JobKoreaAcKrScrapper


@pytest.fixture(scope='module')
def job_korea_ac_kr_scrapper():
    return JobKoreaAcKrScrapper()


'''
def test_open_page(job_korea_ac_kr_scrapper):
    job_korea_ac_kr_scrapper.open_main_page()
'''


def test_sign_in(job_korea_ac_kr_scrapper):
    job_korea_ac_kr_scrapper.sign_in()
