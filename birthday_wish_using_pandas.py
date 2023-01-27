import pandas
from validate_email import validate_email
from datetime import datetime

COLUMNS = ["name", "email", "birthday"]

def valid_email(mail):
    return False if not validate_email(mail) or mail[-9:] not in ["gmail.com", "yahoo.com"] else True

def upload_data_to_file(data):
    data_frame = pandas.DataFrame(columns=COLUMNS, data=data)
    data_frame.to_csv("birthdays_data.csv", index=False)

def get_birthday_list():
    try:
        birthday_data = pandas.read_csv("birthdays_data.csv")
        birthday_data_list = birthday_data.to_dict(orient="records")
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        return False
    return birthday_data_list

def add_birthday(name, email, birthday):
    if not name or not email or not birthday:
        print("Please complete data in all fields")
        return
    if not valid_email(email):
        print("Please enter valid email")
        return

    birthday_data_list = get_birthday_list()
    if not birthday_data_list:
        new_birthday = [{"name": name, "email": email, "birthday": birthday}]
        upload_data_to_file(new_birthday)
    else:
        new_birthday = {"name": name, "email": email, "birthday": birthday}
        if new_birthday in birthday_data_list:
            print(f"\"{name}\" with same mail({email}) and birthday({birthday}) already exists.")
            return
        birthday_data_list.append(new_birthday)
        upload_data_to_file(birthday_data_list)

def check_birthday():
    birthday_data_list = get_birthday_list()
    if birthday_data_list:
        today = str(datetime.now().strftime("%d-%m"))
        today_birthday = [birthday for birthday in birthday_data_list if birthday["birthday"][:-5] == today]
        return today_birthday if today_birthday else False
