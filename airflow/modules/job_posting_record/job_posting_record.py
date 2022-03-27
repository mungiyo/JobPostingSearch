import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

class JobPostingRecord:
    url: str
    company: str
    title: str
    contents: str
    crawled_time: datetime

    def __init__(self, url, company, title, contents_css_selector):
        self.url = url
        self.company = company
        self.title = title
        self.contents = self.set_posting_contents(contents_css_selector)
        self.crawled_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
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
            'crawled_time': self.crawled_time
        }

        return dict_data