from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]) -> None:
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# t1 = ["getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# t1_param = [[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
# a1 = [1,None,100,100,None,20]

t1 = ["getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
t1_param = [[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
a1 = [1,None,100,100,None,20]

# obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
obj = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])

for c, p, a in (zip(t1, t1_param, a1) ):
    f = obj.__getattribute__(c)
    res = f(*p)
    assert res == a
