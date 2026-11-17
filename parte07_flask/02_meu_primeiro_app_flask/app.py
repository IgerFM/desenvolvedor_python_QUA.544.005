#SECTION - Flask
from flask import Flask, render_template #!SECTION

#SECTION - 
app = Flask(__name__)

#SECTION - Rota
@app.route("/")
def index():
    return render_template("index.html")

#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True)