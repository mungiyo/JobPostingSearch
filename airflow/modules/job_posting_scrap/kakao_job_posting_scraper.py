import sys
sys.path.append('c:\\Users\\wkdtj\\Desktop\\JobPostingSearch\\air\\modules\\metadata')
import requests
import time
import random
from job_posting import ScrapedObject
from bs4 import BeautifulSoup as bs

def kakao_job_posting_scraping():
    postings = []
    is_first = True
    next_page_url = None

    while True:
        if is_first:
            page = requests.get('https://careers.kakao.com/jobs')
            is_first = False
        else:
            page = requests.get(next_page_url)

        soup = bs(page.text, 'html.parser')
        posting_css_selector = '#mArticle > div > ul.list_jobs > li'
        posting_elements = soup.select(posting_css_selector)

        for element in posting_elements:    # 각 채용 공고에 스크래핑 수행
            # 스크랩하기 전 중복된 데이터인지 확인
            pass

            # 스크래핑된 데이터 정보
            url = 'https://careers.kakao.com' + element.div.div.a['href']
            company = 'kakao'
            title = element.div.div.a.h4.text
            contents_css_selector = '#mArticle > div > div > div.cont_board.board_detail > div'

            # 공고 내용 스크래핑 후 데이터 객체, 리스트에 append
            posting = ScrapedObject(url, company, title, contents_css_selector)
            postings.append(posting)
            
        try: # 페이지 스크래핑
            page_css_selector = '#mArticle > div > div.paging_list > span > a:nth-child(11)'
            page_element = soup.select(page_css_selector)
            next_page_url = 'https://careers.kakao.com' + page_element[0]['href']

        except IndexError:  # 다음 URL이 없을 경우 스크래핑 중지
            break

        time.sleep(random.uniform(2, 4))
    
    print(len(postings))
    
if __name__ == '__main__':
    kakao_job_posting_scraping()