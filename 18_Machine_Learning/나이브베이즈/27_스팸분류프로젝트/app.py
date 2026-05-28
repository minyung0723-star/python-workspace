"""
실습 과제 : 스팸 문자 분류기 - Flask 웹 서버
train_model.py 실행 후 생성된 pkl 파일명을 아래에 맞춰 수정하세요
"""

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# ================================
# 모델 불러오기
# train_model.py 실행 후 생성된 파일명으로 수정!
# ================================

# TODO 1: pkl 파일 열어서 saved 변수에 담기
with open('spam_model_???.pkl', '___') as f:
    saved = pickle.___(___)

# TODO 2: saved 딕셔너리에서 model 과 vectorizer 꺼내기
model      = saved[___]
vectorizer = saved[___]


@app.route("/")
def 메인페이지():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def 예측하기():
    # TODO 3: 폼에서 'message' 라는 이름으로 입력값 받기
    message = request.form.get(___)

    # TODO 4: vectorizer 로 변환 (힌트: transform, fit 아님!)
    vec  = vectorizer.___([___])

    # TODO 5: model 로 예측
    결과 = model.predict(___)[0]    # 'spam' or 'ham'

    # TODO 6: 확률 계산 (더 높은 쪽 확률 %)
    확률 = round(max(model.predict_proba(vec)[0]) * 100, 1)

    return render_template('index.html', 결과=결과, 확률=확률, 메시지=message)


if __name__ == "__main__":
    app.run(debug=True)