
const API = "http://127.0.0.1:5000";

// LIVROS

async function listarLivros() {
    const resposta = await fetch(API + "/livros");
    const livros = await resposta.json();
    const tabela = document.getElementById("lista-livros");

    tabela.innerHTML = "";

    livros.forEach(function(livro) {
        const linha = document.createElement("tr");

        livro.forEach(function(valor) {
            const coluna = document.createElement("td");
            coluna.textContent = valor;
            linha.appendChild(coluna);
        });

        const acoes = document.createElement("td");

        const editar = document.createElement("button");
        editar.textContent = "Editar";
        editar.onclick = function() {
            document.getElementById("livro-id").value = livro[0];
            document.getElementById("titulo").value = livro[1];
            document.getElementById("autor").value = livro[2];
            document.getElementById("isbn").value = livro[3];
            document.getElementById("genero").value = livro[4];
            document.getElementById("quantidade").value = livro[5];
            document.getElementById("disponiveis").value = livro[6];
        };

        const excluir = document.createElement("button");
        excluir.textContent = "Excluir";
        excluir.onclick = async function() {
            if (confirm("Deseja excluir este livro?")) {
                await fetch(API + "/livros/" + livro[0], {
                    method: "DELETE"
                });
                listarLivros();
            }
        };

        acoes.appendChild(editar);
        acoes.appendChild(excluir);
        linha.appendChild(acoes);
        tabela.appendChild(linha);
    });
}

document.getElementById("form-livros").addEventListener("submit", async function(evento) {
    evento.preventDefault();

    const id = document.getElementById("livro-id").value;

    const dados = {
        titulo: document.getElementById("titulo").value,
        autor: document.getElementById("autor").value,
        isbn: document.getElementById("isbn").value,
        genero: document.getElementById("genero").value,
        quantidade: Number(document.getElementById("quantidade").value),
        disponiveis: Number(document.getElementById("disponiveis").value)
    };

    await fetch(API + "/livros" + (id ? "/" + id : ""), {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    this.reset();
    document.getElementById("livro-id").value = "";
    listarLivros();
});

// USUÁRIOS

async function listarUsuarios() {
    const resposta = await fetch(API + "/usuarios");
    const usuarios = await resposta.json();
    const tabela = document.getElementById("lista-usuarios");

    tabela.innerHTML = "";

    usuarios.forEach(function(usuario) {
        const linha = document.createElement("tr");

        usuario.forEach(function(valor) {
            const coluna = document.createElement("td");
            coluna.textContent = valor;
            linha.appendChild(coluna);
        });

        const acoes = document.createElement("td");

        const editar = document.createElement("button");
        editar.textContent = "Editar";
        editar.onclick = function() {
            document.getElementById("usuario-id").value = usuario[0];
            document.getElementById("nome").value = usuario[1];
            document.getElementById("matricula").value = usuario[2];
            document.getElementById("contato").value = usuario[3];
            document.getElementById("tipo").value = usuario[4];
        };

        const excluir = document.createElement("button");
        excluir.textContent = "Excluir";
        excluir.onclick = async function() {
            if (confirm("Deseja excluir este usuário?")) {
                await fetch(API + "/usuarios/" + usuario[0], {
                    method: "DELETE"
                });
                listarUsuarios();
            }
        };

        acoes.appendChild(editar);
        acoes.appendChild(excluir);
        linha.appendChild(acoes);
        tabela.appendChild(linha);
    });
}

document.getElementById("form-usuarios").addEventListener("submit", async function(evento) {
    evento.preventDefault();

    const id = document.getElementById("usuario-id").value;

    const dados = {
        nome: document.getElementById("nome").value,
        matricula: document.getElementById("matricula").value,
        contato: document.getElementById("contato").value,
        tipo: document.getElementById("tipo").value
    };

    await fetch(API + "/usuarios" + (id ? "/" + id : ""), {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    this.reset();
    document.getElementById("usuario-id").value = "";
    listarUsuarios();
});

// EMPRÉSTIMOS

async function listarEmprestimos() {
    const resposta = await fetch(API + "/emprestimos");
    const emprestimos = await resposta.json();
    const tabela = document.getElementById("lista-emprestimos");

    tabela.innerHTML = "";

    emprestimos.forEach(function(emprestimo) {
        const linha = document.createElement("tr");

        emprestimo.forEach(function(valor) {
            const coluna = document.createElement("td");
            coluna.textContent = valor === null ? "-" : valor;
            linha.appendChild(coluna);
        });

        const acoes = document.createElement("td");

        const editar = document.createElement("button");
        editar.textContent = "Editar";
        editar.onclick = function() {
            document.getElementById("emprestimo-id").value = emprestimo[0];
            document.getElementById("livro-id-emprestimo").value = emprestimo[1];
            document.getElementById("usuario-id-emprestimo").value = emprestimo[2];
            document.getElementById("data-emprestimo").value = emprestimo[3];
            document.getElementById("data-devolucao").value = emprestimo[4] || "";
            document.getElementById("status").value = emprestimo[5];
        };

        const excluir = document.createElement("button");
        excluir.textContent = "Excluir";
        excluir.onclick = async function() {
            if (confirm("Deseja excluir este empréstimo?")) {
                await fetch(API + "/emprestimos/" + emprestimo[0], {
                    method: "DELETE"
                });
                listarEmprestimos();
            }
        };

        acoes.appendChild(editar);
        acoes.appendChild(excluir);
        linha.appendChild(acoes);
        tabela.appendChild(linha);
    });
}

document.getElementById("form-emprestimos").addEventListener("submit", async function(evento) {
    evento.preventDefault();

    const id = document.getElementById("emprestimo-id").value;

    const dados = {
        livro_id: Number(document.getElementById("livro-id-emprestimo").value),
        usuario_id: Number(document.getElementById("usuario-id-emprestimo").value),
        data_emprestimo: document.getElementById("data-emprestimo").value,
        data_devolucao: document.getElementById("data-devolucao").value || null,
        status: document.getElementById("status").value
    };

    await fetch(API + "/emprestimos" + (id ? "/" + id : ""), {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    this.reset();
    document.getElementById("emprestimo-id").value = "";
    listarEmprestimos();
});

// CARREGAR OS REGISTROS

listarLivros();
listarUsuarios();
listarEmprestimos();
