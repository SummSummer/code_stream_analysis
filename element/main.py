from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home_two():
    data = request.data
    my_dict = json.loads(data.decode())
    print(data)
    print(my_dict)
    result = {'result': 'success', 'data': [{'name': my_dict['code_stream'], 'value': my_dict['struct_str']}]}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
