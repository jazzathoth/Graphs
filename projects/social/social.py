import numpy as np


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        for _ in range(numUsers):
            self.addUser(name=self.lastID)

        rem_friends = [int(round(x)) if x > 0 else int(0) for x in np.random.normal(loc=avgFriendships, scale=1, size=numUsers)]

        for i in range(numUsers):
            l_friends = []
            for _ in range(rem_friends[i]):
                proba = rem_friends.copy()
                proba[i] = 0
                total_f = sum(proba)
                proba = [float(x) / total_f for x in proba]
                dupl = True

                while dupl:
                    new_f = int(np.random.choice(list(range(numUsers)),
                                             size=1,
                                             p=proba))
                    if new_f not in l_friends:
                        dupl = False
                rem_friends[new_f] += -1
                l_friends.append(new_f)
            print(rem_friends[i], end=" ")
            print(l_friends)
        return
        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
