# Q1. 역색인(Inverted Index)이 일반 색인보다 검색이 빠른 이유를 한 문장으로 설명해 보세요.
# 답: 색인은 필요한 키워드를 모든 파일에서 일일히 확인후 찾아서 검색하지만 역색인은 키워드로 묶어서 문서를 보관하다가 찾기 때문에 더 빠르다
#
# Q2. Elasticsearch의 Index / Document / Field 를 RDB 용어로 각각 뭐라고 부르나요?
# 답: Index = Table , Document = Row , Field = column
#
# Q3. match 검색과 term 검색의 차이는 무엇인가요? (힌트: 형태소 분석)
# 답: match 검색은 형태소 분석을 거쳐서 검색이 되는 것이고
#     term 검색은 형태소 분석 없이 검색이 되는 차이가 있다
#
# Q4. docker compose down 과 docker compose stop 의 차이는 무엇인가요?
# 답: docker compose down은 컨테이너 중지 삭제이고 docker compose stop은 삭제하지 않고 중지만 한다