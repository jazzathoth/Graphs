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

        start = True

        while len(self.visited) < len(self.world.rooms):
            if not start:
                last_room = current_room
                current_room = self.world.rooms[0]
                #print(self.path)
                for d in self.path:
                    current_room = current_room.getRoomInDirection(direction=d)
            else:
                last_room = None
                current_room = self.starting_room
                start = False
            open_doors = current_room.getExits()
            if current_room not in self.visited:
                if len(self.visited) == len(self.world.rooms):
                    return self.path
                self.visited.add(current_room)
                if len(self.world.rooms) - len(self.visited) == 1:
                    # self.path.append(self.path_to_closest_unvisited(starting_room=current_room,
                    #                                                 target=set(self.world.rooms.values())
                    #                                                 .difference(self.visited)))
                    missing = set(self.world.rooms.keys()).difference(set(r.id for r in self.visited))
                    print(missing)
                    print(current_room.id)
                    print("error")
                    last_path = self.path_to_room(start_room=current_room,
                                                  end_room=self.world.rooms[missing.pop()])
                    print(f"last path: {last_path}")
                    self.path.extend(last_path)
                    print(self.path)
                    return self.path
                if (len(open_doors) < 2 and
                        current_room.getRoomInDirection(direction=open_doors[0]) == last_room):
                    self.path.extend(self.path_to_closest_unvisited(starting_room=current_room))
                else:
                    can_traverse = False
                    idx = len(open_doors)
                    while (idx >= 0) and (can_traverse == False):
                        idx += -1
                        can_traverse = current_room.getRoomInDirection(open_doors[idx]) not in self.visited
                    if can_traverse:
                        self.path.append(open_doors[idx])
                    else:
                        self.path.extend(self.path_to_closest_unvisited(starting_room=current_room))

            #print(len(self.world.rooms) - len(self.visited))
        return self.path

    def path_to_closest_unvisited(self, starting_room, target=None):
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

            open_doors = current_room.getExits()
            if current_room not in visited_local:
                if (current_room not in self.visited) or (len(self.world.rooms) == len(self.visited.union(visited_local))):
                    visited_local.add(current_room)
                    paths.append(current_path)
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
        #print(set(self.world.rooms.keys()).difference(self.visited))
        #print(f"called ptcu. paths: {paths}")

        return min(paths)

    def path_to_room(self, start_room: Room, end_room: Room):
        print('starting: path_to_room')
        print(start_room.id)
        print(end_room.id)
        queue = Queue()
        queue.enqueue(start_room)
        visited_local = set()
        start = True
        while queue.size() > 0:
            if start:
                current_path = []
                current_room = start_room
                queue.dequeue()
                start=False
            else:
                current_path = queue.dequeue()
                current_room = start_room
                for d in current_path:
                    current_room = current_room.getRoomInDirection(direction=d)
                print(current_room)
            if current_room not in visited_local:

                if current_room == end_room:
                    return current_path

                visited_local.add(current_room)
                open_doors = current_room.getExits()

                for door in open_doors:
                    path_copy = current_path.copy()
                    path_copy.append(door)
                    queue.enqueue(path_copy)
        return None
