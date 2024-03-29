from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')