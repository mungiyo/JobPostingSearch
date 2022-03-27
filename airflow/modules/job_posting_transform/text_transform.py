from konlpy.tag import Okt

def text_transform(**context):
    okt = Okt()
    job_postings = context['ti'].xcom_pull(task_ids='job_posting_crawling')

    for posting in job_postings:
        tokenized_text = [word[0] for word in okt.pos(posting['contents'])]
        posting['contents'] = ' '.join(tokenized_text)
    
    return job_postings