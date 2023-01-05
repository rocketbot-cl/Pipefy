# Pipefy
  
Módulo para automatizar Pipefy através de seu API  

*Read this in other languages: [English](Manual_Pipefy.md), [Español](Manual_Pipefy.es.md), [Portugues](Manual_Pipefy.pr.md).*
  
![banner](imgs/Banner_Pipefy.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Conectar ao pipefy
  
Com este comando, a autenticação contra o Pipefy é estabelecida
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando você se conectar com mais de uma conta|conta1|
|Token|Obtenha o token em https//app.pipefy.com/tokens|eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWls.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIeyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsa_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA|

### Criar Card
  
Com este comando pode-se criar uma card
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando se conecta com mais de uma conta|conta1|
|Id do Pipe|Obtenha o id na url do pipe|301741450|
|Campo de atributo|Lista de input para completar os campos da card. Você pode obter o field_id com o comando Obter Pipe por Id|[{ 'field_id': 'nome_do_solicitante','field_value': 'Lucas'},{'field_id': 'e_mail_do_solicitante','field_value': 'user@email.com'}]|
|Arquivo anexo|Caminho do arquivo para ser anexado à card|C:\User\Desktop\test.txt|
|Atribuir à variável|Nome do variável sem {}|variável|

### Obter Pipe por seu ID
  
Com este comando você pode obter informações sobre os campos de um pipe a partir de seu id
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando você se conectar com mais de uma conta|conta1|
|Id do Pipe|Obtenha o id na url do pipe|301741450|
|Atribuir à variável|Nome do variável sem {}|variável|
