from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology,login_required


app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///quiz_app.db")

# Prevent browser from serving from cache to avoid stale content.
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Login route.
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and/or password")
            

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/dashboard")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html",action_url='/login')

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# Register route
@app.route('/register',methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('register.html',action_url = '/register')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm-pass")

        if not username or not password or not confirm:
            return apology('All 3 fields are compulsory')
        
        prev_usernames = db.execute("SELECT * FROM users WHERE username = ?",username)

        if prev_usernames:
            return apology('The username is already in use.')
        
        if len(password) < 8:
            return apology('Password must be at least 8 characters')
        
        if password != confirm:
            return apology("The password and confirm password do not match.")
        
        db.execute("INSERT INTO users (username,hash) VALUES (?,?)",username,generate_password_hash(password))
        
        return redirect('/dashboard')


@app.route('/dashboard')
@login_required
def dashboard():
    quizzes = db.execute("SELECT * FROM Quizzes")
    return render_template('dashboard.html',quizzes=quizzes,index=index)


@app.route('/signout')
@login_required
def signout():
    session.clear()
    return redirect('/')

# Get answers functions that give me a list of answers to render
def get_answers(questions):
    # Initialize an empty dictionary to store answers for each question
    answers_dict = {}

    # Iterate through each question dictionary
    for question in questions:
        question_id = question['question_id']

        # Fetch answers from the database based on question_id
        answers = db.execute("SELECT * FROM Answers WHERE question_id = ?", question_id)

        # Store the answers in the answers_dict with question_id as the key
        answers_dict[question_id] = answers

    return answers_dict

@app.route('/quiz/<int:quiz_id>')
@login_required
def quiz(quiz_id):
    # Fetch data from the database based on quiz_id
    quiz = db.execute("SELECT * FROM Quizzes WHERE quiz_id = ?",quiz_id)

    questions = db.execute("SELECT * FROM Questions WHERE quiz_id = ?",quiz_id)

    answers = get_answers(questions)
                    
    # Render the quiz template with the fetched data
    return render_template('quiz.html',quiz_id = quiz_id,quiz= quiz, questions= questions ,answers  = answers)
    # return render_template('quiz.html', quiz_id=quiz_id,quiz=quiz,questions = questions,answers= answers)
