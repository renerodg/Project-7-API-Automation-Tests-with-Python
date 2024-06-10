import copy
headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
"name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
}
def get_kit_body(name=None):
    kit_body = {}
    if name is not None:
        kit_body['name'] = name
    return copy.deepcopy(kit_body)