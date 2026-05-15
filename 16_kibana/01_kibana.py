"""
Kibana 를 실행하기 위해서는 반드시
docker - Elasticsearch + Kibana 실행

"""

'''
ELK(Logstash + Elasticsearch + kibana)

[프로젝트 = 애플리케이션 로그]
            ↓
         Logstash
      (로그 수집/가공)
            ↓
      Elasticsearch
    (데이터 저장/검색)
            ↓
         Kibana
      (조회/시각화)


주요 기능
- Discover   로그 검색
- Dashboard  화면 구성
- Lens       그래프 생성
- Maps       지도 시각화
- Dev Tools  Elasticsearch 쿼리 테스트

Index Pattern(Data View)
- 예전에는 Index Pattern 요즘 Kibana 에서는 Data View 라고 많이 부름
- Elasticsearch 의 인덱스를 Kibana 가 읽을 수 있게 연결해주는 설정
'''

"""
Index Pattern 생성
순서
1) kibana 

2) 메뉴이동

3) 입력
Name:
logs-view

Index Pattern
logs-*

4) Time Field 선택
보통 @timestamp 선택

5) Discover 사용법
- Discover 로그 검색 화면
- Analytics → Discover
- 기본검색하면
    {
    "level":"ERROR",
    "message":"DB Connection Fail",
    "service":"user-api"
    }
6) KQL(Kibana Query Language)
기본 문법
- 전체      조회 = *
- 특정 필드 검색 = level:"ERROR"
- AND  조     건 = level:"ERROR" AND service:"user-api"
- OR   조     건 = level:"ERROR" OR level:"WARN"
- NOT  조     건 = "INFO"
- 포  함   검 색 = message:"*Fail*"
"""