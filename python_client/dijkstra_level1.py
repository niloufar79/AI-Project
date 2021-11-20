from queue import PriorityQueue
from math import inf


def dijkstra(gridmap,height, width, agentx,agenty, scoredij,trap,character):
  array_distance = {}
  visited = {}
  distancelist = {}
  pq = PriorityQueue()
  pq.put((0, agentx, agenty, 0, scoredij))
  distancelist[(agentx, agenty)] = 0
  array_distance[(agentx, agenty)] = (0, scoredij)
  flag = False
  while not pq.empty():
      temp = pq.get()
      dist = temp[0]
      current_nodex = temp[1]
      current_nodey = temp[2]
      scoredij = temp[4]
      actual_dist = temp[3]
      visited[(current_nodex,current_nodey)] = True
      # print(dist,current_nodex,current_nodey)
      array_distance[(current_nodex,current_nodey)] = (actual_dist, scoredij)
      #up
      if (current_nodex-1 >= 0):
          if (current_nodex-1,current_nodey) in trap:
            flag = True
      if (current_nodex-1 >= 0) and ((current_nodex-1,current_nodey) not in visited) and (
         (gridmap[current_nodex-1][current_nodey] == 'E') or (gridmap[current_nodex-1][current_nodey] == 'T') or (gridmap[current_nodex-1][current_nodey] == "E"+character) or(gridmap[current_nodex-1][current_nodey] == "T"+character) or flag):

          if (current_nodex-1, current_nodey) not in distancelist:
              if flag:
                distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                pq.put((dist+41, current_nodex-1, current_nodey, dist+1, scoredij-41))
              else:
                  distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex - 1, current_nodey, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex-1, current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex - 1, current_nodey, dist+1, scoredij-41))
              else:
                  if dist + 1 < distancelist[(current_nodex-1, current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex - 1, current_nodey, dist+1, scoredij-1))
      #down

      if current_nodex + 1 < height:
          if (current_nodex + 1, current_nodey) in trap:
              flag = True
      if (current_nodex + 1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (
         (gridmap[current_nodex + 1][current_nodey] == 'E') or (gridmap[current_nodex + 1][current_nodey] == 'T') or (gridmap[current_nodex + 1][current_nodey] == 'E' + character) or (gridmap[current_nodex+1][current_nodey] == 'T' + character)  or flag):

          if (current_nodex + 1, current_nodey) not in distancelist:
              if flag:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                  pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))
      #left
      if(current_nodey - 1 >= 0):

          if (current_nodex,current_nodey-1) in trap:
              flag = True
      if (current_nodey - 1 >= 0) and ((current_nodex , current_nodey-1) not in visited) and (
         (gridmap[current_nodex][current_nodey-1] == 'E') or (gridmap[current_nodex][current_nodey-1] == 'T')or(gridmap[current_nodex][current_nodey-1]=="E"+character) or (gridmap[current_nodex][current_nodey-1]=="T"+character)  or flag):
          if (current_nodex , current_nodey-1) not in distancelist:
              if flag:
                  distancelist[(current_nodex , current_nodey-1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey-1, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey-1)] = dist + 1
                  pq.put((dist + 1, current_nodex , current_nodey-1, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 41
                      pq.put((dist + 41, current_nodex , current_nodey-1, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex , current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey-1, dist + 1, scoredij - 1))
      #right
      if current_nodey + 1 < width:
          if (current_nodex , current_nodey+1) in trap:
              flag = True
      if (current_nodey + 1 < width) and ((current_nodex, current_nodey+1) not in visited) and (
         (gridmap[current_nodex][current_nodey+1] == 'E') or (gridmap[current_nodex][current_nodey+1] == 'T') or (gridmap[current_nodex][current_nodey+1]=="E"+character)or (gridmap[current_nodex][current_nodey+1]=="T"+character) or flag):

          if (current_nodex, current_nodey + 1) not in distancelist:
              if flag:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                      pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))

  return array_distance