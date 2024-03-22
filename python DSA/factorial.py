def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    
def main():
    n = int(input())
    if 1 <= n <=15:
        output = factorial(n)
        print(output)
        
main()