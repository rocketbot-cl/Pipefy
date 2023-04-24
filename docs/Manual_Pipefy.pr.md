# Pipefy
  
Módulo para automatizar pipefy através de sua API. Permite criar cartões, movê-los, editá-los, etc.  

*Read this in other languages: [English](Manual_Pipefy.md), [Português](Manual_Pipefy.pr.md), [Español](Manual_Pipefy.es.md)*
  
![banner](imgs/Banner_Pipefy.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar ao pipefy
  
Com este comando você pode estabelecer a autenticação com Pipefy
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando você se conectar com mais de uma conta|conta1|
|Token|Obtenha o token em https//app.pipefy.com/tokens|eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWls.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIeyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsa_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA|
|Atribuir resultado a variável|Variável onde o resultado da conexão será salvo|result|

### Obter Pipe por seu ID
  
Com este comando você pode obter informações sobre os campos de um pipe a partir de seu id
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando você se conectar com mais de uma conta|conta1|
|Id do Pipe|Id do pipe que você deseja obter os campos. Você pode obter o id na url do pipe|301741450|
|Atribuir à variável|Variável onde o resultado da execução será armazenado|variável|

### Criar Card
  
Com este comando pode-se criar uma card
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando se conecta com mais de uma conta|conta1|
|Id do Pipe|Obtenha o id na url do pipe|301741450|
|Título da card|Título da card que será criada|Draft|
|Campo de atributo|Lista de input para completar os campos da card. Você pode obter o field_id com o comando Obter Pipe por Id|[{ 'field_id': 'nome_do_solicitante','field_value': 'Lucas'},{'field_id': 'e_mail_do_solicitante','field_value': 'user@email.com'}]|
|Arquivo anexo|Caminho do arquivo para ser anexado à card|C:\User\Desktop\test.txt|
|Atribuir à variável|Nome do variável sem {}|variável|

### Subir arquivo
  
Com este comando você pode enviar um documento para os servidores do Pipefy, ele retorna a URL do arquivo enviado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando você se conecta com mais de uma conta|conta1|
|Atribuir à variável|Nome do variável sem {}|variável|
|Arquivo anexo|Caminho do arquivo a ser anexado ao card|C:\User\Desktop\test.txt|

### Atualizar Card
  
Com este comando você pode atualizar uma card
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador para quando se conecta com mais de uma conta|conta1|
|Id da card|Obtenha o id na url do pipe|643648856|
|Novo título da card|Título que a card terá. Deixe em branco se não quiser alterá-lo|Draft|
|Id dos responsáveis|Array de ids de usuários para atribuir à card. Deixe em branco se não quiser alterá-lo|[307721335, 307721336, 307721337]|
|Data de vencimento|Data em que a card vencerá. Deixe em branco se não quiser alterá-lo|2023-02-15T16:30:00+00:00|
|IDs das etiquetas|Array de ids de etiquetas para atribuir à card. Deixe em branco se não quiser alterá-lo|[307721335, 307721336, 307721337]|
|Atribuir à variável|Nome do variável sem {}|variável|

### Mover card
  
Com este comando você pode mover um card de uma fase para outra dentro de um pipe. Você pode obter o ID da fase com o comando 'Obter Pipe por ID'
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do card|ID do card para mover|643648856|
|ID da fase|ID da fase para mover o card|643648856|
|Atribuir à variável|Nome do variável sem {}|variável|

### Excluir card
  
Com este comando você pode excluir um card do Pipefy
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do card|ID do card para excluir|643648856|
|Atribuir à variável|Nome do variável sem {}|variável|
