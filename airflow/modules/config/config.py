import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

class Config:
    JOB_POSTINGS = {
        'kakao': {
            'url': 'https://careers.kakao.com/jobs',
            'posting_css_selector': '#mArticle > div > ul.list_jobs > li',
            'posting_contents_css_selector': '#mArticle > div > div > div.cont_board.board_detail > div'
        },
        'line': {
            'url': 'https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia',
            'posting_css_selector': '#container > div.content_w1200 > div.job_result > ul > li',
            'posting_contents_css_selector': '#jobs-contents > div'
        },
        'naver': {
            'url': 'https://recruit.navercorp.com/naver/job/listJson',
            'method': 'POST',
            'data': {
                'classNm': 'developer',
                'startNum': 1,
                'endNum': 1000
            },
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://recruit.navercorp.com/naver/job/list/developer'
            },
        }
    }

    MONGO_HOST = 'localhost'
    MONGO_PORT = '27017'
    MONGO_DB = 'job'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"

class JobPostingRecord:
    url: str
    company: str
    title: str
    contents: str
    scraped_time: datetime

    def __init__(self, url, company, title, contents_css_selector=None, contents=None):
        self.url = url
        self.company = company
        self.title = title
        if contents_css_selector is None:
            self.contents = contents
        else: 
            self.contents = self.set_posting_contents(contents_css_selector)
        self.scraped_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def set_posting_contents(self, posting_contents_css_seletor):  # job posting contents scraping func.
        page = requests.get(self.url)
        soup = bs(page.text, 'html.parser')
        element = soup.select(posting_contents_css_seletor)
        tagged_txt_list = element[0].children   # tag list of HTML document       
        articles = [txt.get_text(' ') for txt in tagged_txt_list] # text list of tagged_text
        contents = ' '.join(articles) # ' ' joined string
        
        return contents
    
    def get_dict_posting(self):
        dict_data = {
            'url': self.url,
            'company': self.company,
            'title': self.title,
            'contents': self.contents,
            'scraped_time': self.scraped_time
        }

        return dict_data