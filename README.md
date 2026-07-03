# API REST utilizando HTTP e Docker

Projeto desenvolvido para a disciplina **Redes Convergentes**, com o objetivo de demonstrar o funcionamento do protocolo **HTTP** por meio da implementação de uma **API REST** executada em containers Docker.

---

## 📖 Sobre o Projeto

O protocolo HTTP é a base da comunicação entre clientes e servidores na Web. Neste projeto foi desenvolvida uma API REST simples utilizando **Python** e **Flask**, permitindo demonstrar na prática:

- Arquitetura cliente-servidor;
- Métodos HTTP (GET, POST, PUT e DELETE);
- Códigos de resposta HTTP;
- Comunicação utilizando mensagens em formato JSON;
- Containerização da aplicação com Docker.

---

## 🎯 Objetivo

Demonstrar o funcionamento do protocolo HTTP por meio da implementação de uma API REST containerizada, evidenciando a comunicação cliente-servidor, os métodos HTTP e os códigos de resposta.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Flask
- Docker
- Docker Compose
- HTTP
- JSON

---

## 📂 Estrutura do Projeto

```text
projeto-http/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── Tutorial_API_HTTP_Docker.pdf
└── imagens/
```

---

## 🚀 Como Executar

### Pré-requisitos

- Docker
- Docker Compose

### 1. Clone o repositório

```bash
git clone https://github.com/vito-hnq/projeto-http-rest.git
```

### 2. Acesse a pasta

```bash
cd projeto-http-rest
```

### 3. Execute a aplicação

```bash
docker compose up --build
```

Após a inicialização, a API estará disponível em:

```
http://localhost:5000
```

---

## 🌐 Endpoints

### Verificar funcionamento da API

```http
GET /
```

Resposta:

```json
{
  "mensagem": "API HTTP funcionando"
}
```

---

### Listar dispositivos

```http
GET /dispositivos
```

---

### Cadastrar dispositivo

```http
POST /dispositivos
```

Exemplo de JSON:

```json
{
  "nome": "Switch",
  "ip": "192.168.1.2"
}
```

---

### Atualizar dispositivo

```http
PUT /dispositivos/{id}
```

Exemplo:

```json
{
  "nome": "Switch Core",
  "ip": "10.0.0.2"
}
```

---

### Remover dispositivo

```http
DELETE /dispositivos/{id}
```

---

## 📷 Demonstração

Após executar a aplicação:

```
http://localhost:5000/
```

Resultado esperado:

```json
{
  "mensagem": "API HTTP funcionando"
}
```

---

## 📄 Tutorial

O tutorial completo encontra-se no arquivo:

```
Tutorial_API_HTTP_Docker.pdf
```

---

## 📚 Conteúdos Demonstrados

- Comunicação Cliente-Servidor
- HTTP
- API REST
- Métodos HTTP
- Códigos de Status HTTP
- JSON
- Docker
- Containerização

---

## 👨‍💻 Autor

**Victor Henrique Santos Ferreira**

Curso Superior de Tecnologia em Redes de Computadores

Instituto Federal da Paraíba (IFPB)

---

## 📜 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina de Redes Convergentes.
