def characters_count(words):
    numbers_count = 0
    alphabets_count = 0
    symbols_count = 0
    
    #ascii value of numbers is 48-57
    #ascii value of alphabets in capital letter 65-90
    #ascii value small alphabets 97-122
    for i in words:
        if ord(i) >= 48 and ord(i) <= 57:
            numbers_count += 1
        elif (ord(i) >= 65 and ord(i) <=90) or (ord(i) >=97 and ord(i) <= 122):
            alphabets_count += 1
        elif i != " ":
            symbols_count += 1
            
    print("numbers count ->",numbers_count)
    print("alphabets count->",alphabets_count)
    print("special characters->",symbols_count)
    
def word_count(words):
    words_list = words.split()
    words_set = set(words_list)
    for i in words_set:
        print(i,"->",words_list.count(i))

def reverse_sentence(words):
    words = words + " "
    output = ""
    word = ""
    for i in words:
        if i != " ":
            word += i
            continue
        output = word + " " + output
        word = ""
    print(output)
    # output = ""
    # words_list = words.split()
    # for i in words_list:
    #     output = i + " " + output
    # print(output)

def vowels_count(words):
    vowels_count = {}
    for i in words:
        if i.isalpha() and (i.lower() in ["a","e","i","o","u"]):
            i = i.lower()
            if i not in vowels_count:
                vowels_count[i] = 1
            else:
                vowels_count[i] += 1
    print(vowels_count)
    
def first_non_repeated_alphabet(words):
    words_list = words.split()
    
    for i in words_list:
        if len(i) == 1:
            print(i)
        elif i[0] not in i[1:]:
            print(i)
                
    
if __name__  == "__main__":
    words = "My name is Prasanth . Prasanth is a good boy pppp"
    print('---------- Character count ------------')
    characters_count(words)
    print()
    print('---------- word count -----------------')
    word_count(words)
    print()
    print("--------- Reverse a sentence-----------")
    reverse_sentence(words)
    print()
    print("----------Vowels count-----------------")
    vowels_count(words)
    print()
    print("----------Non repeated first character in a word------")
    first_non_repeated_alphabet(words)