from flask import Flask, url_for, redirect, request, session, render_template, flash

app = Flask(__name__)
app.secret_key = "REPLACE KEY LATER"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/