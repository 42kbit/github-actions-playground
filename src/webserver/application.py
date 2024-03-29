from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/app")
def app_page():
    return render_template('app.html')

if __name__ == "__main__":
    app.run()