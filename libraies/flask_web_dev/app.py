from flask import Flask, render_template,request,session
import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Enable only if using HTTPS

print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password").encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, hashed_password.decode('utf-8')))
        db.commit()
        cursor.close()
        db.close()
        return "User registered successfully!"  
    # Handle GET request
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password").encode('utf-8')

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password, user[0].encode('utf-8')):
            cursor.close()
            db.close()
            return "Login successful!"
        else:
            cursor.close()
            db.close()
            return "Invalid credentials!"
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
