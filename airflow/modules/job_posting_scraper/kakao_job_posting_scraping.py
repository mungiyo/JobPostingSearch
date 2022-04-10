import requests
import time
import random
from bs4 import BeautifulSoup as bs
from config import Config
from job_posting_record import JobPostingRecord

def kakao_job_posting_scraping():
    job_postings = []
    next_page_url = Config.JOB_POSTINGS['kakao']['url']
    posting_css_selector = Config.JOB_POSTINGS['kakao']['posting_css_selector']
    posting_contents_css_selector = Config.JOB_POSTINGS['kakao']['posting_contents_css_selector']
    page_css_selector = Config.JOB_POSTINGS['kakao']['page_css_selector']

    while True:
        page = requests.get(next_page_url)
        soup = bs(page.text, 'html.parser')
        posting_elements = soup.select(posting_css_selector)

        for element in posting_elements:
            # scraped data info.
            url = 'https://careers.kakao.com' + element.div.div.a['href']
            company = 'kakao'
            title = element.div.div.a.h4.text

            # after contents scarping, append to posting list
            posting = JobPostingRecord(url, company, title, posting_contents_css_selector)
            job_postings.append(posting)

            time.sleep(random.uniform(1, 2))    # 1 ~ 2 seconds sleep
            
        try: # page scraping
            page_element = soup.select(page_css_selector)
            next_page_url = 'https://careers.kakao.com' + page_element[0]['href']

        except IndexError:  # no next url, while break
            break

        time.sleep(random.uniform(1, 2))    # 1 ~ 2 seconds sleep
    
    serialized_data = [posting.get_dict_posting() for posting in job_postings]

    return serialized_data