# Diagrama de Classes — Biblioteca Escolar Luz do Saber

```mermaid
classDiagram
    class Livro {
        +int id
        +str titulo
        +str autor
        +str isbn
        +str genero
        +int quantidade
        +int disponiveis
    }

    class Usuario {
        <<abstract>>
        +int id
        +str nome
        +str matricula
        +str contato
    }

    class Aluno {
        +str tipo
    }

    class Professor {
        +str tipo
    }

    class Emprestimo {
        +int id
        +date data_emprestimo
        +date data_devolucao
        +str status
    }

    class Acervo {
        +adicionar_livro()
        +consultar_livros()
        +atualizar_quantidade()
    }

    Usuario <|-- Aluno
    Usuario <|-- Professor
    Livro "1" --> "0..*" Emprestimo : participa
    Usuario "1" --> "0..*" Emprestimo : realiza
    Acervo "1" o-- "0..*" Livro : organiza
```

## Relacionamentos
- `Usuario` é uma classe abstrata. `Aluno` e `Professor` herdam dela.
- Um livro pode aparecer em vários empréstimos ao longo do tempo.
- Um usuário pode realizar vários empréstimos.
- O acervo organiza vários livros.
