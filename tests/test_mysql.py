import sys
import pymysql

# con = pymysql.connect('server', 'username', 'password', 'dbname')
if (len(sys.argv) != 5):
    print("Number of arguments: {}".format(len(sys.argv)))
    print("\nUsage: {} server username password dbname\n".format(sys.argv[0]))
    sys.exit("Refer Usage syntax")

con = pymysql.connect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print("Database version is: {}".format(version[0]))
sys.exit(0)
