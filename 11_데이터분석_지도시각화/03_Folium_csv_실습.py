import pandas as pd
import folium
from folium.plugins import MarkerCluster



def 주유소_지도():
    df = pd.read_csv('데이터실습파일/서울특별시_중랑구_주유소_20260213.csv')
    # todo 1 : CSV 파일 읽기
    # 힌트 : read_excel 이 아니라 read_csv 를 사용하시면 됩니다.
    #        엑셀처럼 skiprows, header=None 없어도 컬럼명이 자동으로 잡힙니다.
    print(df.columns)
    # todo 2 : 컬럼명 확인하기
    # 힌트 : print(df.columns) 로 찍어보시고
    #        위도, 경도 컬럼 이름이 정확히 뭔지 확인하세요.
    df = df.dropna(subset=["위도","경도"])
    # todo 3 : 위도 경도 NaN 있는 행 제거
    # 힌트 : dropna(subset=[...]) 오늘 배운 것 그대로 사용하시면 됩니다.
    #        컬럼명만 todo 2 에서 확인한 이름으로 바꿔주세요.
    map = folium.Map(location=[37.6063, 127.0928], zoom_start=12)
    # todo 4 : 지도 생성
    # 힌트 : 중랑구 중심 위도경도는 37.6063, 127.0928 입니다.
    #        zoom_start 는 본인이 원하는 숫자로 설정해보세요.
    cluster = MarkerCluster().add_to(map)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["위도"], row["경도"]]
        ).add_to(cluster)
    # todo 5 : 클러스터링으로 마커 찍기
    # 힌트 : MarkerCluster 와 iterrows 오늘 배운 것 그대로입니다.
    map.save("주유소지도.html")
    # todo 6 : html 파일로 저장
    # 힌트 : m.save("주유소지도.html")
# 주유소_지도()

def 공중화장실_지도():
    df = pd.read_csv('데이터실습파일/공중화장실정보.csv', encoding='cp949')
    print(df.columns)

    df = df.dropna(subset=['WGS84위도', 'WGS84경도'])
    map = folium.Map(location=[36.5, 127.5], zoom_start=7)

    cluster = MarkerCluster().add_to(map)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["WGS84위도"], row["WGS84경도"]],
            popup=row["화장실명"]
        ).add_to(cluster)

    map.save("화장실지도.html")
공중화장실_지도()