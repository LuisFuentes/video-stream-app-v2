from flask import render_template, Flask, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'L33T!';

@app.route('/')
@app.route('/index')
def index():
	return render_template("login.html")
	
@app.route('/signup', methods=['POST'])
def signup():
	session['username'] = request.form['username']
	session['password'] = request.form['password']
	return redirect(url_for('video'))

@app.route('/video')
def video():
	return render_template("video.html")
		
if __name__ == '__main__':
	app.run()
	

