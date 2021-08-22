# Job posting scrapper
- For personal use
- Get job posts containing predefined keywords from following sources and store it to DB
    - NAVER Cafe
    - job.korea.ac.kr
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



