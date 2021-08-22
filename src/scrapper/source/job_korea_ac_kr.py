import time

import pandas as pd

from scrapper.source.base_web_scrapper import BaseWebScrapper
from scrapper.source.config.job_korea_ac_kr import KOREA_AC_KR_ID, KOREA_AC_KR_PASSWORD

MAIN_URL = 'https://job.korea.ac.kr/user/index/home/homeMain.do'
SIGN_IN_URL = 'https://job.korea.ac.kr/user/login/login/initLogin.do;jsessionid=z97LhvTKqp1gxT4TzYt7HyGPFXGvFsgHtcyPhQbKYcJP822sPj6d!-1194304187'
JOB_POSTINGS_URL = 'https://job.korea.ac.kr/user/recu/recruit/recruitList.do?searchRecuRcmdCd=002'

SIGN_IN_ID_XPATH = '//*[@id="loginIdK"]'
SIGN_IN_PW_XPATH = '//*[@id="loginPwdK"]'
SIGN_IN_PROCEED_XPATH = '//*[@id="loginBtn"]'

JOB_POSTING_TABLE_XPATH = '//*[@id="sub_container"]/div[3]/div[2]/div[3]/table/tbody'


class JobKoreaAcKrScrapper(BaseWebScrapper):
    def __init__(self, os: str = 'macos64', headless: bool = False):
        super().__init__(os=os, headless=headless)
        self._login = {'id': KOREA_AC_KR_ID, 'pw': KOREA_AC_KR_PASSWORD}
        self._page_num = None

    def open_job_posting_page(self):
        self._driver.get(JOB_POSTINGS_URL)
        self._current_page_num = 1

    def move_to_next_page(self):
        next_page_xpath = self._get_next_page_xpath(self._current_page_num)
        self._driver.find_element_by_xpath(next_page_xpath).click()
        self._current_page_num += 1

    def _get_next_page_xpath(self, current_page_num: int):
        return '//*[@id="sub_container"]/div[3]/div[2]/div[4]/div/a[%s]' % (current_page_num + 2)

    def _get_table(self):
        table = self._driver.find_element_by_xpath(JOB_POSTING_TABLE_XPATH)
        table = self._parse_table(table)
        return table

    def _parse_table(self, table):
        data_dates = []
        data_titles = []

        # Get posting & ending-dates
        posts = table.text.split('작성일')
        for idx in range(1, len(posts)):
            post = posts[idx]
            post = post.replace(': ', '').replace('\n', ' ')

            post_date = post[:11]
            if '채용시 마감' in post:
                end_date = '채용시 마감'
                post = post[post.find('채용시 마감') + 6:]
            else:
                end_date = post[post.find('마감일') + 3: post.find('마감일') + 13]
                post = post[post.find('마감일') + 13:]

            posts[idx] = post
            data_dates.append({'post_date': post_date, 'end_date': end_date})

        # Replace view count
        post = posts[0]
        post = post.replace('\n', ' ')
        posts[0] = post

        for idx in range(1, len(posts)):
            post = posts[idx]
            elements = post.split(' ')
            elements = elements[2:]
            elements = ['%s ' % x for x in elements]
            elements = ''.join(elements)
            posts[idx] = elements

        # Complete table
        for idx in range(0, len(posts)):
            post = posts[idx]
            elements = post.split(' ')
            post_id = elements[0]
            elements = ['%s ' % x for x in elements]
            post_title = ''.join(elements[1:])
            data_titles.append({'post_id': post_id, 'post_title': post_title})

        data_dates = pd.DataFrame(data_dates)
        data_titles = pd.DataFrame(data_titles)

        return data_dates.merge(data_titles.iloc[: data_dates.shape[0] - 1], left_index=True, right_index=True)

    def sign_in(self):
        self._driver.get(SIGN_IN_URL)
        # self._driver.find_element_by_xpath(SIGN_IN_ID_XPATH).click()
        self._driver.find_element_by_xpath(
            SIGN_IN_ID_XPATH).send_keys(KOREA_AC_KR_ID)

        # self._driver.find_element_by_xpath(SIGN_IN_PW_XPATH).click()
        self._driver.find_element_by_xpath(
            SIGN_IN_PW_XPATH).send_keys(KOREA_AC_KR_PASSWORD)

        self._driver.find_element_by_xpath(SIGN_IN_PROCEED_XPATH).click()
        time.sleep(2)
