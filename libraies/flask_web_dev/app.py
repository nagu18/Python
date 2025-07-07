from flask import Flask, render_template,request,session
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Konda@2026",
        database="user_db"
    )

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, password))
        db.commit()
        return "User registered successfully!"  
    # Handle GET request
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)
