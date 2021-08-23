import pytest

from scrapper.source.job_korea_ac_kr import JobKoreaAcKrScrapper


@pytest.fixture(scope='module')
def job_korea_ac_kr_scrapper():
    return JobKoreaAcKrScrapper()


def test_sign_in(job_korea_ac_kr_scrapper):
    job_korea_ac_kr_scrapper.sign_in()


def test_open_job_posting_page(job_korea_ac_kr_scrapper):
    job_korea_ac_kr_scrapper.open_job_posting_page()


def test_move_to_next_page(job_korea_ac_kr_scrapper):
    job_korea_ac_kr_scrapper.move_to_next_page()


def test_get_table(job_korea_ac_kr_scrapper):
    table = job_korea_ac_kr_scrapper.get_table()
    import pandas as pd

    assert type(table) == pd.DataFrame
