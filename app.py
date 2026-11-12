from flask import Flask, jsonify, request

from modelos.livro import Livro
from banco.livro_dao import LivroDAO
from modelos.usuario import Usuario
from banco.usuario_dao import UsuarioDAO
from modelos.emprestimo import Emprestimo
from banco.emprestimo_dao import EmprestimoDAO

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

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    dao = UsuarioDAO()
    usuarios = dao.buscar_todos()
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.json

    usuario = Usuario(
        dados["nome"],
        dados["matricula"],
        dados["contato"],
        dados["tipo"]
    )

    dao = UsuarioDAO()
    dao.inserir(usuario)

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

@app.route("/usuarios/<int:id_usuario>", methods=["PUT"])
def atualizar_usuario(id_usuario):
    dados = request.json

    usuario = Usuario(
        dados["nome"],
        dados["matricula"],
        dados["contato"],
        dados["tipo"]
    )

    dao = UsuarioDAO()
    dao.atualizar(id_usuario, usuario)

    return jsonify({"mensagem": "Usuário atualizado com sucesso!"})

@app.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def remover_usuario(id_usuario):
    dao = UsuarioDAO()
    dao.remover(id_usuario)

    return jsonify({"mensagem": "Usuário removido com sucesso!"})

@app.route("/emprestimos", methods=["GET"])
def listar_emprestimos():
    dao = EmprestimoDAO()
    emprestimos = dao.buscar_todos()
    return jsonify(emprestimos)

@app.route("/emprestimos", methods=["POST"])
def cadastrar_emprestimo():
    dados = request.json

    emprestimo = Emprestimo(
        dados["livro_id"],
        dados["usuario_id"],
        dados["data_emprestimo"],
        dados["data_devolucao"],
        dados["status"]
    )

    dao = EmprestimoDAO()
    dao.inserir(emprestimo)

    return jsonify({"mensagem": "Empréstimo cadastrado com sucesso!"}), 201

@app.route("/emprestimos/<int:id_emprestimo>", methods=["PUT"])
def atualizar_emprestimo(id_emprestimo):
    dados = request.json

    emprestimo = Emprestimo(
        dados["livro_id"],
        dados["usuario_id"],
        dados["data_emprestimo"],
        dados["data_devolucao"],
        dados["status"]
    )

    dao = EmprestimoDAO()
    dao.atualizar(id_emprestimo, emprestimo)

    return jsonify({"mensagem": "Empréstimo atualizado com sucesso!"})

@app.route("/emprestimos/<int:id_emprestimo>", methods=["DELETE"])
def remover_emprestimo(id_emprestimo):
    dao = EmprestimoDAO()
    dao.remover(id_emprestimo)

    return jsonify({"mensagem": "Empréstimo removido com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)

