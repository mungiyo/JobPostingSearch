class Config:
    JOB_POSTINGS = {
        'kakao': {
            'url': 'https://careers.kakao.com/jobs',
            'posting_css_selector': '#mArticle > div > ul.list_jobs > li',
            'posting_contents_css_selector': '#mArticle > div > div > div.cont_board.board_detail > div',
            'page_css_selector': '#mArticle > div > div.paging_list > span > a:nth-child(11)'
        }
    }