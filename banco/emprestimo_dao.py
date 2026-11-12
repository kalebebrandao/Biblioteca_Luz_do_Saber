from banco.conexao import conectar


class EmprestimoDAO:
    def inserir(self, emprestimo):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """INSERT INTO emprestimos
            (livro_id, usuario_id, data_emprestimo, data_devolucao, status)
            VALUES (?, ?, ?, ?, ?)""",
            (emprestimo.livro_id, emprestimo.usuario_id,
             emprestimo.data_emprestimo, emprestimo.data_devolucao,
             emprestimo.status)
        )

        conexao.commit()
        conexao.close()

    def buscar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM emprestimos")
        emprestimos = cursor.fetchall()

        conexao.close()
        return emprestimos

    def atualizar(self, id_emprestimo, emprestimo):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """UPDATE emprestimos
            SET livro_id=?, usuario_id=?, data_emprestimo=?,
            data_devolucao=?, status=?
            WHERE id=?""",
            (emprestimo.livro_id, emprestimo.usuario_id,
             emprestimo.data_emprestimo, emprestimo.data_devolucao,
             emprestimo.status, id_emprestimo)
        )

        conexao.commit()
        conexao.close()

    def remover(self, id_emprestimo):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM emprestimos WHERE id=?",
            (id_emprestimo,)
        )

        conexao.commit()
        conexao.close()
