import numpy as np

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    D = np.zeros((m+1, n+1))
    D.fill(-1 * np.Inf)
    D[0, :] = 0
    D[:, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:  # match, add 1 to lcs
                D[i][j] = D[i-1][j-1]+1
            else: # no match, take the best value from above or left
                D[i][j] = max(D[i-1][j] , D[i][j-1])

    return D[m][n]

if __name__ == "__main__":
    import pylcs
    import string
    import random
    
    letters = string.ascii_letters
    for _ in range(1000):
        s1 = ''.join(random.choice(letters) for i in range(random.randint(1, 100)))
        s2 = ''.join(random.choice(letters) for i in range(random.randint(1, 100)))

        assert lcs(s1, s2) == pylcs.lcs(s1, s2)
    print("All test cases matched the reference implementation")
