from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]          # mydb 말고 library DB 새로 만들기
col_members = db["members"]     # 회원 컬렉션
col_books = db["books"]         # 도서 컬렉션
col_loans = db["loans"]         # 대출 컬렉션


def 회원등록():
    회원1명 = col_members.insert_one(
        {"name":"홍길동", "age":28, "city":"서울", "grade":"일반", "tags":["소설","역사"]}
    )
    print("회원1명 저장 결과 확인 : ", 회원1명.inserted_id)
    회원여러명 = col_members.insert_many([
        {"name":"김도서", "age":35, "city":"부산", "grade":"VIP", "tags":["IT","자기계발"]},
        {"name":"이열람", "age":22, "city":"서울", "grade":"일반", "tags":["소설","만화"]},
        {"name":"박반납", "age":41, "city":"대구", "grade":"VIP", "tags":["역사","철학"]},
        {"name":"최연체", "age":19, "city":"서울", "grade":"정지", "tags":["만화"]}
    ])
    print("회원여러명 저장 결과 확인 : ", 회원여러명.inserted_ids)
# 회원등록()
def 도서등록():
    도서여러개 = col_books.insert_many([
        {"title":"파이썬 기초", "author":"김코딩", "price":25000, "pub_year":2024, "stock":5,"tags":["IT","프로그래밍"]},
        {"title":"세계사 한눈에", "author":"이역사", "price":18000, "pub_year":2023, "stock":3,"tags":["역사","교양"]},
        {"title":"자바스크립트 완전정복", "author":"박프론트", "price":32000, "pub_year":2025, "stock":2,"tags":["IT","프로그래밍"]},
        {"title":"철학의 시작", "author":"최철학", "price":21000, "pub_year":2022, "stock":7,"tags":["철학","교양"]},
        {"title":"만화로 보는 과학", "author":"정만화", "price":15000, "pub_year":2024, "stock":10,"tags":["만화","과학"]}
    ])
    print("도서여러개 저장 결과 확인 : ", 도서여러개.inserted_ids)
# 도서등록()

def 대출등록():
    대출1건 = col_loans.insert_one(
        {"member_name":"홍길동", "title":"파이썬 기초", "is_returned":False, "comments":[], "loan_date":datetime.now()}
    )
    print("대출1건 저장 결과 확인 : ", 대출1건.inserted_id)
    대출여러건 = col_loans.insert_many([
        {"member_name":"김도서", "title":"세계사 한눈에", "is_returned":True, "comments":[{"writer":"사서","text":"정상반납"}], "loan_date":datetime.now()},
        {"member_name":"이열람", "title":"만화로 보는 과학", "is_returned":False, "comments":[], "loan_date":datetime.now()},
        {"member_name":"최연체", "title":"철학의 시작", "is_returned":False, "comments":[{"writer":"사서","text":"연체중 연락요망"}], "loan_date":datetime.now()}
    ])
    print("대출여러건 저장 결과 확인 : ", 대출여러건.inserted_ids)
# 대출등록()

def members조회():
    # 1.
    for doc in col_members.find():
        print("전체 조회 : ", doc)
    # 2.
    for doc in col_members.find({"city":"서울"}):
        print(f"도시가 서울인 회원 : {doc}")
    # 3.
    for doc in col_members.find_one({"grade":"VIP"}):
        print(f"grade가 VIP 인 회원 한 건 조회 : {doc}")
    # 4.
    for doc in col_members.find().sort("age",1):
        print(f"나이 기준 오름차순 정렬 조회 : {doc}")
    # 5
    for doc in col_members.find({"age": {"$gte": 20, "$lte": 40}}):
        print(f"나이가 20 이상 40 이하인 회원 조회 : {doc}")
    # 6.
    for doc in col_members.find({},{"_id":0, "name":1, "age":1,"grade":1}):
        print(f"이름, 나이, grade 필드만 보기 : {doc}")
    # 7.
    count = col_members.count_documents({"city":"서울"})
    print(f"도시가 서울인 회원수 : {count}")
    # 8.
    exists = col_members.find({"grade":"정지"}) is not None
    print(exists)
    # 9.
    for doc in col_members.find().sort("age",1).limit(2):
        print(f"나이가 낮은 회원 2명만 조회 : {doc}")
    # 10.
    for doc in col_members.find({"tags":"IT"}):
        print(f"tags에 IT 가 포함된 회원 : {doc}")
# members조회()

def books조회():
    # 1.
    for doc in col_books.find():
        print("전체 조회 : ", doc)
    # 2.
    for doc in col_books.find({"price":{"&gte":20000}}):
        print(f"가격이 20000 이상인 도서 : {doc}")
    # 3.
    for doc in col_books.find().sort("pub_year",1):
        print(f"pub_year기준 최신순 정렬 조회 : {doc}")
    # 4.
    for doc in col_books.find_one({}, sort=[("price", -1)]):
        print(f"가장 비싼 도서 1권만 조회 : {doc}")
    # 5.
    for doc in col_books.find({},{"_id":0, "title":1, "price":1,"stock":1}):
        print(f"제목, 가격, 개수 필드만 보기 : {doc}")
    # 6.
    for doc in col_books.find({"stock":{"$lte":5}}):
        print(f"stock이 5 이하인 도서 수 세기 : {doc}")
    # 7.
    # 8.
    # 9.
    # 10.

# def loans조회():
#     # 1.
#     # 2.
#     # 3.
#     # 4.
#     # 5.
#     # 6.
#     # 7.
#     # 8.
#     # 9.
#     # 10.




















