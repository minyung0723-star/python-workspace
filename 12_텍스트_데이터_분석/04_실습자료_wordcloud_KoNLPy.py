import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter

text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""

def 실습1():

    wc = WordCloud()

    text = """
    Python machine learning data science artificial intelligence
    deep learning neural network programming code development
    algorithm model training dataset feature engineering
    """

def 실습2():
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='plasma'
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('wordcloud.png',dpi=150)
    plt.show()

text = """
game player character level skill attack defense magic sword shield
warrior mage archer knight paladin ranger assassin monk wizard priest
quest dungeon boss monster enemy battle victory defeat reward experience
item weapon armor potion gold treasure map village castle dragon
team strategy strength speed agility intelligence stamina power ability
"""

def 실습3():
    wc = WordCloud(
        background_color='black',
        width=1000,
        height=500,
        max_words=50
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def 실습4():

    colormaps = ['plasma','inferno','cool']
    plt.figure(figsize=(15, 5))

    for i, cmap in enumerate(colormaps):
        wc = WordCloud(
            colormap=cmap
        ).generate(text)
        plt.subplot(1, 3, i + 1)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(cmap)
    plt.tight_layout()
    plt.show()

def 실습5():
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)
    wc.to_file("wc_file.png")

def 실습6_형태소분석():
    okt = Okt()
    text = "나는 파이썬으로 자연어 처리를 공부하고 있어요"
    print(okt.morphs(text))
    print(okt.nouns(text))
    print(okt.morphs(text,stem=True))

def 실습7_wordcloud연결():
    text = """
    파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
    데이터 과학자들은 파이썬으로 딥러닝 모델을 학습시킵니다.
    자연어 처리와 컴퓨터 비전 분야에서도 파이썬이 인기입니다.
    인공지능 시대에 데이터 분석 능력은 매우 중요합니다.
    """
    okt = Okt()

    nouns = okt.nouns(text)

    stopwords = {'것', '수', '등', '및', '더', '이', '그', '저', '때', '년', '들'}

    filtered = [w for w in nouns if w not in stopwords and len(w) > 1]

    # TODO: Counter 로 단어 빈도 계산
    counts = Counter(filtered)

    # TODO: 한글 폰트 경로 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    wc = WordCloud(
        font_path = font_path,
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='Set2'
    # TODO: 빈도 딕셔너리로 WordCloud 생성
    ).generate_from_frequencies(counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    # TODO: 'korean_wordcloud.png' 저장, dpi=150
    plt.savefig('korean_wordcloud.png', dpi=150)
    plt.show()

실습1()
실습2()
실습3()
실습4()
실습5()
실습6_형태소분석()
실습7_wordcloud연결()
