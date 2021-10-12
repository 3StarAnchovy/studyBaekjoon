
def inputXY():
    y, x = map(int, input().split())
    ChessMap = []
    for i in range(y):
        ChessMap.append(list(input()))
    print(ChessMap)


def drawMap(ChessMap, x, y):
    cmp1 = "BWBWBWBW"
    cmp2 = "WBWBWBWB"
    min = 0
    cnt = 0
    
    for i_y in range(y - 8): # 8 x 8
        for i_x in range(x - 8):
            
    return (min)


inputXY()
drawMap(ChessMap, x, y)
