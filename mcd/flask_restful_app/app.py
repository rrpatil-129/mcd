# import json
#
#
# def lambda_handler(event, context):
#     # TODO implement
#     print("Inside lambda function")
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home', methods=['GET'])
def home():
    return "Wel-Come to McDonalds Project"


app.run(host='0.0.0.0')
