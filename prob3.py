"""You are given an integer n.

You must print all integers from 1 to n without spaces, on a single line.

You are not allowed to use string methods (like join(), str.replace(), etc.)."""
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n + 1):
        print(i, end="")