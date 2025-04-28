import cx_Oracle as oci #별칭부여 가능
import csv

from pandas.core.accessor import delegate_names


def createTable():

    # 1) 연결객체 얻어오기
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2) SQL 문장 #''' => 개행 O
    sql = '''
        CREATE TABLE supply 
        (
            id                  number primary key
            ,supplier_name      varchar2(50)
            ,invoice_number     varchar2(30)
            ,part_number        varchar2(20)
            ,cost               number
            ,purchase_date      date                
        )
    '''
    # 3) cursor 객체 얻어오기
    cursor = conn.cursor()  # 변수명을 설정해서 conn를 얻어온다
    # 4) SQL 전송
    cursor.execute(sql)
    # 파이썬은 기본적으로 excute 를 사용한다
    # excute 부분에서 SQL문을 보기떄문에 sql 문장에 오류가 있거나 테이블관련해서 오류가 있으면 exectue error 라고 표시된다
    sql2 = 'CREATE SEQUENCE seq_supply_id' # seq_table명_
    cursor.execute(sql2)
    # 결과처리

    # 5) cursor 닫기
    cursor.close()
    # 6) 연결 객체 닫기
    conn.close()

def saveTable(data):
    # 1) 연결객체 얻어오기
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = """
        INSERT INTO
        supply(id,supplier_name,invoice_number,part_number,cost,purchase_date)
        VALUES(seq_supply_id.NEXTVAL, :0,:1,:2,:3,:4)
    """
    # 프로그램으로 취급하기떄문에 0 부터 시작

    # 3) cursor 객체 얻어오기
    cursor = conn.cursor()  # 변수명을 설정해서 conn를 얻어온다
                            # conn.cursor()로 얻는 객체는, => JDBC의 PreparedStatement이다.
    # 4) SQL 전송
    cursor.execute(sql, data) #순서를 잡아두면 입력 할때 알맞게 들어간다
    conn.commit()  # ************** 파이썬에서는 반드시 commit 을 해줘야한다)
    # 5) cursor 닫기
    cursor.close()
    # 6) 연결 객체 닫기
    conn.close()

def deleteData():
    #삭제할 테이블명과 PK값을 넘겨받는다고 가정
    tblName = 'supply'
    pkVal = 1;

    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = 'DELETE FROM {0} WHERE id={1}'.format(tblName,pkVal)
    # print(sql)

    cursor = conn.cursor()  # 변수명을 설정해서 conn를 얻어온다
    # conn.cursor()로 얻는 객체는, => JDBC의 PreparedStatement이다.
    # 4) SQL 전송
    cursor.execute(sql)  # 순서를 잡아두면 입력 할때 알맞게 들어간다
    conn.commit()  # ************** 파이썬에서는 반드시 commit 을 해줘야한다)
    # 5) cursor 닫기
    cursor.close()
    # 6) 연결 객체 닫기
    conn.close()


if __name__ == '__main__':
 #파이썬 내부적인 변수 => __name__

    #(0) 테이블 생성
    #createTable()

    #(1) 데이터를 저장
    #temp = ['ict','9999','8888',9000,'2025-04-28']
    #saveTable(temp) #입력하는 데이터가 따로있음

    #(9) 삭제
    deleteData()