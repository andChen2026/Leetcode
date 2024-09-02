class EditDistance:
    def __init__(self) -> None:
        pass

    @staticmethod
    def minDistance(self, word1: str, word2: str) -> int:
        cols = len(word1)
        rows = len(word2)

        M = [[0 for col in range(cols)] for row in range(rows)]
        M[0][0] = 1

        for A in rows:
            for B in cols:
                if word1[A] == word2[B] and self.isValid(A, B): 
                    M[A][B] = M[A-1][B-1]
                else:
                    M[A][B] = self.getMin(M, A, B)
        return M[rows][cols]

    def isValid(self, A: int, B: int) -> bool:
        return A > 0 and B > 0 

    def getMin(self, M: list, A: int, B: int) -> int:
        if A-1 < 0:
            return M[0][B-1]
        if B-1 < 0:
            return M[A-1][0]
        return min(M[A-1][B], M[A][B-1])
    
minDist: int = EditDistance.minDistance("hello", "hi")
print(minDist)