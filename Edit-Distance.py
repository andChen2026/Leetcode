class EditDistance:
    def __init__(self) -> None:
        print("Instantiated...")

    def minDistance(self, word1: str, word2: str) -> int:
        cols = len(word1) 
        rows = len(word2) 

        M = [[0 for col in range(cols)] for row in range(rows)]

        for A in range(0, rows):
            for B in range(0, cols):
                cW1, cW2 = word1[B], word2[A]
                M[A][B] = self.__getValS(M, A, B) if cW1 == cW2 else self.__getValD(M, A, B)
        return M[rows][cols]

    def __getValS(self, M: list, A: int, B: int) -> int:
        if A == 0 and B == 0:
            return 0
        elif A == 0:
            return M[A][B-1]
        elif B == 0:
            return M[A-1][B]
        return M[A-1][B-1]
    
    def __getValD(self, M: list, A: int, B: int) -> int:
        if A == 0 and B == 0:
            return 1
        elif A == 0:
            return M[0][B-1] + 1
        elif B == 0:
            return M[A-1][0] + 1
        return min(M[A-1][B], M[A][B-1]) + 1
    
ED = EditDistance()
print(ED.minDistance("horse", "rose"))