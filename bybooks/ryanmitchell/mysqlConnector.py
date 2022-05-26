import pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='scraping',
    cursorclass=DictCursor
)

with connection.cursor() as cursor:
    query = '''
    SELECT
        *
    FROM
        pages
    '''
    cursor.execute(query)
    for row in cursor:
        print(row)

with connection.cursor() as cursor:
    query = '''
    INSERT INTO 
        pages(title,content) 
    VALUES ("Test page title2", "Test page content2");
    '''
    cursor.execute(query)
    connection.commit()

connection.close()