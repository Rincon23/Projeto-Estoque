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

#Editar produto
def EditarProduto(descricao):
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto WHERE Descricao = ?", (descricao,))
    EditorProduto = cursor.fetchone()
    conn.close()

    return EditorProduto