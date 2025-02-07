# API Filmes

## Introdução

Esta API RESTful foi desenvolvida para expor dados relacionados a filmes, atores, gêneros e reviews. Utilizando o framework **Django** juntamente com o **Django REST Framework (DRF)**, a aplicação permite operações de CRUD e consultas de informações de forma segura e escalável. Ela é destinada a parceiros e clientes que necessitam consumir esses dados para diferentes finalidades.

## Tecnologias Utilizadas

- **Django:** Framework web para desenvolvimento ágil em Python.
- **Django REST Framework (DRF):** Extensão do Django para criação de APIs RESTful.
- **SQLite:** Banco de dados utilizado para persistência dos dados (ideal para desenvolvimento; em produção, pode ser substituído por PostgreSQL ou outro SGBD robusto).
- **DRF Spectacular/Swagger:** Ferramentas para gerar documentação interativa dos endpoints.

## Arquitetura

A aplicação segue o padrão **MVT** do Django, que pode ser mapeado para o tradicional **MVC**:

- **Model:**  
  Define as entidades do domínio (ex.: `Movie`, `Actor`, `Genre`, `Review`) no arquivo `models.py`. Essas classes representam as tabelas do banco de dados e suas relações.

- **View (Controller):**  
  As views, localizadas em `views.py`, são responsáveis por receber as requisições HTTP, processar a lógica de negócio e orquestrar a resposta adequada.

- **Serializer:**  
  Os serializers, em `serializers.py`, convertem os dados dos models para JSON e validam os dados recebidos.

A estrutura do projeto está dividida em módulos (ou apps), como **movies**, **actors**, **genres** e **reviews**, cada um representando um domínio específico. A comunicação com o banco de dados é feita por meio do ORM do Django, que abstrai o acesso e as operações sobre os dados.

## Endpoints

### Filmes (Movies)

#### 1. Listar Todos os Filmes / Buscar por Nome
- **Endpoint:** `/movies/`
- **Método:** `GET`
- **Descrição:** Retorna uma lista de todos os filmes cadastrados. É possível filtrar os resultados pelo nome utilizando o parâmetro de consulta `search`.
- **Exemplo de URL:** `/movies/?search=Inception`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "name": "O Poderoso Chefão",
      "genre": 2,
      "release_date": "1972-03-24",
      "rating": 9.2,
      "actors": [1, 2, 3],
      "resume": "Sinopse do filme..."
    },
    {
      "id": 2,
      "name": "Star Wars: Episódio IV",
      "genre": 4,
      "release_date": "1977-05-25",
      "rating": 8.6,
      "actors": [4, 5, 6],
      "resume": "Sinopse do filme..."
    }
  ]
  ```

#### 2. Buscar Filme por ID
- **Endpoint:** `/movies/{id}/`
- **Método:** `GET`
- **Descrição:** Retorna os detalhes de um filme específico com base no seu ID.
- **Exemplo de URL:** `/movies/1/`
- **Resposta:**
  ```json
  {
    "id": 1,
    "name": "O Poderoso Chefão",
    "genre": 2,
    "release_date": "1972-03-24",
    "rating": 9.2,
    "actors": [1, 2, 3],
    "resume": "Sinopse do filme..."
  }
  ```
- **Erros:** Retorna `404 Not Found` se o filme não existir.

#### 3. Criar Novo Filme
- **Endpoint:** `/movies/`
- **Método:** `POST`
- **Descrição:** Cria um novo registro de filme.
- **Corpo da Requisição (JSON):**
  ```json
  {
    "name": "Novo Filme",
    "genre": 3,
    "release_date": "2025-05-20",
    "rating": 8.5,
    "actors": [4, 5],
    "resume": "Descrição e sinopse do novo filme"
  }
  ```
- **Código de Status:** `201 Created`

#### 4. Atualizar Filme
- **Endpoint:** `/movies/{id}/`
- **Método:** `PUT`
- **Descrição:** Atualiza os dados de um filme existente.

#### 5. Excluir Filme
- **Endpoint:** `/movies/{id}/`
- **Método:** `DELETE`
- **Descrição:** Exclui um filme com base no seu ID.

#### 6. Contar Filmes
- **Endpoint:** `/movies/count/`
- **Método:** `GET`
- **Descrição:** Retorna a quantidade total de filmes cadastrados.

## Melhorias Futuras

- **Migração para Banco de Dados Robusto:**  
  Substituir o SQLite por PostgreSQL ou outro SGBD robusto para ambientes de produção.

- **Autenticação e Autorização:**  
  Implementar autenticação JWT e mecanismos de autorização para proteger os endpoints.

- **Caching e Otimização de Performance:**  
  Integrar um sistema de cache (por exemplo, Redis) para melhorar a performance.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto-api.git
   ```
2. **Instale as dependências:**
   ```bash
   cd seu-projeto-api
   pip install -r requirements.txt
   ```
3. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```
4. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```
5. **Acesse a documentação interativa:**
   - Navegue até: `http://localhost:8000/api/v1/docs/`
