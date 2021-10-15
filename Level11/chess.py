
def drawMap(ChessMap, x, y):
    cmp1 = "BWBWBWBW"
    cmp2 = "WBWBWBWB"
    map1 = [cmp1, cmp2, cmp1, cmp2, cmp1, cmp2, cmp1, cmp2]  # black이 먼저인 체스판
    map2 = [cmp2, cmp1, cmp2, cmp1, cmp2, cmp1, cmp2, cmp1]  # white가 먼저인 체스판
    min = 0

    for i_y in range(y - 8 + 1):  # 8 x 8 # map 탐색
        for i_x in range(x - 8 + 1):
            cnt = 0
            for j_y in range(8):
                for j_x in range(8):
                    if(ChessMap[i_y + j_y][i_x + j_x] != map1[j_y][j_x]):
                        cnt += 1
            if (min < cnt):
                min = cnt
            cnt = 0
            for j_y in range(8):
                for j_x in range(8):
                    if(ChessMap[i_y + j_y][i_x + j_x] != map2[j_y][j_x]):
                        cnt += 1
            if (min < cnt):
                min = cnt
    return (min)


y, x = map(int, input().split())
ChessMap = []
for i in range(y):
    ChessMap.append(list(input()))
print(drawMap(ChessMap, x, y))
