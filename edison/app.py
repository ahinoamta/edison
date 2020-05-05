import edison

from flask import render_template


app = edison.app

@app.route("/")
def home():
	return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
