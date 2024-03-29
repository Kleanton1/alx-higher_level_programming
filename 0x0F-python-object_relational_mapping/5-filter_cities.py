#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
    JOIN states ON cities.state_id = state.id
    WHERE states.name = argv[4]
    """)
    [print(city) for city in cur.fetchall()]
