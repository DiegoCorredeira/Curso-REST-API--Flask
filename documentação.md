# Documentação da API de Músicas dos Arctic Monekys

Este documento fornece informações detalhadas sobre como utilizar os recursos disponíveis na REST API de músicas do Arctic Monkeys. Ele descreve as diferentes operações possíveis, as formas de realizar uma requisição e as respostas esperadas.

## 1. Consultar Músicas / Albuns

### Requisição para Listar músicas

Realize uma requisição GET para listar todos as músicas do sistema. Você pode opcionalmente incluir filtros personalizados via parâmetros de consulta na URL. Caso nenhum filtro seja definido, os valores padrão serão utilizados.

#### Possíveis parâmetros de consulta:

- `title`: Filtra músicas pelo nome. Padrão: Null.
- `artist`: Filtra músicas pelo nome dos artistas envolvidos. Padrão: Null.
- `album`: Filtra músicas pelo album. Padrão: Null.
- `released_date`: Filtra músicas pela data de lançamento. Padrão: Null.
- `time`: Filtra músicas pelo tempo de duração. Padrão: Null.

#### Exemplo de Requisição:

```http
GET /all?release_date=2009-08-19
```

#### Resposta:

Como resposta, obtemos uma lista com as músicas que se enquadram nos filtros de requisição acima.

- Status: 200 OK

### Requisição para Visualizar Dados de um album especifico

Realize uma requisição GET para visualizar os dados de um album específico, fornecendo o ID do album na URL.

#### Exemplo de Requisição:

```http
GET /all

GET /suckitandsee

GET /WPSIATWIN

GET /FWN

GET /humbug
```

#### Resposta:

Como resposta, você obterá um JSON contendo os dados do album/música requisitada.

- Status: 200 OK

### Requisição para música inexistente

Caso você pesquise por uma música que não existe, receberá uma mensagem de erro indicando que a música não foi encontrada.

#### Exemplo de Requisição:

```http
GET /FWN/id_que_nao_existe
```

#### Resposta:

- Status: 404 Not Found

## 2. Cadastro de Usuário

### Requisição para Cadastrar um Novo Usuário

Para cadastrar um novo usuário, realize uma requisição POST para a rota `/cadastro`. Certifique-se de incluir o cabeçalho `Content-Type: application/json` e fornecer os dados do usuário no corpo da requisição.

#### Exemplo de Requisição:

```http
POST /cadastro

Header:
Content-Type: application/json

Request Body:
{
    "nome": "Nome do Usuário",
    "email": "usuario@email.com",
    "senha": "senha123"
}
```

#### Resposta:

Você receberá uma mensagem de sucesso informando que o usuário foi criado.

- Status: 201 Created

### Requisição para Cadastrar Usuário Existente

Se você tentar cadastrar um usuário com um login que já existe, receberá uma mensagem de erro informando que o usuário com o mesmo nome já existe.

#### Exemplo de Requisição:

```http
POST /cadastro

Header:
Content-Type: application/json

Request Body:
{
    "nome": "ana",
    "email": "ana@email.com",
    "senha": "outraSenha123"
}
```

#### Resposta:

- Status: 400 Bad Request

## 3. Login de Usuário

### Requisição para Fazer Login de Usuário

Para fazer login com um usuário, realize uma requisição POST para a rota `/login`. Inclua o cabeçalho `Content-Type: application/json` e forneça as credenciais do usuário no corpo da requisição.

#### Exemplo de Requisição:

```http
POST /login

Header:
Content-Type: application/json

Request Body:
{
    "nome": "Nome do Usuário",
    "senha": "senha123"
}
```

#### Resposta:

Você receberá um token de acesso que será necessário para fazer requisições que exigem autenticação.

- Status: 200 OK

### Requisição para Login com Usuário Inexistente

Se você tentar fazer login com um usuário que não existe ou inserir credenciais incorretas, receberá uma mensagem de erro indicando que o usuário ou senha estão incorretos.

#### Exemplo de Requisição:

```http
POST /login

Header:
Content-Type: application/json

Request Body:
{
    "nome": "usuario_inexistente",
    "senha": "senha_incorreta"
}
```

#### Resposta:

- Status: 401 Unauthorized

## 4. Criar Album

### Requisição para Criar um Novo Album

Para criar um novo album, realize uma requisição POST para a rota `/novoalbum/{album_id}`. Certifique-se de incluir o cabeçalho `Content-Type: application/json` e um token de acesso no cabeçalho de autorização.

#### Exemplo de Requisição:

```http
POST /novoalbum/teste

Header:
Content-Type: application/json
Authorization: Bearer {token_de_acesso}

Request Body:
{
	             "title": "Secret Door",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:43"
}
```

#### Resposta:

Você receberá uma mensagem de sucesso ao criar a nova música pela primeira vez. Ao tentar criar novamente uma música com o mesmo ID, receberá uma mensagem de erro indicando que o ID já existe.

- Status: 201 Created (Primeira vez)
- Status: 400 Bad Request (ID já existe)

## 5. Atualizar Músicas

### Requisição para Atualizar  Músicas

Para atualizar os dados de um album, realize uma requisição PUT para a rota `/FWN/{fwn_id}`. Certifique-se de incluir o cabeçalho `Content-Type: application/json` e um token de acesso no cabeçalho de autorização.

#### Exemplo de Requisição:

```http
PUT /FWN/1

Header:
Content-Type: application/json
Authorization: Bearer {token_de_acesso}

Request Body:
{
                    "title": "Secret Door",
                    "artist": "Arctic Monkeys",
                    "album": "Humbug",
                    "release_date": "2009-08-19",
                    "time": "3:43"
}
```

#### Resposta:

Você receberá uma mensagem de sucesso ao atualizar os dados da música, juntamente com o status code 200 OK. O PUT também pode criar uma nova música se o ID não existir, emitindo uma mensagem de 201 Created na primeira vez e 200 OK nas subsequentes.

- Status: 200 OK
- Status: 201 Created (Primeira vez)
- Status: 400 Unauthorized (Token de acesso inválido)

## 6. Deletar música

### Requisição para Deletar uma música

Para deletar uma música, realize uma requisição DELETE para a rota `/FWN/{FWN_id}`. Certifique-se de incluir um token de acesso no cabeçalho de autorização.

#### Exemplo de Requisição:

```http
DELETE /FWN/teste

Header:
Authorization: Bearer {token_de_acesso}
```

#### Resposta:

Você receberá uma mensagem de sucesso ao deletar uma música existente. Ao tentar deletar a mesma música novamente, receberá um erro 404 Not Found indicando que a música não existe. Se você não enviar o token de autorização, receberá um erro 401 Unauthorized.

- Status: 200 OK
- Status: 404 Not Found
- Status: 401 Unauthorized

## 7. Logout de Usuário

### Requisição para Fazer Logout de Usuário

Para fazer logout de um usuário, realize uma requisição POST para a rota `/logout`. Envie o token de acesso no cabeçalho de autorização.

#### Exemplo de Requisição:

```http
POST /logout

Header:
Authorization: Bearer {token_de_acesso}
```

#### Resposta:

Você receberá uma mensagem de sucesso informando que o usuário foi deslogado. O token de acesso não funcionará mais em requisições subsequentes, a menos que o usuário faça login novamente.

- Status: 200 OK

## 8. Consultar Dados de Usuário

### Requisição para Ler Dados de Usuário

Para ler os dados de um usuário específico, realize uma requisição GET para a rota `/usuarios/{user_id}`. Certifique-se de incluir o cabeçalho `Content-Type: application/json`.

#### Exemplo de Requisição:

```http
GET /user/2

Header:
Content-Type: application/json
```

#### Resposta:

Você obterá os dados do usuário com o ID especificado, excluindo a senha.

- Status: 200 OK

## 9. Deletar Usuário

### Requisição para Deletar um Usuário

Para deletar um usuário, realize uma requisição DELETE para a rota `/usuarios/{user_id}`. Certifique-se de incluir um token de acesso no cabeçalho de autorização.

#### Exemplo de Requisição:

```http
DELETE /user/2

Header:
Authorization: Bearer {token_de_acesso}
```

#### Resposta:

Você receberá uma mensagem de sucesso ao deletar um usuário existente. Ao tentar deletar o mesmo usuário novamente, receberá um erro 404 Not Found indicando que o usuário não existe ou não foi encontrado. Se você enviar um token de autorização expirado, receberá um erro 401 Unauthorized.

- Status: 200 OK
- Status: 404 Not Found
- Status: 401 Unauthorized
