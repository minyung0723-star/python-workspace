import mysql.connector

def DB연결():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="tjee1234",
        database="instagram_clone"
    )
    return conn
def 유저전체조회기능():
    conn = DB연결()
    # cursor = conn.cursor()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    결과목록 = cursor.fetchall()
    for 행 in 결과목록:
        print(행)
    cursor.close()
    conn.close()

유저전체조회기능()