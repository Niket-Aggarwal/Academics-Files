from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as c
app = Flask(__name__)
CORS(app)
con=c.connect(
    host="localhost",
    user="root",     
    password="admin",   
    database="web" 
)   
cursor = con.cursor()
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    review = data.get('review')
    option = data.get('option')
    if not review or not option:
        return jsonify({'message': 'All fields are required!'}), 400
    try:
        sql = "INSERT INTO form (text,review) VALUES (%s, %s)"
        cursor.execute(sql, (review, option))
        con.commit()
        return jsonify({'message': 'Feedback stored'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Database error!'}), 500
if __name__ == '__main__':
    app.run(debug=True)
