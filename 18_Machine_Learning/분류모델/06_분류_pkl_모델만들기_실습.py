import pickle
from sklearn.datasets import load_iris, load_wine, load_digits, load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def 참고용코드():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    with open(f"iris_model{acc * 100:.1f}.pkl", "wb") as f:
        pickle.dump(model, f)

    print("모델 저장 완료")
참고용코드()

def 실습_1():
    wine = load_wine()
    X = wine.data
    y = wine.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3) #
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    with open(f"wine_model{acc * 100:.1f}.pkl", "wb") as f:
        pickle.dump(model, f)
# 실습_1()

def 실습_2():
    digits = load_digits()
    X = digits.data
    y = digits.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3) #
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    with open(f"digits_model{acc * 100:.1f}.pkl", "wb") as f:
        pickle.dump(model, f)
# 실습_2()

def 실습_3():
    cancer = load_breast_cancer()
    X = cancer.data
    y = cancer.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3) #
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    with open(f"cancer_model{acc * 100:.1f}.pkl", "wb") as f:
        pickle.dump(model, f)
# 실습_3()
# def 실습_4():
