from flask import Flask, render_template
from Senha import Confirmacao
from BancoProduto import CriarTabelaProduto, AddProduto, SelecionarTodosOsProdutos
import webview

app = Flask(__name__)

#Criar tabela se ela não existir
CriarTabelaProduto()

#Configurar janela do pyview
windows = webview.create_window('Projeto Banco', app, width = 1900, height=900, resizable=True, confirm_close=False)

#Acessando templates
@app.route("/")
def OOhomepage():
    return render_template("homepage.html")

@app.route("/VisualizacaoBanco")
def OOVisualizacaoBanco():
    Produto = SelecionarTodosOsProdutos()
    return render_template("VisualizacaoBanco.html", Produto=Produto)

@app.route("/AddProduto")
def OOAddMateriais():
    Produto = SelecionarTodosOsProdutos()
    return render_template("AddProduto.html", Produto=Produto)

#Acessando funções

@app.route("/Confirmacao", methods=["POST"])
def OOconfirmar_usuario():
    return Confirmacao()

@app.route("/AddProduto", methods=["POST"])
def OOAddMaterial():
    return AddProduto()

# colocar o site no ar

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True)
    
