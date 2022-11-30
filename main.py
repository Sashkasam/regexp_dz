import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)


phone_pattern = r'(8|\+7)[\s\(]*(\d{3})[\-\)\s]*(\d{3})[\-]*(\d{2})[\-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)\3-\4-\5 \6\7'


new_contacts_list = list()
for i in contacts_list:
    full_name = ' '.join(i[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], i[3], i[4], re.sub(phone_pattern, phone_sub, i[5]), i[6]]
    new_contacts_list.append(result)


new_contacts_list2 = list()
for contacts in new_contacts_list:
   for i in new_contacts_list:
      if contacts[0] == i[0] and contacts[1] == i[1]:
        if contacts[2] == '':
           contacts[2] = i[2]
        if contacts[3] == '':
           contacts[3] = i[3]
        if contacts[4] == '':
           contacts[4] = i[4]
        if contacts[5] == '':
           contacts[5] = i[5]
        if contacts[6] == '':
           contacts[6] = i[6]
           
for people in new_contacts_list:
   if people not in new_contacts_list2:
      new_contacts_list2.append(people)       




with open("phonebook.csv", "w", encoding='utf8' ) as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list2)