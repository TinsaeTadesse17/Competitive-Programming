# Problem: C - Avoid Trygub - https://codeforces.com/gym/543431/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    string =  input()
    
    print(''.join(sorted(string)))