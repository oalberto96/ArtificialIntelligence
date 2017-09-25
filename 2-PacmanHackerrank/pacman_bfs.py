#!/usr/bin/python

'''
Sample input
3 9
5 1
7 20
%%%%%%%%%%%%%%%%%%%%
%--------------%---%
%-%%-%%-%%-%%-%%-%-%
%--------P-------%-%
%%%%%%%%%%%%%%%%%%-%
%.-----------------%
%%%%%%%%%%%%%%%%%%%%
'''

class Graph:
    def __init__(self):
        self.nodes = {}

    def maze_to_graph(self, r_grid_size, c_grid_size, pacman_r, pacman_c, food_r, food_c, maze):
        empty_spaces = []
        Edges = []
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
    def nodes_sort(self):
        pass

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

    def DFSsearch(self, vertex,visited):
        frontier = [self.start]
        visited = []
        while frontier:
            state = frontier.pop()
            visited.append(state)
            if state == self.goal:
                print(len(visited))
                for v in visited:
                    x,y = v
                    print(str(x) + " " + str(y))
                print(len(visited)-1)
                for v in visited:
                    x,y = v
                    print(str(x) + " " + str(y))
                return True
            for neighbor in self.nodes[state]:
                if neighbor not in frontier and neighbor not in visited:
                    frontier.append(neighbor)


def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    graph = Graph()
    graph.maze_to_graph(r, c, pacman_r, pacman_c, food_r, food_c, grid)
    visited_nodes = []
    start = (pacman_r,pacman_c)
    graph.DFSsearch(start,visited_nodes)
    return



readfile = True
grid = []
if readfile:
    text = open("maze.txt","r")
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

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)
