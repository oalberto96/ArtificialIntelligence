#!/usr/bin/python
from collections import deque

class Graph:
    def __init__(self):
        self.nodes = {}

    def maze_to_graph(self, r_grid_size, c_grid_size, pacman_r, pacman_c, food_r, food_c, maze):
        self.start = (pacman_r,pacman_c)
        self.goal = (food_r,food_c)
        for r,line in enumerate(maze):
            for c,char in enumerate(line):
                vertex = (r,c)
                if char == '%':
                    continue
                if r<r_grid_size-1 and maze[r+1][c] != '%':
                    self.add_edge((vertex,(r+1,c)))
                if c<c_grid_size-1 and maze[r][c+1] != '%':
                    self.add_edge((vertex,(r,c+1)))

    def add_edge(self, vertex):
        vertex1,vertex2 = vertex
        edge = []
        if vertex1 in self.nodes:
            edge = self.nodes[vertex1]
            edge.append(vertex2)
        else:
            edge.append(vertex2)
            self.nodes[vertex1] = edge
        edge = []
        if vertex2 in self.nodes:
            edge = self.nodes[vertex2]
            edge.append(vertex1)
        else:
            edge.append(vertex1)
            self.nodes[vertex2] = edge

    def get_path(self,parent, start, goal):
        path = [goal]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def deleteMin(self, list, dest_node):
        '''
        Funcion que regresa el nodo con menor coste segun la
        siguiente formula:
            Cost = d(s,c) + h(c)
        '''
        min_cost = self.manhattan_distance(list[0], dest_node)
        min_item = list[0]
        for item in list:
            cost = self.manhattan_distance(item,dest_node)
            if cost < min_cost:
                min_cost = cost
                min_item = item
        return list.pop(list.index(min_item))

    def manhattan_distance(self,source,dest_node):
        return abs(source[0] - dest_node[0]) + abs(source[1] - dest_node[1])

    def ASTARsearch(self, start):
        frontier = [start]
        explored = []
        parent = {}
        while frontier:
            state = self.deleteMin(frontier, self.goal)
            explored.append(state)
            if state == self.goal:
                path = self.get_path(parent,self.start,self.goal)
                print(len(path)-1)
                for v in path:
                    x,y = v
                    print(str(x) + " " + str(y))
                return True
            for neighbor in self.nodes[state]:
                if neighbor not in frontier and neighbor not in explored:
                    parent[neighbor] = state
                    frontier.append(neighbor)
                #elif neighbor in frontier:
                    #frontier.decreaseKey(neighbor)

def a_star( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    graph = Graph()
    graph.maze_to_graph(r, c, pacman_r, pacman_c, food_r, food_c, grid)
    start = (pacman_r,pacman_c)
    graph.ASTARsearch(start)

readfile = True
grid = []
if readfile:
    text = open("maze3.txt","r")
    pacman_r, pacman_c = [ int(i) for i in text.readline().strip().split() ]
    food_r, food_c = [ int(i) for i in text.readline().strip().split() ]
    r,c = [ int(i) for i in text.readline().strip().split() ]
    for i in range(0, r):
        grid.append(text.readline().strip())
else:
    pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
    food_r, food_c = [ int(i) for i in input().strip().split() ]
    r,c = [ int(i) for i in input().strip().split() ]
    for i in range(0, r):
        grid.append(input().strip())

a_star(r, c, pacman_r, pacman_c, food_r, food_c, grid)
