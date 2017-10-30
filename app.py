import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", data=data)


with open('exercise-data.json') as json_data:
    data = json.load(json_data)
    json_data.close()
    print(data)

if __name__ == "__main__":
    app.run()
