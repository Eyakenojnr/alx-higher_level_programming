#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE LEFT(name, 1) = 'N' ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database: ", e)
        sys.exit(1)
