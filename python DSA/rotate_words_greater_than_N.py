def rotate_words_greater_N(sentence_list,N,rotation):
    after_rotation = []
    for i in sentence_list:
        if len(i) > N:
            i = rotate_words(i,rotation)
            after_rotation.append(i)
        else:
            after_rotation.append(i)
    return after_rotation

def rotate_words(word,rotation):
    rotation_dup = rotation
    length = len(word)
    rotation_dup %= length
    return (word[-rotation_dup:] + word[:-rotation_dup])


def main():
    sentence_list = input().split()
    N,rotation = tuple(map(int,input().split()))
    output = rotate_words_greater_N(sentence_list,N,rotation)
    output = " ".join(map(str,output))
    print(output)
main()