def naive_algorithm(text,pattern):
    M = len(text)
    N = len(pattern)
    
    for i in range(0,M-N+1):
        count = 0
        for j in range(0,N):
            count += 1
            if (text[i + j] != pattern[j]):
                break
            
        if count == N:
                print("Pattern found at index",i)

def main():
    text = input()
    pattern = input()
    naive_algorithm(text,pattern)

main()