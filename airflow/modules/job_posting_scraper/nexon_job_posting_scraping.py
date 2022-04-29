import requests
import time
import random
from bs4 import BeautifulSoup as bs
from config import Config, JobPostingRecord

def nexon_job_posting_scraping():
    job_postings = []
    next_page_url = Config.JOB_POSTINGS['nexon']['url'] + '&currentPage='
    posting_css_selector = Config.JOB_POSTINGS['nexon']['posting_css_selector']
    contents_css_selector = Config.JOB_POSTINGS['nexon']['contents_css_selector']
    flag = True
    currentPage = 0

    while flag:
        rep = requests.get(next_page_url + str(currentPage), allow_redirects=False)
        soup = bs(rep.text, 'html.parser')
        posting_elements = soup.select(posting_css_selector)
      
        for element in posting_elements:
            # scraped data info.
            try:
                url = 'https://career.nexon.com' + element.a['href']
                company = '넥슨'
                title = element.a.dl.dt.text
                career = element.a.dl.find('dd', 'career').span.text
                
                # after contents scarping, append to posting list
                posting = JobPostingRecord(
                    url=url,
                    company=company,
                    title=title,
                    career=career,
                    contents_css_selector=contents_css_selector
                )
                job_postings.append(posting)
                
                time.sleep(random.uniform(0, 1))    # 1 ~ 2 seconds sleep
            
            except:
                flag = False
            
        currentPage += 1
    
    serialized_data = [posting.get_dict_posting() for posting in job_postings]

    return serialized_data