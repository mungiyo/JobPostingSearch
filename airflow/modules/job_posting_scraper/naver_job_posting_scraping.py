import requests
from config import Config, JobPostingRecord

def naver_job_posting_scraping():
    job_postings = []
    url = Config.JOB_POSTINGS['naver']['url']
    method = Config.JOB_POSTINGS['naver']['method']
    data = Config.JOB_POSTINGS['naver']['data']
    headers = Config.JOB_POSTINGS['naver']['headers']

    datas = requests.request(url=url, method=method, data=data, headers=headers).json()
    for data in datas:
        posting = JobPostingRecord(
            url='https://recruit.navercorp.com/naver/job/list/developer/' + str(data['annoId']),
            company='네이버',
            title=data['jobNm'],
            contents=data['jobText']
        )
        job_postings.append(posting)
    
    serialized_data = [posting.get_dict_posting() for posting in job_postings]
    
    return serialized_data