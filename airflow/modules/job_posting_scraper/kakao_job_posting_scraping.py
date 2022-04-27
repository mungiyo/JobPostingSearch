import requests
import time
import random
from bs4 import BeautifulSoup as bs
from config import Config, JobPostingRecord

def kakao_job_posting_scraping():
    job_postings = []
    next_page_url = Config.JOB_POSTINGS['kakao']['url'] + '?page='
    posting_css_selector = Config.JOB_POSTINGS['kakao']['posting_css_selector']
    contents_css_selector = Config.JOB_POSTINGS['kakao']['contents_css_selector']
    page_num = 1

    while True:
        rep = requests.get(next_page_url + str(page_num), allow_redirects=False)
        if rep.status_code == 302: break
        soup = bs(rep.text, 'html.parser')
        posting_elements = soup.select(posting_css_selector)
        
        for element in posting_elements:
            # scraped data info.
            url = 'https://careers.kakao.com' + element.div.div.a['href']
            company = '카카오'
            title = element.div.div.a.h4.text

            # after contents scarping, append to posting list
            posting = JobPostingRecord(
                url=url,
                company=company,
                title=title,
                contents_css_selector=contents_css_selector
            )
            job_postings.append(posting)
            
            time.sleep(random.uniform(1, 2))    # 1 ~ 2 seconds sleep
            
        page_num += 1
    
    serialized_data = [posting.get_dict_posting() for posting in job_postings]

    return serialized_data