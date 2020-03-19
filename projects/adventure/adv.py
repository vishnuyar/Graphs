from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def room_recursive(starting_room,room_graph,room_dict=None,visit_list=None):
    if visit_list is None:
        visit_list = []
    if room_dict is None:
        room_dict = {}
    room_no = starting_room.id
    if room_no not in room_dict.keys():
        visit_list.append(room_no)
        room_dict[room_no] = {}
        directions = starting_room.get_exits()
        for dir in directions:
            room_dict[room_no].update({dir:starting_room.get_room_in_direction(dir).id})
        for direction in starting_room.get_exits():
            new_room = starting_room.get_room_in_direction(direction)
            room_recursive(new_room,room_graph,room_dict,visit_list)
    if len(room_dict) == len(room_graph):
        return room_dict,visit_list
    

def getrooms(room_no,room_dict):
    directions = room_dict[room_no]
    for direction in directions:
        print(direction,directions[direction])



def bfs(starting_vertex, destination_vertex,room_dict):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        paths = []
        visited = set()
        bft_queue = Queue()
        dir_queue = Queue()
        bft_queue.enqueue([starting_vertex])
        dir_queue.enqueue([])
        while bft_queue.size() > 0:
            vertex_path = bft_queue.dequeue()
            dir_path = dir_queue.dequeue()
            vertex = vertex_path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return dir_path
                for direction in room_dict[vertex]:
                    path_copy = vertex_path.copy()
                    dirpath_copy = dir_path.copy()
                    path_copy.append(room_dict[vertex][direction])
                    dirpath_copy.append(direction)
                    bft_queue.enqueue(path_copy)
                    dir_queue.enqueue(dirpath_copy)



#print(type(world.starting_room.id))
room_dict,visited = room_recursive(world.starting_room,room_graph)
#print(visited)
#print(room_dict)
for i in range(len(visited)-1):
    traversal_path.extend(bfs(visited[i],visited[i+1],room_dict))
#print(len(visited_rooms))
# for i in range(len(visited_rooms)-1):
#     print(f'from {visited_rooms[i].id} to {visited_rooms[i+1].id}')
#     roompath,directions_path = bfs(visited_rooms[i],visited_rooms[i+1])
#     print(directions_path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
