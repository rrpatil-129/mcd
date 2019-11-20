import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home', methods=['GET'])
def home():
    return "Wel-Come to McDonalds"


app.run(host='0.0.0.0')
