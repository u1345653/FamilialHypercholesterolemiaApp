from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)