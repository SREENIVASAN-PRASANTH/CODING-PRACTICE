def read_inputs(no_of_persons):
    names_list, incomes_list = [], []
    for i in range(no_of_persons):
        each_entry = input().split()
        name = " ".join(each_entry[:len(each_entry) - 1])
        income = int(each_entry[-1])
        names_list.append(name)
        incomes_list.append(income)
    return names_list, incomes_list

def get_formatted_name(name):
    name = "".join(name.split())
    name = name.lower()
    return name

def get_persons_dict(names_list, incomes_list):
    persons_dict = dict()
    for i in range(len(names_list)):
        name = get_formatted_name(names_list[i])
        if name not in persons_dict.keys():
            persons_dict[name] = incomes_list[i]
        else:
            persons_dict[name] += incomes_list[i]
    return persons_dict

def get_richest_person_name(persons_dict):
    max_income = max(persons_dict.values())
    richest_persons_name_list = []
    for each_person in persons_dict.keys():
        if (persons_dict[each_person] == max_income):
            richest_persons_name_list.append(each_person)
    richest_persons_name_list.sort()
    return richest_persons_name_list[0]

def print_richest_person_first_entry(names_list, richest_person_name):
    for i in range(len(names_list)):
        name = get_formatted_name(names_list[i])
        if (name == richest_person_name):
            print("The highest income person name and index = " + names_list[i] + " " + str(i))
            break
        
def main():
    no_of_persons = int(input("Enter the no.of persons: "))
    names_list, incomes_list = read_inputs(no_of_persons)
    persons_dict = get_persons_dict(names_list, incomes_list)
    richest_person_name = get_richest_person_name(persons_dict)
    print_richest_person_first_entry(names_list, richest_person_name)

main()