import sqlite3
from pathlib import Path

# Caminho do banco de dados dentro da pasta do projeto
PASTA_ATUAL = Path(__file__).resolve().parent
CAMINHO_BANCO = PASTA_ATUAL / "biblioteca.db"


def conectar():
    """Abre e retorna uma conexão com o banco de dados."""
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    """Cria as tabelas do sistema caso elas ainda não existam."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            isbn TEXT UNIQUE,
            genero TEXT,
            quantidade INTEGER NOT NULL DEFAULT 0,
            disponiveis INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            contato TEXT,
            tipo TEXT NOT NULL CHECK (tipo IN ('Aluno', 'Professor'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao TEXT,
            status TEXT NOT NULL DEFAULT 'Ativo',
            FOREIGN KEY (livro_id) REFERENCES livros(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados conectado e tabelas criadas com sucesso!")
