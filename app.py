from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Ervin!"
@app.route("/index")
def index():
    return app.send_static_file('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
