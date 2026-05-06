import folium

### 서울특별시 종로구 관철동 위도 경도를 검색하여 위치 설정하거나
#### 나의 동네 위도 경도로 변경해서 진행
# TODO 1. 지도 만들기 (내 동네 위도/경도로 바꿔보기)
m = folium.Map(
    location=[37.587379, 127.209414],  # 위도, 경도
    zoom_start=12       # 동네 보기 좋은 줌 레벨
)

# TODO 2. 첫 번째 카페 마커
folium.Marker(
    location=[37.585706, 127.211922],
    popup='obo',   # 카페 이름
    tooltip='오비오'  # 마우스 올렸을 때 텍스트
).add_to(m)

# TODO 3. 두 번째 카페 마커
folium.Marker(
    location=[37.585845, 127.211775],
    popup='stay alive',
    tooltip='스테이얼라이브 카페'
).add_to(m)

# TODO 4. 세 번째 카페 마커
folium.Marker(
    location=[37.586257, 127.212299],
    popup='megacoffie',
    tooltip='메가커피'
).add_to(m)

# TODO 5. 저장
m.save('myLocationMap.html')  # 파일 이름