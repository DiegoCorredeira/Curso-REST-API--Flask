# Autenticação REST

#### Como funciona o modelo de autenticação na WEB

1. Autenticação:
   A autenticação é o processo de verificar a identidade de um usuário para garantir que ele seja realmente quem afirma ser. Isso é geralmente feito por meio de um nome de usuário e senha, embora outros métodos, como autenticação de dois fatores (2FA), biometria (impressões digitais, reconhecimento facial) e tokens também possam ser usados.
   * O usuário fornece suas credenciais (por exemplo, nome de usuário e senha) em um formulário de login.
   * O servidor web recebe essas credenciais e as verifica em seu banco de dados para ver se correspondem a uma conta de usuário registrada.
   * Se as credenciais estiverem corretas, o servidor autentica o usuário e concede a ele um token de sessão ou cookie, que é usado para identificar o usuário nas solicitações subsequentes.
   * O usuário agora está autenticado e pode acessar recursos protegidos.
2. Autorização:
   A autorização é o processo de determinar quais recursos um usuário autenticado tem permissão para acessar e quais operações ele pode realizar nesses recursos. Isso envolve definir políticas de acesso que especificam quem pode fazer o quê.
   * Após a autenticação bem-sucedida, o servidor verifica as permissões do usuário com base em seu perfil ou grupo de usuários.
   * As políticas de autorização definem o que um usuário pode fazer em um determinado contexto. Por exemplo, um usuário pode ter permissão para ler documentos, mas não para modificá-los.
   * Quando um usuário tenta acessar um recurso ou executar uma ação, o servidor verifica se as permissões do usuário permitem essa ação.
   * Se as permissões permitirem, o servidor concede acesso ao recurso ou permite a ação. Caso contrário, o acesso é negado.

#### REST APIs são Stateless

Isso significa que cada solicitação feita a uma API REST não deve depender do estado anterior da comunicaçào. Casa solicitação deve conter todas as informações necessárias para que o servidor compreenda e processe a solicitação, sem depender de informações de sessão ou estado de armazenamento.


#### Melhores soluções para autenticação em REST API

* Digest Access Authentication
* Asymmetric Cryptography
* OAuth
* **JSON WEB TOKEN**
