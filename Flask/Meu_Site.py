from flask import Flask, render_template
from Senha import Confirmacao
from BancoProduto import CriarTabelaProduto, AddProduto, SelecionarTodosOsProdutos, DeleteProduto, EditarProduto
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

@app.route("/Menu")
def OOPaginaMenu():
    return render_template("Menu.html")

@app.route("/Cadastrar-Produto")
def OOSelecionarTodosOsProdutos():
    Produto = SelecionarTodosOsProdutos()
    return render_template("Cadastrar-Produto.html", Produto=Produto)

@app.route("/PagEditarProduto/<descricao>")
def OOEditarProduto(descricao):
    EditorProduto = EditarProduto(descricao)
    return render_template("PagEditarProduto.html", EditorProduto=EditorProduto)


#Acessando funções

@app.route("/Confirmacao", methods=["POST"])
def OOconfirmar_usuario():
    return Confirmacao()

@app.route("/AddProduto", methods=["POST"])
def OOAddProduto():
    return AddProduto()

@app.route("/DeletarProduto", methods=["POST"])
def OODeletarProduto():
    return DeleteProduto()

# colocar o site no ar

if __name__ == "__main__":
    #webview.start()
    app.run(debug=True)
    
