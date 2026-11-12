from flask import Flask, jsonify, request

from modelos.livro import Livro
from banco.livro_dao import LivroDAO

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Biblioteca Luz do Saber"


@app.route("/livros", methods=["GET"])
def listar_livros():
    dao = LivroDAO()
    livros = dao.buscar_todos()
    return jsonify(livros)

@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    dados = request.json

    livro = Livro(
        dados["titulo"],
        dados["autor"],
        dados["isbn"],
        dados["genero"],
        dados["quantidade"],
        dados["disponiveis"]
    )

    dao = LivroDAO()
    dao.inserir(livro)

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201


@app.route("/livros/<int:id_livro>", methods=["PUT"])
def atualizar_livro(id_livro):
    dados = request.json

    livro = Livro(
        dados["titulo"],
        dados["autor"],
        dados["isbn"],
        dados["genero"],
        dados["quantidade"],
        dados["disponiveis"]
    )

    dao = LivroDAO()
    dao.atualizar(id_livro, livro)

    return jsonify({"mensagem": "Livro atualizado com sucesso!"})


@app.route("/livros/<int:id_livro>", methods=["DELETE"])
def remover_livro(id_livro):
    dao = LivroDAO()
    dao.remover(id_livro)

    return jsonify({"mensagem": "Livro removido com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)

