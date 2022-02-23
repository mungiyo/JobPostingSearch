import requests
import time
import pprint
from bs4 import BeautifulSoup as bs
from config.DataObject import ScrapedObject

target = 'https://careers.kakao.com/jobs?page=1'

def contents_scraping(url):    # 채용 공고의 내용 스크래핑 함수
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    element = soup.select('#mArticle > div > div > div.cont_board.board_detail > div')
    doc = element[0].children   # HTML 문서의 태그들의 리스트
    articles = [d.get_text('|').replace('  ', '').replace('\n', '')
                for d in doc
                if d != '\n'] # doc의 각 태그들에서 전처리 한 텍스트들의 리스트
    contents = '\n'.join(articles) # '\n'으로 하나의 문자열로 생성

    return contents

def kakao_job_posting_scraping(target):
    page = requests.get(target)
    soup = bs(page.text, 'html.parser')

    elements = soup.select('#mArticle > div > ul.list_jobs > li')

    for element in elements:
        # 스크랩하기 전 중복된 데이터인지 확인
        pass

        # 스크래핑된 데이터 정보
        url = 'https://careers.kakao.com' + element.div.div.a['href']
        company = '카카오'
        title = element.div.div.a.h4.text
        contents = contents_scraping(url)

        # 스크래핑된 데이터 객체 -> json 형식으로 변환
        data = ScrapedObject(url, company, title, contents)
        data_json = data.get_json_contents()
        # pprint.pprint(data_json)
        
        time.sleep(1)

if __name__ == '__main__':
    kakao_job_posting_scraping(target)