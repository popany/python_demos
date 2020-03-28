from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)

@app.route("/get-file/<filename>")
def get_file(filename):
    try:
        return send_from_directory("c:/tmp", filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# curl -u x:y -H "Content-Type:application/json" -X GET --data '{"say": "hello"}' 192.168.1.5:8099/hello
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    user = request.authorization["username"]
    password = request.authorization["password"]
    say = request.json.get("say")
    reply = "hello"
    return jsonify({'say': say, 'reply': reply, 'user': user}) 

if __name__ == '__main__': 
    # app.run(debug = True) 
    app.run(host='0.0.0.0', debug=True, port=8099)