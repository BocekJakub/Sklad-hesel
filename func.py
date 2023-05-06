import json
from typing import List


# function import datas (načtení databáze)
def import_db(data):
    with open(data, 'r') as file:
        return json.load(file)


# function save datas (uložení nové databáze)
def save_db(database):
    with open('data.json', 'w') as file:
        json.dump(database, file)


# create list (vytvoření listu podle klíče např. list názvů, list loginu atd.)
def list_cycle(data, key):
    list_passwords = []
    for i in range(0, len(data)):
        list_passwords.append(data[i][key])
    return list_passwords


# filter database by input (vyfiltruje novou databázi podle vstupu)
def filter_list(data, key):
    list_passwords = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i]['alias'])):
            if key in data[i]['alias'][j]:
                list_passwords.append(data[i])
    return list_passwords


# choice datas (výběr z filtrované databáze a výpis dat)
def choice_password(data, names):
    global login
    global password
    global note
    for i in range(0, len(data)):
        if data[i]['name'] == names:
            login = data[i]['name']
            password = data[i]['password']
            note = data[i]['note']
    return [login, password, note]


# find alias
def find_alias(new, data, key):
    new = list_cycle(filter_list(data, key), 'name')

# add new datas to database
def add_new_password(data, name, password, alias, note):
    new_data = {}
    new_data["alias"]: List[str] = []
    new_data["name"] = name
    new_data["password"] = password
    new_data["alias"] = alias
    new_data["note"] = note
    data.append(new_data)
    save_db(data)


# update password (úprava údaju u hesla)
# zatím není naprogramováno
def add_new_password(data, name, password, alias, note):
    new_data = {}
    new_data["alias"]: List[str] = []
    new_data["name"] = name
    new_data["password"] = password
    new_data["alias"] = alias
    new_data["note"] = note
    data.append(new_data)
    save_db(data)

# function search button
def action_with_arg(choice_list, data, input_box):
    choice_list['values'] = (list_cycle(filter_list(data, input_box.get()), 'name'))

# combobox search
def callback(self, choice_list):
    self.promena = choice_list.get()
    print(self.promena)
#test = import_db('data.json')
#enter = input("Hledej: ")
#new = list_cycle(filter_list(test, enter), 'name')
#print(new)
#enter2 = int(input("výběr hesla: "))
#choice_password(test, new, enter2)
