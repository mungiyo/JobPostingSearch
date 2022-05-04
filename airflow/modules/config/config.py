import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

class JobPostingRecord:
    url: str
    company: str
    title: str
    career: str
    contents_css_selector: str
    contents: str
    scraped_time: datetime

    def __init__(self, url, company, title, career=None, contents_css_selector=None, contents=None):
        self.url = url
        self.company = company
        self.title = title
        self.career = career
        if contents_css_selector is None:
            soup = bs(contents, 'html.parser')
            self.contents = soup.get_text()
        else:
            self.contents = self.set_posting_contents(contents_css_selector)
        self.scraped_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def set_posting_contents(self, posting_contents_css_seletor):  # job posting contents scraping func.
        page = requests.get(self.url)
        soup = bs(page.content, 'html.parser', from_encoding='utf-8')
        element = soup.select(posting_contents_css_seletor)
        contents = element[0].get_text()
        
        return contents
    
    def get_dict_posting(self):
        dict_data = {
            'url': self.url,
            'company': self.company,
            'title': self.title,
            'career': self.career,
            'contents': self.contents,
            'scraped_time': self.scraped_time
        }

        return dict_data

class Config:
    JOB_POSTINGS = {
        'kakao': {
            'url': 'https://careers.kakao.com/jobs',
            'posting_css_selector': '#mArticle > div > ul.list_jobs > li',
            'contents_css_selector': '#mArticle > div > div > div.cont_board.board_detail > div'
        },
        'line': {
            'url': 'https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia',
            'posting_css_selector': '#container > div.content_w1200 > div.job_result > ul > li',
            'contents_css_selector': '#jobs-contents > div'
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
        },
        'nexon': {
            'url': 'https://career.nexon.com/user/recruit/member/postList?joinCorp=NX&jobGroupCd=22&reSubj=',
            'posting_css_selector': '#frmMain > fieldset > div.wrapPostGroup > ul > li',
            'contents_css_selector': '#frmMain > div > div.detailContents'
        }
    }

    MONGO_HOST = 'mongo'
    MONGO_PORT = '27017'
    MONGO_DB = 'job'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"