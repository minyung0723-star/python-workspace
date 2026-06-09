from transformers import pipeline, ElectraForSequenceClassification, ElectraTokenizer, MarianTokenizer

"""
pipeline = 허깅페이스가 만든 올인원 간편 도구
            딥러닝의 복잡한 과정을 한 줄로 처리해줌
내부적으로 토크나이저 + 모델 + 모델후처리를 자동으로 알아서 다 해줌

ElectraForSequenceClassification = 어떤 구조의 신경망을 사용할 것인가
 Electra For SequenceClassification
 모델종류 + 하고 싶은 직업
 
 AI 에게 각자 컴퓨터 사양 전달
 작업관리자 → 성능 화면 캡쳐 프롬프트 전달
 만들고 싶은 ai 목표 얘기
 내 컴퓨터 사양해서 할 수 있는 방법 알려줘
"""
# 1. 한국어 감정분석
def 한국어감정분석():
    모델이름 = "monologg/koelectra-base-finetuned-sentiment"

    # 모델과 토크나이저를 명시적으로 호출
    토크나이저 = ElectraTokenizer.from_pretrained(모델이름)
    모델 = ElectraForSequenceClassification.from_pretrained(모델이름)

    분석모델 = pipeline(
        "sentiment-analysis",
        model = 모델,
        device=0, # GPU 사용 device=-1 CPU 사용
        tokenizer=토크나이저
    )
    print(분석모델("이 영화 진짜 최고야!!!"))


# 2. 번역
def 번역():
    번역모델 = pipeline(
        "translation_ko_to_en",
        model="Helsinki-NLP/opus-mt-ko-en",
        device=0
    )

    print(번역모델("안녕하세요. 반갑습니다."))


def 번역_2():
    모델선택 = "Helsinki-NLP/opus-mt-ko-en"

    토크나이저 = MarianTokenizer.from_pretrained(모델선택)
    모델 = MarianTokenizer.from_pretrained(모델선택)
    글자 = "안녕하세요. 반갑습니다."
    # 토크나이징
    inputs = 토크나이저(글자, return_tensors='pt',padding=True)

    # 번역 생성
    translated = 모델.generate(**inputs)

    # 디코딩
    result = 토크나이저.decode(translated[0], skip_special_tokens=True)
    print(result)

def 이미지분류():
    분류모델 = pipeline(
        "image-classification",
        model='google/vit-base-patch16-224',
        device=0
    )
번역_2()