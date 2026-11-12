class Emprestimo:
    def __init__(self, livro_id, usuario_id, data_emprestimo, data_devolucao, status):
        self.livro_id = livro_id
        self.usuario_id = usuario_id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.status = status
