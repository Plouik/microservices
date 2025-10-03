from flask import Flask, render_template, request
import os, requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form.get('version') == 'Get version':
			return os.getenv('FLASK_ENV', "Please set FLASK_ENV")
		elif  request.form.get('db') == 'Get DB':
			r = requests.get(f"http://backend:{os.getenv('PORT_BACKEND',80)}/db")
			return r.text

	return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('PORT_FRONTEND'))
