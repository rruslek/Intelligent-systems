import json

print("Экспертная система - рекомендация по выбору языка программирования\n")


def check_rule(rule):
    conditions = rule["conditions"]
    for set in conditions:
        do = True
        if 'not' in set:
            not_conditions = set["not"][0]
            for cond in not_conditions:
                if not_conditions[cond] == facts[cond]:
                    do = False
            for cond in set:
                if cond != 'not':
                    if set[cond] != facts[cond]:
                        do = False
        else:
            for cond in set:
                if set[cond] != facts[cond]:
                    do = False
    return do


def do_rule(rule):
    if rule["function"] == 'yes-or-no':
        yes_or_no(rule["question"], rule["conclusion"])
    if rule["function"] == 'ask-value':
        ask_value(rule["question"], rule["conclusion"])
    if rule["function"] == 'check-time':
        check_time(rule["conclusion"])
    if rule["function"] == 'get-solution':
        get_solution(rule["result"], rule["conclusion"])


def yes_or_no(question, conclusion):
    okay = False
    while not okay:
        answer = input(question)
        if answer == "yes" or answer == "Yes" or answer == "Y" or answer == "y":
            answer = "yes"
            facts[conclusion] = answer
        if answer == "no" or answer == "No" or answer == "N" or answer == "n":
            answer = "no"
            facts[conclusion] = answer
        if answer != "yes" and answer != "no":
            print("Ответьте, пожалуйста, нормально: yes - если да, no - если нет.")
        else:
            okay = True


def ask_value(question, conclusion):
    answer = int(input(question))
    facts[conclusion] = answer


def check_time(conclusion):
    time = int(facts["time"])
    if time > 3:
        facts[conclusion] = ">3"
    else:
        facts[conclusion] = "<3"
    facts["time"] = None
    print(facts)


def get_solution(result, conclusion):
    facts[conclusion] = result


with open('data.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

rules = data["Rules"]
facts = data["Facts"][0]

solution = None

while solution is None:
    rule_found = False
    for rule in rules:
        rule_found = check_rule(rule)
        if rule_found:
            break
    do_rule(rule)
    solution = facts["solution"]

print("\nРекомендуемый язык для изучения:\n" + str(solution))
