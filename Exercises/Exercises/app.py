from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Zepto!</h1><p>Flask app running on Kubernetes.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
