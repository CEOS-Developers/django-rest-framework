# Django Rest Framework 과제

## 유의사항
- 이미 있는 db.sqlite3에 예시 데이터가 들어있으므로 DB는 변경하지 않고 사용하도록 합니다.
- [django 공식 도큐먼트](https://docs.djangoproject.com/ko/2.2/)와 [drf 공식 도큐먼트](https://www.django-rest-framework.org/)를 참조해서 주어진 api를 구현하시면 됩니다.

## 구현 스펙
1. 모든 'Post'의 list를 가져오는 API
    - url: `api/posts/`
    - method: `GET`
 
    결과 예시)
    ```
    [
        {
            "id": 1,
            "comment": [
                1,
                2,
                3
            ],
            "text": "예시 포스트1",
            "likes_count": 123,
            "created_at": "2019-09-30T00:12:54.190364+09:00",
            "updated_at": "2019-09-30T00:12:54.190393+09:00"
        },
        {
            "id": 2,
            "comment": [
                4,
                5
            ],
            "text": "예시 포스트2",
            "likes_count": 22,
            "created_at": "2019-09-30T00:17:59.223263+09:00",
            "updated_at": "2019-09-30T00:17:59.223329+09:00"
        },
        {
            "id": 3,
            "comment": [
                6,
                7
            ],
            "text": "예시 포스트3",
            "likes_count": 54,
            "created_at": "2019-09-30T00:18:30.796290+09:00",
            "updated_at": "2019-09-30T00:18:30.796335+09:00"
        }
    ]
    ``` 

2. 새로운 'Post'를 create 하도록 요청하는 API
- text 값을 담아 보내면 해당 값을 text field에 저장하고 있는 Post 생성
    - url: `api/posts/`
    - method: `POST`
    - body: `{"text": "새로운 post"}`
    

## Tip
https://www.django-rest-framework.org/api-guide/generic-views/
https://www.django-rest-framework.org/api-guide/serializers/ 