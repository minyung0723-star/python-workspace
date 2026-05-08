from os.path import exists

from pymongo import MongoClient
from datetime import datetime
client = MongoClient("mongodb://localhost:27017/")
db = client['mydb']
col_books = db['books']
col_products = db['products']
col_posts = db['posts']

def insert_문제1번():
    단행본1권 = col_books.insert_one(
        {"title": "파이썬 완전정복", "author": "김코딩", "price": 28000, "pub_year": 2024}
    )
    print("단행본 1권 저장 결과 확인 : ", 단행본1권.inserted_id)
    도서3권 = col_books.insert_many([
        {"title": "mongoDB 바이블", "author": "이데이터", "price": 35000, "pub_year": 2023},
        {"title": "자바스크립트 입문", "author": "박프론트", "price": 22000, "pub_year": 2025},
        {"title": "리눅스 실전", "author": "최서버", "price": 19000, "pub_year": 2022}
    ])
    print("도서 3권 저장 결과 확인 : ", 도서3권.inserted_ids)

# insert_문제1번()
def insert_문제2번():
    결과 = col_products.insert_many([
        {"product_name" : "무선 마우스", "price":35000, "stock":100, "tags": ["전자기기", "컴퓨터"]},
        {"product_name" : "맨투맨 티셔츠", "price":45000, "stock":50, "options": {"color":["검정","흰색","회색"], "size": ["S","M","L","XL"]}},
        {"product_name" : "블루투스 이어폰", "price":89000, "stock":30, "sale_price": 71200, "discount_rate":20}
    ])
    print("상품 3개 저장 결과 확인 : ", 결과.inserted_ids)
# insert_문제2번()

def insert_문제3번():
    게시물1 = col_posts.insert_one(
        {"author":"김개발", "content":"오늘 mongoDB 공부 시작!", "likes":0,"created_at":datetime.now()}
    )
    print("게시물 1개 저장 결과 확인 : ", 게시물1.inserted_id)

    게시물여러개 = col_posts.insert_many([
        {"author":"이몽고" , "content":"맛집 발견" , "images":["img1.jpg","img2.jpg","img3.jpg"] , "likes":0 , "comments":[] , "created_at":datetime.now()},
        {"author":"박클라" , "content":"주말 코딩중" , "hashtags":["개발","파이썬","mongoDB"] , "likes":5,
            "comments":[{"writer":"최데이", "text":"멋지다!"},{"writer":"김개발", "text":"나도 공부해야지"}]}
    ])
    print("개시물 여러개 저장 결과 확인 : ",게시물여러개.inserted_ids)
# insert_문제3번()

def read_문제1_도서관_books_컬렉션_조회():
    for doc in col_books.find():
        print("전체 조회 : ", doc)

    doc = col_books.find_one({"author":"김코딩"})
    print("김코딩 한 건 조회 : ",doc)

    for doc in col_books.find({"price":{"$gte":20000}}):
        print(f"가격이 20000 이상인데이터 조회 : {doc}")

    for doc in col_books.find().sort("pub_year",-1):
        print(f"최신순 정렬 : {doc}")

    for doc in col_books.find().sort("price",1).limit(2):
        print(f"가격 낮은 책 2권만 조회 : {doc}")

    for doc in col_books.find({},{"_id":0, "title":1, "price":1}):
        print(f"title, price 만 조회 : {doc}")

    count = col_books.count_documents({})
    print(f"전체 책 권수 세기 : {count}")

    exists = col_books.find_one({"author":"홍길동"}) is not None
    print(f"홍길동 존재 여부 : {exists}")
# read_문제1_도서관_books_컬렉션_조회()

def read_문제2_쇼핑몰_product_조회():
    for doc in col_products.find():
        print("전체 조회 : ", doc)

    for doc in col_products.find({"price":{"$gte":50000}}):
        print(f"가격이 50000 이상인상품 조회 : {doc}")

    for doc in col_products.find().sort("price",-1):
        print(f"가격 내림차순 조회 : {doc}")

    for doc in col_products.find({},{"_id":0,"product_name":1,"price":1}):
        print(f"특정 필드만 보기 : {doc}")

    count = col_products.count_documents({"stock" : {"$lte":50}})
    print(f"stock가 50 이하인 상품 개수 : {count}")

    for doc in col_products.find().skip(2).limit(1):
        print(f"2번째 상품부터 2개만 조회 : {doc}")

    for doc in col_products.find({"discount_rate": {"$exists": True}}):
        print(f"discount_rate 필드가 존재하는 상품 조회 : {doc}")
# read_문제2_쇼핑몰_product_조회()

def read_문제3_SNS_posts_조회():
    for doc in col_posts.find():
        print("전체 조회 : ", doc)

    doc = col_posts.find_one({"name": "김개발"})
    print("author 가 '김개발' 인 게시물 한건 조회",doc)

    for doc in col_posts.find({"likes":{"$gte":1}}):
        print(f"좋아요가 1개 이상인 게시물 : {doc}")

    for doc in col_posts.find().sort("likes", -1):
        print(f"좋아요 내림차순 조회 : {doc}")

    for doc in col_posts.find({},{"_id":0,"author":1,"content":1,"likes":1}):
        print(f"특정 필드만 보기: {doc}")

    for doc in col_posts.find({"hashtags": {"$exists": True}}):
        print(f"hashtags 필드가 존재하는 게시물만 조회 : {doc}")

    for doc in col_posts.find({"comments.writer": "최데이"}):
        print(f"comments 배열 안에 writer가 '최데이'인 게시물 조회 {doc}")

    count = col_posts.count_documents({})
    print(f"전체 게시물 수 세기 : {count}")

read_문제3_SNS_posts_조회()

