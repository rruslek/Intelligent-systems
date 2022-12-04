import yaml

objects = []
with open('code.yaml', encoding="utf8") as fh:
    dictionary_data = yaml.safe_load(fh)
    for k, v in dictionary_data.items():
        objects.append(v)

entities = []
for k in range(len(objects)):
    for kk, vv in objects[k].items():
        if (kk == 'source'):
            check = vv in entities
            if (check == False):
                entities.append(vv)


print('СПИСОК СУЩНОСТЕЙ:')
for e in entities:
    print(e)

entity = input("\nВыберите сущность из списка: ")

questions = []

for k in range(len(objects)):
    quest = False
    for kk, vv in objects[k].items():
        if (vv == entity):
            quest = True
            continue
        if (quest == True):
            questions.append(vv)
            break

print("\nСПИСОК ВОПРОСОВ: ")
for i in questions:
    print(i)
question = input("\nВыберите вопрос из списка: ")

for k in range(len(objects)):
    quest = False
    answer = False
    for kk, vv in objects[k].items():
        if (vv == entity):
            quest = True
            continue
        if (quest == True and vv == question):
            answer = True
            continue
        if (answer == True):
            result = vv
            break

print("\nОТВЕТ:")
if (type(result) == list):
    for i in result:
        print(i)
else:
    print(answer)