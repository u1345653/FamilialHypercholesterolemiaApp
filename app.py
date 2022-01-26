from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    if request.method == "POST":
        data = request.data
        print("Python Data: ", data)
        return render_template('index.html', data = data)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)