# Coleções de Recursos

O URI com recurso único, se chama instancia, e o URI contendo varios recursos, é chamado de coleções.


/postagens = coleção

/postagens/{ID} = instancia


Para as coleções de recursos, contamos com os query parameters.

Com a paginação, podemos determinar quantos elementos queremos exibir por página, através dos parametros de consulta: 

Limit e Offset

Limit => Não mais do que a quantidade limite elementos serão exibidas (possivelmente menos)

Offset => Quantidade de elementos que serão pulados, de forma que só aparecerão resultados posteriores ao valor de offset

Exemplo: 

/postagens?limit=10&offset=30

? => Aceitar parametros

& => Combinar parametros

limit=10 => Queremos no maximo 10 elementos por página

offset=30 => Vamos pular as 30 primeiras linhas do banco de dados, entaão vamos receber os dados da linha 31 a linha 40


Uma coleçao deve conter os nomes no substantivo e no plural.

Ex:  /postagens, /comentarios, /curtidas

Nunca usar verbos no infinitivo: /postar, /comentar, /curtir
