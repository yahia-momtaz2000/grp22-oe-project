# install packages [ mysql |  mysql-connector-python ]
import mysql.connector

class DBConnectionFactory:
    # static variables : username, password, db_name, hostname
    USER = 'root'
    PASSWORD = 'root'
    HOST = 'localhost'
    DATABASE = 'oe'

    @staticmethod
    def create_connection():
        db_conn = mysql.connector.connect(user=DBConnectionFactory.USER,
                                          password=DBConnectionFactory.PASSWORD,
                                          host=DBConnectionFactory.HOST,
                                          database=DBConnectionFactory.DATABASE)
        db_conn.autocommit = False
        return db_conn

# main program
# my_conn = DBConnectionFactory.create_connection()
# print(my_conn)
#

