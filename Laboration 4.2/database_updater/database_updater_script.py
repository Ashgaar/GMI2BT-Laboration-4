import sqlite3, requests, json
from sqlite3 import Error

url_for_weather_data = "https://api.openweathermap.org/data/2.5/weather?q=Borlänge&appid=30dd1f6f5388207521043b867e018856"



def main():
    database = r"C:\Users\zangi\Programmering\IT-säkerhet Högskolan Dalarna\Skriptprogrammering\Laboration 4\Laboration 4.2\db\weather_data.db3"

    sql_create_weather_table = """ CREATE TABLE weather(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    location VARCHAR(30) NOT NULL,
                                    value1 VARCHAR(10),
                                    value2 VARCHAR(10),
                                    value3 VARCHAR(10),
                                    time VARCHAR
                                );"""

    conn = create_connection(database)


    with conn:
        res = requests.get(url_for_weather_data)
        data = json.loads(res.text)

        project = (data['name'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'], res.headers['Date'])
        create_project(conn, project)

    print("Successfully added data to database.")



def create_project(conn, project):
    sql = ''' INSERT INTO weather(location,value1,value2,value3,time)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    main()
