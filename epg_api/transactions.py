from flask import Flask,abort,jsonify
from flask_restful import Api, Resource, reqparse
import mysql.connector
from flask_mysqlpool import MySQLPool
from flask import current_app as app



class transactions(Resource):

       
           def get(self):
                db = MySQLPool(app)
                try:
                   conn = db.connection.get_connection()  # get connection from pool
                   cursor = conn.cursor(dictionary=True)
                   cursor.execute("select host,user from mysql.user")
                  
                   result = cursor.fetchall()
                   conn.close()  # return connection to pool
                except mysql.connector.Error as err:
                   print(format(err))
                   conn.close()
                   abort(500)
                to_json = [dict(row) for row in result]
                return jsonify(to_json) 
