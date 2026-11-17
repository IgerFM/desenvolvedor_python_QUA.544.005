#SECTION - Flask
from flask import Flask #!SECTION

#SECTION - Ativação framework
app = Flask(__name__) #!SECTION

#SECTION - Rota
#NOTE - Cria uma rota para o conteúdo a ser exibido no navegador
@app.route("/")
def hello_world():
    return f"Olá, mundo! 🌏"

#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True)

    