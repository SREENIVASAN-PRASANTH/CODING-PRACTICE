def adding_numbers_and_words(word_chunks_list, sorted_numbers_list):
    reordered_sentence = ''
    for each_word in word_chunks_list:
        reordered_sentence += each_word
        if len(sorted_numbers_list) != 0:
            reordered_sentence += str(sorted_numbers_list.pop())   
    return reordered_sentence
    
def get_number_end_index(sentence, start_index):
    end_index = len(sentence)
    for j in range(start_index, len(sentence)):
        if not sentence[j].isdigit():
            end_index = j
            break
    return end_index
    
def get_word_chunks_and_numbers_list(sentence):
    word_chunks_list, numbers_list = [], []
    i = 0
    while i < len(sentence):
        number = ""
        if sentence[i].isdigit():
            start_index = i
            end_index = get_number_end_index(sentence, start_index)  
            number = int(sentence[start_index:end_index])
            word_chunk = sentence[:start_index]
            numbers_list.append(number)
            word_chunks_list.append(word_chunk)
            sentence = sentence[end_index:]
            i = 0
        else:
            i += 1
    word_chunks_list.append(sentence)
    return word_chunks_list, numbers_list
    
def get_reordered_string(sentence):
    word_chunks_list, numbers_list = get_word_chunks_and_numbers_list(sentence)
    sorted_numbers_list = sorted(numbers_list, reverse=True)
    reordered_sentence = adding_numbers_and_words(word_chunks_list, sorted_numbers_list)
    return reordered_sentence

def main():
    sentence = input()
    reordered_sentence = get_reordered_string(sentence)
    print(reordered_sentence)
    
main()