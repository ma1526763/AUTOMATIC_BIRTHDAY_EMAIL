import json
from birthday_wish_using_pandas import valid_email
from datetime import datetime

def add_birthday(name, email, birthday):
    if not name and not email and not birthday:
        print("Please Fill all the fields")
        return
    if not valid_email(email):
        print("Please enter valid email")
        return
    try:
        with open("birthday_data.json", "r+") as file:
            data = json.load(file)
            already_exist = False
            for mail_key in data:
                if mail_key == email:
                    already_exist = True
                    for birthday_data in data[mail_key]:
                        if birthday_data["birthday"] == birthday:
                            return print("A user with same email and birthday exist.")
            if already_exist:
                file.seek(0)
                data[mail_key].append({"name": name, "birthday": birthday})
                json.dump(data, file, indent=4)
            else:
                file.seek(0)
                data[email] = [{"name": name, "birthday": birthday}]
                json.dump(data, file, indent=4)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("birthday_data.json", "w") as file:
            data = {email: [{"name": name, "birthday": birthday}]}
            json.dump(data, file, indent=4)

def check_birthday():
    try:
        with open("birthday_data.json", "r+") as file:
            data = json.load(file)
            birthday_list = []
            today = datetime.now().strftime("%d-%m")
            for k, v in data.items():
                for birthday in v:
                    if birthday["birthday"][:-5] == today:
                        birthday_list.append({"name": birthday["name"], "email": k, "birthday": birthday["birthday"]})
            return birthday_list
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return False
