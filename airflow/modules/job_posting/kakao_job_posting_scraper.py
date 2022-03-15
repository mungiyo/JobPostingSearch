import requests
import time
import random
from config import JobPostingRecord, Config
from bs4 import BeautifulSoup as bs

def kakao_job_posting_scraping():
    job_postings = []
    next_page_url = Config.JOB_POSTINGS['kakao']['url']
    posting_css_selector = Config.JOB_POSTINGS['kakao']['posting_css_selector ']
    contents_css_selector = Config.JOB_POSTINGS['kakao']['contents_css_selector']
    page_css_selector = Config.JOB_POSTINGS['kakao']['page_css_selector']

    while True:
        page = requests.get(next_page_url)
        soup = bs(page.text, 'html.parser')
        posting_elements = soup.select(posting_css_selector)

        for element in posting_elements:
            # 스크래핑된 데이터 정보
            url = 'https://careers.kakao.com' + element.div.div.a['href']
            company = 'kakao'
            title = element.div.div.a.h4.text

            # 공고 내용 스크래핑 후 데이터 객체, 리스트에 append
            posting = JobPostingRecord(url, company, title, contents_css_selector)
            job_postings.append(posting.get_dict_posting())

            time.sleep(random.uniform(1, 2))
            
        try: # 페이지 스크래핑
            page_element = soup.select(page_css_selector)
            next_page_url = 'https://careers.kakao.com' + page_element[0]['href']

        except IndexError:  # 다음 URL이 없을 경우 스크래핑 중지
            break

        time.sleep(random.uniform(1, 2))
    
    return job_postings