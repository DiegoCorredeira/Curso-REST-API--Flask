# Resposta HTTP no REST


#### Status Code: 

São codigos que são enviados juntamente com a resposta de uma requisição HTTP. Esses códigos ajudam o cliente saber se a requisição foi bem sucedida. E se não foi, ajuda a entender qual foi a causa do provavel erro!

As mais comuns são

* **200 -> Success**
* **500 -> Server Error**
* **404 -> Not Found**

![1694961867200](image/respostarest/1694961867200.png)

Normalmente, quem adiciona a página 404, é o desenvolvedor que está consumindo o REST API em questão. Assim como , toma outras decisões acerca de cada Status Codes.


#### Formato dos Dados

O criador do REST API é quem decide em que formato ele será exibido. 

Os formatos mais comuns são JSON e XML, mas hoje em dia, as APIS possuem JSON como formato padrão, mas, em muitos casos, são fornecido ambos os formatos.


#### Documentação

A pesar de não existir nenhuma obrigação de ter documentação, ou até mesno um manual de como deve ser, é altamente **recomendavel criar uma documentação e seguir guias de boas práticas,**


#### Como o servidor identifica que tipo de formato de dados deve enviar? 

Através de um parametro do **HEADER,** chamado **Content-Type**.

Junto com a requisição para acessar um recurso, envia-se um header contendo informações necessárias. Essas informações são chamadas de **METADATA.**

**Content-Type**  é um tipo de Metadata que indica qual o formato que se espera do servidor. Existem alguns padrões predefinidos de valores do **Content-Type**

Para receber XML, usa-se txt/xml e para receber dados em JSON usa-se application/json
