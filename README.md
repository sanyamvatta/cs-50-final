# GetQuizzed
#### Video Demo:  https://youtu.be/tG2AZs6m-Io
#### Description: Hello everyone. GetQuizzed is a simple web based quiz application. It contains multiple quizzes ( 3 as of today) but simple SQL queries can be used to add more. It is based on HTML, css, JavaScript for frontend . It also uses bootstrap for styling and some of its styles are also inspired by codepen.While for the backend and db it uses flask and SQL. It has login functionality and allows various users to give quizzes in different categories when they are logged in. If the user is not logged in he will only be able to access the about page of the website. When logged in the user will be able to gain full functionality. The users after giving the quiz will have their score evaluated and will be tested if they are the master or not. They can see thier history as well as their percentile rank in each quiz. Their is also a global leaderboard where different people/users can compete to be at the top of each quiz. each quiz is of 10 questions and a score from 0 to 40000 can be achieved. This is all of my app as of today. Also the website if fully mobile responsive which means the style of my website changes based on the screen size via the use of css media queries and bootstap's responsive designs.

## Now I will be explaining the whole work flow of my app and what each file in my project does.

#### 1. App.py : This is the main app of my project. This app initializes the flask app and defines multiple routes. It contains all the main functionality of the app . Like login, register, quiz checking, scoring and leaderboards. 

#### 2. Helpers.py: I created this file to avoid cluttering and keeping my app.py succint and clean. In this file I have added various helper functions which I use multiple times in my code like apology and login required.

#### 3. Schemas.sql : This app is an sql file that is used for any new person viewing my project get a sense of the schema of the database of my project. So he can contribute more easily. it contains all the SQL commands I used to create the multiple tables of my app.

#### 4. Quiz_app.db : This file contains the database of my file. This is the part of core functionality of my fille. The database stores the users, make them able to log in, store the quiz data as well as the leaderboard.

#### 5. Templates folder : This folder in my project directory contains all the Jinja templates I use to render the different views to my user. It has a different index.html for when the user first enters the sight and also a different template for login and register. But rest all of the templates of my file extend a base "layout.html" template to avoid repetition of code and promote code resuability.

#### 6. Static folder : This folder in the project contains all of my static resources that I use to make my project stylish and interactive. This mainly consist of my CSS and JS files. These files are used to style the html and the JS is used to give some interactivity to the app.

## Learnings

### Creating this app for me was a beautiful part of CS50. I first took on a quiz app thinking it would be easy to develop and their wouldn't be much complexity to it. Now you may ask why I picked a simple project? The simple answer is I was not confident though I completed all the psets they were guided. I was scared to swim in the sea alone without the help of "Brian Yu" (seems dramatic). But as I delved deeper into the app I found out that no app is big or small. Even a simple quiz app that I envisioned to be a single page app grew out and as I was going I added multiple features, multiple quizzes because that is what we learned in CS50. Always challenge yourself for more. Thankyou David Malan, Brian Yu and all the CS50 team for making such a beautiful course free and a memorable part in my CS50 journey. 


