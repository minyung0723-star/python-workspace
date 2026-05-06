'''
인터랙티브 지도를 만들 수 있는 라이브러리
Leaflet.js 기반으로 동작해서 html 파일로 저장하여 사용할 수 있다.
지도 위에 데이터 시각화, 클러스터링, 히트맵 등 가능

설치
pip install folium

* 추가개념
** Leaflet : Folium이 내부적으로 사용하는 지도 엔진
** 클러스터링 : 마커가 너무 많을 때 뭉쳐서 보여주는 것
            예를들어 마커 2799개 -> 그냥 찍으면 지도가 점으로 가득참
                                -> 클러스터링 처리하면 숫자로 묶어서 보여줌
** 히트맵 : 밀집도를 색상으로 표현
            예를 들어 휴게소가 많은 곳 -> 빨갛게 표기
                     휴게소가 적은 곳 -> 파랗게 표기
흐름
folium.Map() 생성
    -> .add_to(변수 = 공간데이터명칭) 으로 추가
      --> 모든 추가가 끝난다면 변수.save("저장할_파일이름.html")

데이터
전국 편의점 / 카페 위치
전국 주유소 위치 / 가격
서울시 따릉이 대여소
전국 공공화장실 위치 등 사용하며 데이터 분석할 수 있다.

csv 데이터를 선택할 때 주의할 점
1. 위도 경도가 컬럼으로 존재하는가?
2. 데이터를 제한없이 다운로드하여 가져올 수 있는가?
'''

import folium

## 1. 지도 생성
### folium 라이브러리에서 Map() 지도 생성 기능 호출
#### 지도생성 기능을 호출해서 지도를 만들 때
##### 중심이 되는 위도 경도 설정, 처음에 시작할 zoom 정도 세팅
m = folium.Map(
    location=[37.5665, 126.9780], # 위도, 경도 (서울)
    zoom_start=12 # zoom level (1 == 지구전체 ~ 18 == 건물 하나)
)

기본타입 = folium.Map(tiles='OpenStreetMap')
밝은타입 = folium.Map(tiles='CartoDB position')
어두운타입 = folium.Map(tiles='CartoDB dark_matter')
위성지도타입 = folium.Map(tiles='Sta,em Terrain')

# 다양한 타입이 존재

## 2. 마커 추가
### folium 라이브러리에서 Marker() 위치 표기 기능 호출
#### 어떤 위치를 표기해야하는지 설정, 클릭하면 보이는 글자, 텍스트 등 팝업 삽입
#### 마우스를 살~짝 올리면 보여질 텍스트 툴팁 추가 folium 에서 제공하는 기본 아이콘 세팅
##### 모든 세팅을 끝낸 결과를 m 공간에 추가하겠다.
folium.Marker(
    location=[37.5665,126.9780],
    popup='서울시청', # 클릭하면 뜨는 팝업
    tooltip='여기를 클릭', # 마우스를 올려두면 뜨는 텍스트
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

## 3. 원형 마커
### 원 둥글기, 원둘레, 색상, 색상채우기 유무, 불투명도 0~1 사이로 설정 가능
#### 마커나 원형마커를 이용해서 범위나 현재 위치 설정
##### 모든 세팅을 끝낸 결과를 m 공간에 추가하겠다.
folium.CircleMarker(
    location=[37.5700,126.9800],
    radius=30,
    color="blue",
    fill=True,
    fill_opacity=0.4
).add_to(m)
# m에 보관된 코드를 참고하여 html 파일을 나의 컴퓨터에 저장하겠다.
m.save('01_map.html')