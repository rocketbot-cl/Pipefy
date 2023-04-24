import requests
import os
import json


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
        self.valid = False
        self.getValid()

    def getValid(self):
        '''
            Metodo para validar la API Key
        '''
        try:
            url = self.api_url
            payload = {"query": "{ me { id email } }"}
            headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.token}"
            }
            
            r = requests.post(url, json=payload, headers=headers)

            if r.status_code == 200:
                self.valid = True
            else:
                self.valid = False

        except Exception as exc:
            raise exc


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
        print(response)
        res = requests.request("put", response["signedUrl"], data=open(file, 'rb'))
        result = response["baseUrl"] + '/' + response["filename"]
        return result

    def __requests(self, method: str, query: dict = {}) -> dict:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.request(
            method, self.api_url, json=query, headers=headers)
        return response.json()

    def delete_card(self, card_id):
        # query = f"mutation {{ deleteCard(input: {{ id: {card_id} }}) {{ success }}}}"
        query = 'mutation { deleteCard(input: { id: %(id)s }) { %(response_fields)s }}' % {
            'id': card_id,
            'response_fields': "success",
        }
        return requests.post(self.api_url, json={"query": query}, headers={"Authorization": f"Bearer {self.token}"}).json()

    def update_card(self, card_id, title=None, due_date=None, assignee_ids=[], label_ids=[]):
        if due_date:
            query = '''mutation {
                updateCard(
                    input: {
                    id: %(id)s
                    title: %(title)s
                    due_date: "%(due_date)s"
                    assignee_ids: [ %(assignee_ids)s ]
                    label_ids: [ %(label_ids)s ]
                    }
                ) { %(response_fields)s }
                }''' % {
                'id': json.dumps(card_id),
                'title': json.dumps(title),
                'due_date': due_date,
                'assignee_ids': ', '.join([json.dumps(id) for id in assignee_ids]) if assignee_ids else json.dumps(assignee_ids),
                'label_ids': ', '.join([json.dumps(id) for id in label_ids]) if label_ids else json.dumps(label_ids),
                'response_fields': 'card { id title }'
            }
        else:
            query = '''mutation {
                updateCard(
                    input: {
                    id: %(id)s
                    title: %(title)s
                    assignee_ids: [ %(assignee_ids)s ]
                    label_ids: [ %(label_ids)s ]
                    }
                ) { %(response_fields)s }
                }''' % {
                'id': json.dumps(card_id),
                'title': json.dumps(title),
                'assignee_ids': ', '.join([json.dumps(id) for id in assignee_ids]) if assignee_ids else json.dumps(assignee_ids),
                'label_ids': ', '.join([json.dumps(id) for id in label_ids]) if label_ids else json.dumps(label_ids),
                'response_fields': 'card { id title }'
            }
        return requests.post(self.api_url, json={"query": query}, headers={"Authorization": f"Bearer {self.token}"}).json()
    
    def move_card_to_phase(self, card_id, destination_phase_id):
        """ Move card to phase: Mutation to move a card to a phase, in case of success a query is returned. """

        response_fields = 'card{ id current_phase { name } }'
        query = '''
            mutation {
              moveCardToPhase(
                input: {
                  card_id: %(card_id)s
                  destination_phase_id: %(destination_phase_id)s
                }
              ) { %(response_fields)s }
            }
        ''' % {
            'card_id': json.dumps(card_id),
            'destination_phase_id': json.dumps(destination_phase_id),
            'response_fields': response_fields,
        }
        return requests.post(self.api_url, json={"query": query}, headers={"Authorization": f"Bearer {self.token}"}).json()