from flask import Flask, send_from_directory, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Ervin!"
@app.route("/index")
def index():
    return render_template('layout.html',title="Brigitta")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
