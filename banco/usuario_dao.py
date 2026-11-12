from banco.conexao import conectar


class UsuarioDAO:
    def inserir(self, usuario):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """INSERT INTO usuarios (nome, matricula, contato, tipo)
            VALUES (?, ?, ?, ?)""",
            (usuario.nome, usuario.matricula, usuario.contato, usuario.tipo)
        )

        conexao.commit()
        conexao.close()

    def buscar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        conexao.close()
        return usuarios

    def atualizar(self, id_usuario, usuario):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """UPDATE usuarios
            SET nome=?, matricula=?, contato=?, tipo=?
            WHERE id=?""",
            (usuario.nome, usuario.matricula, usuario.contato,
             usuario.tipo, id_usuario)
        )

        conexao.commit()
        conexao.close()

    def remover(self, id_usuario):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))

        conexao.commit()
        conexao.close()
