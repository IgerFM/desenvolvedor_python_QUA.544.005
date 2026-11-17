#SECTION - Flask
from flask import Flask, render_template, request #!SECTION


app = Flask(__name__)

#SECTION - Rota
@app.route("/")
def index():
    return render_template("index.html") #!SECTION

@app.route("/maioridade", methods = ['POST'])
def maioridade():
    nome = None
    idade = None

    if request.method == 'POST':
        nome = request.form.get('nome', '')
        idade = int(request.form.get('idade', ''))
        result = f"É maior de idade" if idade >= 18 else "É menor de idade"
    return render_template("result.html", nome=nome, result=result)

#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True) #!SECTION