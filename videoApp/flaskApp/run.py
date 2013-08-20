from flask import render_template, Flask, request, redirect, url_for, abort, session, flash
from flask.ext.wtf import Form
from wtforms import TextField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'L33T!';

class LoginForm(Form):
	username = TextField('username')
	password = TextField('password')


@app.route('/')
@app.route('/index')
def index():
	return render_template("login.html")
	
@app.route('/signup', methods=["GET", "POST"])
def signup():
	form = LoginForm()
	
	if (str(form.username.data)) == "luis" and (str(form.password.data)) == "sofiebio":
		return redirect(url_for('video'))
	else:
		return redirect(url_for('index'))
	
@app.route('/video')
def video():
	return render_template("video.html")
	
		
if __name__ == '__main__':
	app.run(debug=True)
	

