import requests
import time
import random
from bs4 import BeautifulSoup as bs
from config import Config, JobPostingRecord

def line_job_posting_scraping():
    job_postings = []
    page_url = Config.JOB_POSTINGS['line']['url']
    posting_css_selector = Config.JOB_POSTINGS['line']['posting_css_selector']
    posting_contents_css_selector = Config.JOB_POSTINGS['line']['posting_contents_css_selector']

    rep = requests.get(page_url)
    soup = bs(rep.text, 'html.parser')
    posting_elements = soup.select(posting_css_selector)

    for element in posting_elements:
        # scraped data info.
        url = 'https://careers.linecorp.com' + element.a['href']
        company = 'line'
        title = element.a.h3.text
        region = element.a.div.span.text
        
        if not (region in ("Seoul", "Bundang")): continue

        # after contents scarping, append to posting list
        posting = JobPostingRecord(url, company, title, posting_contents_css_selector)
        job_postings.append(posting)

        time.sleep(random.uniform(1, 2))    # 1 ~ 2 seconds sleep
    
    serialized_data = [posting.get_dict_posting() for posting in job_postings]

    return serialized_data