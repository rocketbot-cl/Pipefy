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
    
    def create_card(self, pipe_id: int, fields_attributes: list, title: str = "Draft",  options: str = "{clientMutationId,card{id}}", upload_attachments: str = "") -> dict:
        fields_without_quote = "["
        for field in fields_attributes:
            fields_without_quote += removeQuotes(field) + ","
        fields_without_quote += "]"

        
        input_args = {"pipe_id": pipe_id,
                      "fields_attributes": fields_without_quote,
                      "title": title
                      }
        if upload_attachments:
            filenames = self.upload_file(upload_attachments)
            print("Files to attach",filenames)
            input_args["attachments"] =  filenames
        input_args = removeQuotes(input_args)
        query = "mutation{createCard(input:input_args) options}".replace(
            "input_args", input_args).replace("options", options)
        print("query", query.replace("'","\""))
        return self.__requests("post", {"query": query})

    def upload_files(self, attachments: list):
        filenames = []
        for attachment in attachments:
            if os.path.isfile(attachment):
                filenames.append(self.upload_file(attachment))
        return filenames

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
        print(response)
        return response.json()

    # def delete_card(self, card_id):
    #     query = "mutation{deleteCard(input:{card_id}) {success}}".replace("{card_id}", "{id: " + str(card_id) + "}")
    #     print(query)
    #     return self.__requests("post", query)
