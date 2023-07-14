def count_subsequence_AG(A):
    count = 0
    n = len(A)

    for i in range(n - 1):
        if A[i] == 'A':
            for j in range(i + 1, n):
                if A[j] == 'G':
                    count += 1

    return count


A = input("Enter the string A: ")

output = count_subsequence_AG(A)
print("Number of times 'AG' appears:", output)