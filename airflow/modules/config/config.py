class Config:
    JOB_POSTINGS = {
        'kakao': {
            'url': 'https://careers.kakao.com/jobs',
            'posting_css_selector': '#mArticle > div > ul.list_jobs > li',
            'posting_contents_css_selector': '#mArticle > div > div > div.cont_board.board_detail > div',
            'page_css_selector': '#mArticle > div > div.paging_list > span > a:nth-child(11)'
        },
        'line': {
            'url': 'https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia',
            'posting_css_selector': '#container > div.content_w1200 > div.job_result > ul > li',
            'posting_contents_css_selector': '#jobs-contents > div'
        }
    }

    MONGO_HOST = 'localhost'
    MONGO_PORT = '27020'
    MONGO_DB = 'job'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?replicaSet=replication&readPreference=primary&directConnection=true&ssl=false"