import json
from datetime import datetime

class ScrapedObject:
    url: str                # 해당 url
    company: str            # 회사
    title: str              # 제목
    contents: str           # 내용
    scraped_time: datetime  # 스크랩된 시간

    def __init__(self, url, company, title, contents):
        self.url = url
        self.company = company
        self.title = title
        self.contents = contents
        self.scraped_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def get_json_contents(self):
        dict_data = {
            'url': self.url,
            'company': self.company,
            'title': self.title,
            'contents': self.contents,
            'scraped_time': self.scraped_time
        }

        json_string = json.dumps(dict_data, ensure_ascii=False)

        return json_string