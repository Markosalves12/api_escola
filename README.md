# 🎓 API Escola

Uma API RESTful desenvolvida com Django + Django REST Framework para **gerenciar alunos e matrículas em cursos escolares**.

> Repositório oficial: [https://github.com/Markosalves12/api_escola](https://github.com/Markosalves12/api_escola.git)

## 📚 Funcionalidades

- 👤 Cadastro de alunos
- 📘 Cadastro de cursos
- 📝 Matrícula de alunos em cursos
- 🔍 Listagem de alunos, cursos e matrículas
- 🧾 Filtros por nome, curso, data, etc.
- 🔐 Autenticação de acesso à API

## 🧰 Tecnologias Utilizadas

- **Django 4.x**
- **Django REST Framework**
- **SQLite** (padrão, mas pode usar PostgreSQL)
- **DRF-YASG** (para documentação Swagger/OpenAPI)
- **Python 3.10+**

---

## 🔄 Endpoints Disponíveis

Exemplos de rotas:

### 📌 Alunos
| Método | Endpoint         | Ação                 |
|--------|------------------|----------------------|
| GET    | /api/alunos/     | Listar alunos        |
| POST   | /api/alunos/     | Criar aluno          |
| GET    | /api/alunos/1/   | Detalhar aluno       |
| PUT    | /api/alunos/1/   | Atualizar aluno      |
| DELETE | /api/alunos/1/   | Remover aluno        |

### 📌 Cursos
| Método | Endpoint        | Ação                |
|--------|-----------------|---------------------|
| GET    | /api/cursos/    | Listar cursos       |
| POST   | /api/cursos/    | Criar curso         |

### 📌 Matrículas
| Método | Endpoint             | Ação                    |
|--------|----------------------|-------------------------|
| GET    | /api/matriculas/     | Listar todas as matrículas |
| POST   | /api/matriculas/     | Criar nova matrícula  
