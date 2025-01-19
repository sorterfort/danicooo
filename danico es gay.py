from flask import Flask

app = Flask(bueno)

@app.route("/")
def home():
    return "Danico es gay"

if __name__ == "__main__":
    app.run(debug=True)
