from util import Queue, Stack
from room import Room
from player import Player
from world import World


class Traverser:

    def __init__(self, world: World, player: Player):
        self.world = world
        self.player = player
        self.visited = set()
        self.starting_room = player.currentRoom
        self.path = []

    def generate_path(self):
        reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        start = True
        self.visited.add(self.starting_room)
        while len(self.visited) < len(self.world.rooms):
            if start:
                next_dir = None
                current_room = self.starting_room
                start = False
                open_doors = current_room.getExits()
            else:
                current_room = current_room.getRoomInDirection(next_dir)


            if current_room not in self.visited:
                open_doors = current_room.getExits()
                self.visited.add(current_room)
                self.path.append(next_dir)
                if len(self.visited) == len(self.world.rooms):
                    return self.path
                elif len(current_room.getExits()) > 1:
                    next_dir = open_doors.pop()
                elif len(current_room.getExits()) == 1:
                    self.path.extend(self.path_to_closest_unvisited(current_room))
                else:
                    print("!!!Error!!!")

            else:
                if (len(current_room.getExits()) > 1) & (len(open_doors) > 0):
                    next_dir = open_doors.pop()
                elif len(open_doors) == 0:
                    self.path.extend(self.path_to_closest_unvisited(current_room))


    def path_to_closest_unvisited(self, starting_room, target=None):
        print(f"ptcu called, curpath: {self.path}")
        queue = Queue()
        paths = []
        visited_local = set()
        queue.enqueue(starting_room)

        start = True
        while queue.size() > 0:
            if not start:
                current_path = queue.dequeue()
                current_room = starting_room
                for d in current_path:
                    current_room = current_room.getRoomInDirection(direction=d)
            else:
                current_path = []
                current_room = queue.dequeue()
                start = False
            print(current_path)
            open_doors = current_room.getExits()
            if current_room not in visited_local:
                if (current_room not in self.visited) or (len(self.world.rooms) == len(self.visited.union(visited_local))):
                    visited_local.add(current_room)
                    paths.append(current_path)
                    return current_path
                else:
                    # if (len(open_doors) < 2 and
                    #         current_room.getRoomInDirection(open_doors[0]) is not prev_room):
                    #     visited_local.add(current_room)
                    # else:
                    visited_local.add(current_room)
                    for next_room in open_doors:
                        cpath_copy = current_path.copy()
                        cpath_copy.append(next_room)
                        queue.enqueue(cpath_copy)
        print(f"final paths: {paths}")
        return min(paths)