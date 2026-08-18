from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My Python app is working on Render."

if __name__ == "__main__":
    app.run()
