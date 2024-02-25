from itertools import combinations

strings = input("Enter the strings: ").split()
strings.sort()

N = int(input("Enter the no.of combinations: "))
indexes = list(range(len(strings)))

combination = list(combinations(indexes,N))

unique_combinations = set()

for i in combination:
    diff_combiations = ""
    for j in range(len(i)):
        diff_combiations += strings[i[j]] + " "
    unique_combinations.add(diff_combiations)

unique_combinations = list(unique_combinations)
unique_combinations.sort()

for i in unique_combinations:
    print(i)
