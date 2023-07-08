import psycopg2
import psycopg2.extras
hostname = 'localhost'
database = 'demo_python'
owner = 'postgres'
pwd = 'python'
port_id = 5432
conn = None
try:
    conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = owner,
    password = pwd,
    port= port_id 
    )
    cur = conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
    cur.execute('drop table if exists employees')
    create_table = ''' create table if not exists employees (EMPLOYEE_ID real not null primary key,	FIRST_NAME	varchar,
                        LAST_NAME	varchar, EMAIL varchar,	PHONE_NUMBER varchar,	
                        HIRE_DATE date, 	JOB_ID	int, SALARY	float, COMMISSION_PCT varchar,	MANAGER_ID int, 	DEPARTMENT_ID int)'''
    cur.execute(create_table)
    insert_data = 'insert into employees values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_values = [(  25, 'Abdulkadir', 'Duran', 'abdulkadir5035010144gmail.com', '+8613205296991', '2022-08-10', 25, 60000, '-', 6, 100 ),
                        (198,	'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '2022-08-10', 25,	2600,	 '- ',	124,	50),
                        (199,	'Douglas', 	'Grant',	'DGRANT', '650.507.9844','2013-06-08',40,	2600,	 '-' ,	124,	50 ),
                        (200,	'Jennifer',	'Whalen',	'JWHALEN',	'515.123.4444',	'2017-09-03',	70,	4400,	 '-',	101,	10),
                        (201,	'Michael',	'Hartstein',	'MHARTSTE',	'515.123.5555',	'2017-02-04',	25,	13000,  '-', 	100,	20),
                        (202,	'Pat',   'Fay',	'FAY',	'603.123.6666',	'2017-08-05',	30,	30000,	 '-', 201,	20),
                        (203, 'Kader', 'Ali', 'Ali', '+8613202596991', '2022-08-10', 30, 25000, '25', 202, 20),
                    ]
    
    for record in insert_values:
        cur.execute(insert_data, record)
    cur.execute('select * from employees')
    for record in cur.fetchall():
        print(record['salary'])
    update_table = '''update employees set COMMISSION_PCT = '25' '''
    cur.execute(update_table)

    delete_data = 'delete from employees where EMPLOYEE_ID = 203'
    cur.execute(delete_data)
    conn.commit()
    

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()