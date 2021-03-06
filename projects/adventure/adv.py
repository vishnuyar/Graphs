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
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()




# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def room_recursive(starting_room,room_graph,room_dict=None,visit_list=None,previous_direction=None):
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
        directions = starting_room.get_exits()
        random.shuffle(directions)
        for direction in directions:
            new_room = starting_room.get_room_in_direction(direction)
            room_recursive(new_room,room_graph,room_dict,visit_list,direction)
    if len(room_dict) == len(room_graph):
        return room_dict,visit_list
    



def bfs(starting_vertex, destination_vertex,room_dict):
        """
        Return a directions containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
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
room_order = []
min_steps = 2000
for step in range(200000):
    traversal_path = []
    #world.starting_room = world.rooms[i]
    player = Player(world.starting_room)
    #Traverse all the rooms in the world using recursive dft 
    room_dict,visited = room_recursive(world.starting_room,room_graph)
    #print(visited)
    #print(room_dict)
    for i in range(len(visited)-1):
        #Get the shortest between the two rooms
        path = bfs(visited[i],visited[i+1],room_dict)
        #print(f'{visited[i]} to {visited[i+1]} in {len(path)} ')
        traversal_path.extend(path)



    # TRAVERSAL TEST
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        print(f"Times:{step} , TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    if min_steps > len(traversal_path):
        min_steps = len(traversal_path)
        room_order = visited
        optimum_path = traversal_path.copy()
print('---------------')
print(f'The minimum number of steps is {min_steps}') 
print('---------------')
#print(f'The order of rooms visited is {visited}')
print('---------------')
print(f'Traversal {optimum_path}')
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
