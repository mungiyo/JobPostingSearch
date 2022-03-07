import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

class JobPostingRecord:
    url: str                # 해당 url
    company: str            # 회사
    title: str              # 제목
    contents: str           # 내용
    scraped_time: datetime  # 스크랩된 시간

    def __init__(self, url, company, title, contents_css_selector):
        self.url = url
        self.company = company
        self.title = title
        self.contents = self.set_posting_contents(contents_css_selector)
        self.scraped_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def set_posting_contents(self, posting_contents_css_seletor):  # 채용 공고의 내용 스크래핑 함수
        page = requests.get(self.url)
        soup = bs(page.text, 'html.parser')
        element = soup.select(posting_contents_css_seletor)
        tagged_txt_list = element[0].children   # HTML 문서의 태그들의 리스트
        
        articles = [txt.get_text('|').replace('  ', '').replace('\n', '')
                    for txt in tagged_txt_list
                    if txt != '\n'] # doc의 각 태그들에서 전처리 한 텍스트들의 리스트

        contents = '\n'.join(articles) # '\n'으로 하나의 문자열로 생성
        
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