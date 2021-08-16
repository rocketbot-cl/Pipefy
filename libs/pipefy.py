import requests
import os


def removeQuotes(dictionary: dict):
    result = "{"
    for key, value in dictionary.items():
        if isinstance(value, str) and not value.startswith(("[", "{")):
            value = "\"" + str(value) + "\""
        result += key + ":" + str(value) + ","
    return result[:-1] + "}"


class Pipefy:

    def __init__(self, token):
        self.api_url = "https://api.pipefy.com/graphql"
        self.token = token

    def get_all_cards(self, pipe_id: int, options: str = None) -> dict:
        query = "{allCards(pipeId:pipe_id) options}".replace(
            "pipe_id", str(pipe_id)).replace("options", str(options))

        return self.__requests("post", query)

    def get_pipe_by_id(self, pipe_id: int, options: str) -> dict:

        query = "{pipe(id:pipe_id) options}".replace(
            "pipe_id", str(pipe_id)).replace("options", str(options))
        
        return self.__requests("post", {"query": query})

    def create_card(self, pipe_id: int, fields_attributes: list, options: str = "{clientMutationId,card{id}}", upload_attachments: str = "") -> dict:
        fields_without_quote = "["
        for field in fields_attributes:
            fields_without_quote += removeQuotes(field) + ","
        fields_without_quote += "]"

        
        input_args = {"pipe_id": pipe_id,
                      "fields_attributes": fields_without_quote}
        if upload_attachments:
            filename = self.upload_file(upload_attachments)
            input_args["attachments"] =  filename
        input_args = removeQuotes(input_args)
        query = "mutation{createCard(input:input_args) options}".replace(
            "input_args", input_args).replace("options", options)
        
        return self.__requests("post", {"query": query})

    def upload_files(self, attachments: list):
        for attachment in attachments:
            if os.path.isfile(attachment):
                self.upload_files(attachment)

    def upload_file(self, file: str) -> str:
        filename = os.path.basename(file)
        url = f"https://app.pipefy.com/upload_attachments/new?objectName={filename}"
        request = requests.request("get", url)
        response = request.json()
        res = requests.request("put", response["signedUrl"], data=open(file, 'rb'))
        
        return response["filename"]

    def __requests(self, method: str, query: dict = {}) -> dict:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.request(
            method, self.api_url, json=query, headers=headers)
        return response.json()


pipefy = Pipefy("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIjoiZGFuaWxvLnRvcm9Acm9ja2V0Ym90LmNvbSIsImFwcGxpY2F0aW9uIjozMDAxMDcxODF9fQ.waS9k2ekcQq5xkQ5JU63vfNiv2VXTyHmSmsPX4ulQ1WnVwRz7Dka_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA")

# print(pipefy.get_all_cards(301741450,"{edges {node {id,assignees {id}}}}"))
# print(pipefy.get_pipe_by_id(301741450,"{start_form_fields {id, label}}"))
print(pipefy.create_card(301741450, [{"field_id": "nome_do_solicitante", "field_value": "Danilo2"}, {"field_id": "e_mail_do_solicitante", "field_value": "Danilo@rocketbot.com"}, {
      "field_id": "tipo_de_contrato", "field_value": "Indeterminado"}, {"field_id": "contrato_j_criado", "field_value": "Sim"}], upload_attachments="C:/Users/danil/Downloads/RPA_Integration.pdf"))
