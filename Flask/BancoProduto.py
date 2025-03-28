from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

#Criar tabela se ela não existir
def CriarTabelaProduto():
    banco = sqlite3.connect('Dados.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        IdProduto INTEGER PRIMARY KEY AUTOINCREMENT,
        Descricao TEXT,
        Valor REAL
    )
    """)

    banco.commit()
    banco.close()

@app.route("/AddProduto", methods=["POST"])
def AddProduto():
    Descricao = request.form["Descricao"]
    Valor = request.form["Valor"]

    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produto (Descricao, Valor) VALUES (?, ?)", (Descricao, Valor))
    conn.commit()
    conn.close()

    return redirect("/VisualizacaoBanco")

#Selecionando todas os produtos
def SelecionarTodosOsProdutos():
    conn = sqlite3.connect("Dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    Produto = cursor.fetchall()
    conn.close()
    return Produto