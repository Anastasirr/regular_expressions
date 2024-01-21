import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern = r'\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб.)?\s?(\d{4})?\)?'
sub_pattern = r'+7(\2)\3-\4-\5 \6\7'


# помещение ФИО в поля таблицы, приведение телефонов к нужному формату
def add_notebook(contact_list: list):
  new_list = list()
  for item in contact_list:
    full_name = ' '.join(item[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
              re.sub(pattern, sub_pattern, item[5]),
              item[6]]
    new_list.append(result)
  return remove_pub_wr_con(new_list)


# удаление дубликатов и запись контактов в новый лист
def remove_pub_wr_con(contacts):
  contact_dict = {}
  for contact in contacts:
    first_name = contact[0]
    last_name = contact[1]
    if (first_name, last_name) in contact_dict:
      existing_contact = contact_dict[(first_name, last_name)]
      for i in range(2, len(contact)):
        if contact[i] != "":
          existing_contact[i] = contact[i]
    else:
      contact_dict[(first_name, last_name)] = contact

  new_contacts = list(contact_dict.values())
  return new_contacts


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(add_notebook(contacts_list))

