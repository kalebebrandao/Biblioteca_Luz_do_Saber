from banco.conexao import conectar


class LivroDAO:
    def inserir(self, livro):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """INSERT INTO livros (titulo, autor, isbn, genero, quantidade, disponiveis)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (livro.titulo, livro.autor, livro.isbn, livro.genero,
             livro.quantidade, livro.disponiveis)
        )

        conexao.commit()
        conexao.close()

    def buscar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()

        conexao.close()
        return livros

    def atualizar(self, id_livro, livro):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """UPDATE livros
            SET titulo=?, autor=?, isbn=?, genero=?, quantidade=?, disponiveis=?
            WHERE id=?""",
            (livro.titulo, livro.autor, livro.isbn, livro.genero,
             livro.quantidade, livro.disponiveis, id_livro)
        )

        conexao.commit()
        conexao.close()

    def remover(self, id_livro):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))

        conexao.commit()
        conexao.close()
