#!/usr/bin/python3
''' lists all states with a name starting with N (upper N)
from the Db hbtn_0e_0_usa
'''
import MySqLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM 'states' ORDER BY 'id'")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
