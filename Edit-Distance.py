class EditDistance:
    def __init__(self) -> None:
        pass

    def test(self) -> None:
        print("Hello")

    def minDistance(self, word1: str, word2: str) -> int:
        cols = len(word1)
        rows = len(word2)

        M = [[0 for col in range(cols)] for row in range(rows)]
        M[0][0] = 1

        for A in rows:
            for B in cols:
                if word1[A] == word2[B] and self.__isValid(A, B): 
                    M[A][B] = M[A-1][B-1]
                else:
                    M[A][B] = self.__getMin(M, A, B)
        return M[rows][cols]

    def __isValid(self, A: int, B: int) -> bool:
        return A > 0 and B > 0 

    def __getMin(self, M: list, A: int, B: int) -> int:
        if A-1 < 0:
            return M[0][B-1]
        if B-1 < 0:
            return M[A-1][0]
        return min(M[A-1][B], M[A][B-1])
    
ED = EditDistance()