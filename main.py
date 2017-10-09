import subprocess
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
	command = request.args.get('ping') if request.args.get('ping') else None
	if command:
		output = subprocess.check_output(command, shell=True)
	else:
		output = "None"
	return render_template("index.html",output=output)
 
if __name__ == "__main__":
    app.run(debug=True)
