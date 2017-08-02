from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('test.html')

@app.route('/details')
def self_intro():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)