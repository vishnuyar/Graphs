import random
import itertools
from util import Stack,Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        

        # Add users
        for i in range(num_users):
            self.add_user(f'user_{i+1}')

        # Create friendships
        friendsships = list(itertools.combinations(range(1,num_users+1),avg_friendships))
        random.shuffle(friendsships)
        total_friendships = (num_users*avg_friendships)//2
        for frienship in friendsships[:total_friendships]:
            self.add_friendship(frienship[0],frienship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        user_graphs = {}  # Note that this is a dictionary, not a set
        
        sc_bft = Queue()
        visited = set()
        sc_bft.enqueue([user_id])
        while sc_bft.size() > 0:
            current_user_path = sc_bft.dequeue()
            current_user = current_user_path[-1]
            #print(f'{current_user}:{current_user_path}')
            if current_user not in user_graphs.keys():
                user_graphs.update({current_user:current_user_path})
            if current_user not in visited:
                visited.add(current_user)
                for friend in self.friendships[current_user]:
                    if friend not in visited:
                        friendship_path = current_user_path.copy()
                        friendship_path.append(friend)
                        sc_bft.enqueue(friendship_path)

        
        return user_graphs


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    for i in sorted(connections.keys()):
        print(f'{i}:{connections[i]}')
