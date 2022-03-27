class Config:
    JOB_POSTINGS = {
        'kakao': {
            'url': 'https://careers.kakao.com/jobs',
            'posting_css_selector': '#mArticle > div > ul.list_jobs > li',
            'posting_contents_css_selector': '#mArticle > div > div > div.cont_board.board_detail > div',
            'page_css_selector': '#mArticle > div > div.paging_list > span > a:nth-child(11)'
        }
    }

    MONGO_HOST = 'localhost'
    MONGO_PORT = '27017'
    MONGO_DB = 'test'
    MONGO_USER = 'root'
    MONGO_PASSWORD = 'password'
    MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"