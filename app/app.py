from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",  # ❌ Intentionally wrong
        database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    return f"Database time: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
