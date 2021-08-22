# Job posting scrapper
- For personal use

## How it works

<p align="center">
    <img src="https://github.com/hyeon95y/job_posting_scrapper/blob/main/class_diagram.png" width=600px>
</p>

- Get job posts containing predefined keywords from following sources
    - NAVER Cafe
    - job.korea.ac.kr
- Process above runs perodically by Airflow scheduler
- Store scrapped job posting at DB
- Send alert via messagner if any post newly stored at DB is previously unseen

## Prerequisites

```
$ direnv allow
$ pip install -r requirements
```

For any kind of editing
```
$ pre-commit install 
$ pytest tests
```



