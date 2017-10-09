import subprocess
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
 
@app.route("/")
def index():
	command = request.args.get('ping') if request.args.get('ping') else None
	if command:
		output = subprocess.check_output(command, shell=True)
		return output
	else:
		return "This is a ping service. Please use http://url/?ping=google.com to ping"

@app.route("/hello")
def hello():
	return render_template("index.html")
 
if __name__ == "__main__":
    app.run(debug=True)
