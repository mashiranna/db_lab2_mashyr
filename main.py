import psycopg2

username = 'mashyr_anna'
password = '1234'
database = 'mashyr_anna_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select category, count(category) from app group by category
'''
query_2 = '''
select age_rating, count(age_rating) from app group by age_rating
'''

query_3 = '''
select initial_date_of_release, app_size, app.app_name from app_publisher, app
where app_publisher.app_name = app.app_name
order by initial_date_of_release
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

result_1 = []
result_2 = []
result_3 = []

with con:

    print("Database opened successfully")

    cur = con.cursor()

    print('\n1.  ')
    cur.execute(query_1)
    for row in cur:
        print(row)
        result_1.append(row)

    print('\n2.  ')
    cur.execute(query_2)
    for row in cur:
        print(row)
        result_2.append(row)

    print('\n3.  ')
    cur.execute(query_3)
    for row in cur:
        print(row)
        result_3.append(row)
