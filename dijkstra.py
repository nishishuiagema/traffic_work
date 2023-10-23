MAX = float('inf') # 无穷大
matrix = [[0, MAX, MAX, MAX, 2.8, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, 0, 0.96, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, 0.96, 0, 2.9, 2.9, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.8, MAX, MAX],
          [MAX, MAX, 2.9, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [2.8, MAX, 2.9, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, 0, 2.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.5, 1.5, MAX, MAX, MAX, MAX, MAX, 2.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.9, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, 2.5, 0, MAX, MAX, MAX, 1.4, MAX, MAX, 0.6, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, MAX, 1.9, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, 1.6, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.9, 1.6, 0, 3.0, 2.0, MAX, 4.6, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, 1.4, MAX, MAX, 3.0, 0, 2.0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.6, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.0, 2.0, 0, MAX, MAX, 3.7, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, MAX, 2.5, MAX, 1.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, 0.6, MAX, MAX, 4.6, MAX, MAX, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, 2.5, MAX, MAX, MAX, MAX, MAX, 3.7, 2.5, MAX, 0, MAX, MAX, MAX, 1.1, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, 1.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, MAX, MAX, 2.1, MAX, 1.7, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.5, MAX, MAX, MAX, 0, MAX, 1.7, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0.95, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.6, 1.2, 2.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.1, 2.1, 1.7, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.6, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, 1.5, MAX, MAX, MAX, MAX, MAX, 2.1, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.7, MAX, MAX, MAX, 1.5, 0, MAX, MAX, 2.0, MAX, 1.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, 2.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, 1.6, MAX, 1.8, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.6, 0, MAX, MAX, 2.3, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.5, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.0, MAX, MAX, 0, 0.74, MAX, MAX, 1.3, MAX, MAX, 2.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.8, MAX, 0.74, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.5, MAX, 2.3, MAX, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.2, 0.8],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.2, 2.1, MAX, MAX, MAX, MAX, MAX, MAX, 0, 0.52, 1.4, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.6, MAX, MAX, MAX, MAX, MAX, 1.3, MAX, MAX, 0.52, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0.95, 1.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.4, MAX, 0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, 2.0, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.5, MAX, MAX, MAX, MAX, MAX, 2.0, 0, 2.0, 1.4, MAX, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.0, 0, 3.0, 4.1, MAX, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.4, 3.0, 0, MAX, 1.5, MAX, MAX, MAX, MAX, 3.0],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 4.1, MAX, 0, 1.0, MAX, MAX, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.5, 1.0, 0, 2.4, 3.7, MAX, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 2.4, 0, MAX, MAX, 3.0, 3.2],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 3.7, MAX, 0, MAX, 0.96, MAX],
          [MAX, MAX, 1.8, MAX, MAX, 2.9, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.5, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0, MAX, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 1.2, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 3.0, 0.96, MAX, 0, MAX],
          [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX, 0.8, MAX, MAX, MAX, MAX, MAX, MAX, 3.0, MAX, MAX, 3.2, MAX, MAX, MAX, 0]]
          #节点间距离


def dijkstra(matrix, start, stop):
    N = [start] # 存储经过的点
    position=[] # 存储最短路径
    distance = matrix[start-1].copy() # 初始临时距离


    while len(N) < 40:
        Distance = distance.copy()
        for i in N:
            Distance[i - 1] = MAX
        t = Distance.index(min(Distance[1:])) # 寻找临时距离中最小值
        for i in range(len(matrix[t])):
            if matrix[t][i] < MAX:
                if (distance[t] + matrix[t][i]) < distance[i]: # 更新临时距离
                    distance[i] = distance[t] + matrix[t][i]
        N.append(t + 1)


    temp = stop - 1
    while temp != start-1: # 回溯最短路径
        for i in range(len(distance)):
            if distance[i] + matrix[i][temp] == distance[temp]:
                position.append(i+1)
                temp = i
    position.reverse()


    if stop not in position:
        position.append(stop)
    for i in range(len(position)):
        position[i] -= 1


    return distance[stop-1], position
