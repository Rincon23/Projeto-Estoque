from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

#Criar tabela se ela não existir
def CriarTabelaProduto():
    banco = sqlite3.connect('Dados.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        Descricao TEXT NOT NULL UNIQUE,
        Valor REAL NOT NULL,
        Quantidade REAL NOT NULL
    )
    """)

    banco.commit()
    banco.close()

@app.route("/AddProduto", methods=["POST"])
def AddProduto():
    Descricao = request.form["Descricao"]
    Valor = request.form["Valor"]
    Quantidade = request.form["Quantidade"]

    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produto (Descricao, Valor, Quantidade) VALUES (?, ?, ?)", (Descricao, Valor, Quantidade))
    conn.commit()
    conn.close()

    return redirect("/Cadastrar-Produto")

#Selecionando todas os produtos
def SelecionarTodosOsProdutos():
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    Produto = cursor.fetchall()
    conn.close()
    return Produto

@app.route("/DeletarProduto", methods=["POST"])
def DeleteProduto():
    try:
        Descricao = request.form["Descricao"]

        banco = sqlite3.connect('Dados.db')
        cursor = banco.cursor()
        cursor.execute("DELETE from Produto WHERE Descricao = ?", (Descricao,))

        banco.commit() 
        banco.close()
        print("Os dados foram removidos")
    except sqlite3.Error as erro:
        print("Erro ao excluir: ", erro)
    return redirect("/Cadastrar-Produto") 

#Buscar produto
def BuscarProduto(descricao):
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto WHERE Descricao = ?", (descricao,))
    EditorProduto = cursor.fetchone()
    conn.close()

    return EditorProduto

def EditarProduto(DescricaoAntiga, NovaDescricao, NovoValor, NovaQuantidade):
    try:
        banco = sqlite3.connect('Dados.db')
        cursor = banco.cursor()

        cursor.execute("UPDATE Produto SET Descricao = ?, Valor = ?, Quantidade = ? WHERE Descricao = ?", 
                       (NovaDescricao, NovoValor, NovaQuantidade, DescricaoAntiga))

        banco.commit() 
        banco.close()
        print("Produto atualizado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao atualizar o produto: ", erro)

    return redirect("/Cadastrar-Produto")

@app.route("/EditarProduto", methods=["POST"])
def EditarProdutoRoute():
    try:
        DescricaoAntiga = request.form["DescricaoAntiga"]
        NovaDescricao = request.form["NovaDescricao"]
        NovoValor = request.form["NovoValor"]
        NovaQuantidade = request.form["NovaQuantidade"]

        EditarProduto(DescricaoAntiga, NovaDescricao, NovoValor, NovaQuantidade)

    except sqlite3.Error as erro:
        print("Erro ao atualizar o produto: ", erro)

    return redirect("/Cadastrar-Produto")
