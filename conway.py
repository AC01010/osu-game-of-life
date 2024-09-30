playfield = (33, 25)
offsets = (12, 4)

class Conway:
    def __init__(self, length, width) -> None:
        self.state = [[0 for _ in range(length)] for _ in range(width)]
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return "\n".join(["".join(["█" if str(cell) == "1" else "." for cell in row]) for row in self.state])
    
    def osu_field(self):
        return [row[offsets[0]:offsets[0]+playfield[0]] for row in self.state[offsets[1]:offsets[1]+playfield[1]]]
    
    def clear(self):
        self.state = [[0 for _ in range(self.length)] for _ in range(self.width)]
    
    def place(self, x, y):
        print(x,y)
        self.state[y][x] = 1

    def place_with_offset(self, x, y):
        self.state[y+self.width//2][x+self.length//2] = 1

    def next_state(self):
        new_state = [[0 for _ in range(len(self.state[0]))] for _ in range(len(self.state))]
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                new_state[i][j] = self._next_cell_state(i, j)
        self.state = new_state
    
    def _next_cell_state(self, x, y):
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x+i < len(self.state) and 0 <= y+j < len(self.state[0]):
                    live_neighbors += self.state[x+i][y+j]
        if self.state[x][y] == 1:
            if live_neighbors < 2 or live_neighbors > 3:
                return 0
            return 1
        else:
            if live_neighbors == 3:
                return 1
            return 0
        
    def _next_cell_state_with_loop(self, x, y):
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                live_neighbors += self.state[(x+i)%len(self.state)][(y+j)%len(self.state[0])]
        if self.state[x][y] == 1:
            if live_neighbors < 2 or live_neighbors > 3:
                return 0
            return 1
        else:
            if live_neighbors == 3:
                return 1
            return 0
        
def render(matrix):
    coords = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                coords.append((col*16, row*16))
    return coords

def get_timestamp(beat_no):
    # 0-1350
    return round(1706 + 428.571429 * beat_no)

conway = Conway(playfield[0]+offsets[0]*2, playfield[1]+offsets[1]*2)

instructions = {
    0: ([(1,0),(4,0),(7,0),(10,0),(13,0),(16,0),(19,0),(22,0),(25,0),(28,0),(31,0),(34,0),(37,0),(40,0),(43,0),(46,0),(49,0),(52,0),(55,0),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(15,1),(16,1),(17,1),(18,1),(19,1),(20,1),(21,1),(22,1),(23,1),(24,1),(25,1),(26,1),(27,1),(28,1),(29,1),(30,1),(31,1),(32,1),(33,1),(34,1),(35,1),(36,1),(37,1),(38,1),(39,1),(40,1),(41,1),(42,1),(43,1),(44,1),(45,1),(46,1),(47,1),(48,1),(49,1),(50,1),(51,1),(52,1),(53,1),(54,1),(55,1),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),(17,3),(18,3),(19,3),(20,3),(21,3),(22,3),(23,3),(24,3),(25,3),(26,3),(27,3),(28,3),(29,3),(32,3),(33,3),(34,3),(37,3),(38,3),(39,3),(40,3),(41,3),(42,3),(43,3),(44,3),(45,3),(46,3),(47,3),(48,3),(49,3),(50,3),(51,3),(52,3),(53,3),(54,3),(55,3),(0,4),(31,4),(32,4),(36,4),(37,4),(56,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(12,5),(13,5),(14,5),(15,5),(16,5),(17,5),(18,5),(19,5),(20,5),(21,5),(22,5),(23,5),(24,5),(27,5),(28,5),(29,5),(33,5),(34,5),(38,5),(39,5),(40,5),(41,5),(44,5),(45,5),(46,5),(47,5),(48,5),(49,5),(50,5),(51,5),(52,5),(53,5),(54,5),(55,5),(26,6),(27,6),(43,6),(44,6),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),(12,7),(13,7),(14,7),(15,7),(16,7),(17,7),(18,7),(19,7),(20,7),(21,7),(22,7),(23,7),(24,7),(27,7),(28,7),(29,7),(33,7),(34,7),(40,7),(41,7),(45,7),(46,7),(49,7),(50,7),(51,7),(52,7),(53,7),(54,7),(55,7),(0,8),(31,8),(32,8),(36,8),(38,8),(39,8),(48,8),(49,8),(56,8),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),(13,9),(14,9),(15,9),(16,9),(17,9),(18,9),(19,9),(20,9),(21,9),(22,9),(23,9),(24,9),(27,9),(28,9),(29,9),(32,9),(33,9),(34,9),(38,9),(39,9),(45,9),(46,9),(50,9),(51,9),(52,9),(53,9),(54,9),(55,9),(26,10),(27,10),(40,10),(41,10),(43,10),(44,10),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11),(12,11),(13,11),(14,11),(15,11),(16,11),(17,11),(18,11),(19,11),(20,11),(21,11),(22,11),(23,11),(24,11),(28,11),(29,11),(30,11),(31,11),(32,11),(43,11),(44,11),(50,11),(51,11),(52,11),(53,11),(54,11),(55,11),(0,12),(29,12),(45,12),(46,12),(48,12),(49,12),(56,12),(1,13),(2,13),(3,13),(4,13),(5,13),(6,13),(7,13),(8,13),(9,13),(10,13),(11,13),(12,13),(13,13),(14,13),(15,13),(16,13),(17,13),(18,13),(19,13),(20,13),(21,13),(22,13),(23,13),(24,13),(30,13),(40,13),(48,13),(49,13),(52,13),(53,13),(54,13),(55,13),(26,14),(28,14),(35,14),(39,14),(50,14),(51,14),(1,15),(2,15),(3,15),(4,15),(5,15),(6,15),(7,15),(8,15),(9,15),(10,15),(11,15),(12,15),(13,15),(14,15),(15,15),(16,15),(17,15),(18,15),(19,15),(20,15),(21,15),(22,15),(23,15),(24,15),(28,15),(30,15),(32,15),(33,15),(34,15),(35,15),(36,15),(43,15),(51,15),(52,15),(53,15),(54,15),(55,15),(0,16),(31,16),(32,16),(33,16),(37,16),(44,16),(56,16),(1,17),(2,17),(3,17),(4,17),(5,17),(6,17),(7,17),(8,17),(9,17),(10,17),(11,17),(12,17),(13,17),(14,17),(15,17),(16,17),(17,17),(18,17),(19,17),(20,17),(21,17),(22,17),(23,17),(24,17),(28,17),(30,17),(32,17),(33,17),(34,17),(35,17),(36,17),(43,17),(51,17),(52,17),(53,17),(54,17),(55,17),(26,18),(28,18),(35,18),(39,18),(50,18),(51,18),(1,19),(2,19),(3,19),(4,19),(5,19),(6,19),(7,19),(8,19),(9,19),(10,19),(11,19),(12,19),(13,19),(14,19),(15,19),(16,19),(17,19),(18,19),(19,19),(20,19),(21,19),(22,19),(23,19),(24,19),(30,19),(40,19),(48,19),(49,19),(52,19),(53,19),(54,19),(55,19),(0,20),(29,20),(45,20),(46,20),(48,20),(49,20),(56,20),(1,21),(2,21),(3,21),(4,21),(5,21),(6,21),(7,21),(8,21),(9,21),(10,21),(11,21),(12,21),(13,21),(14,21),(15,21),(16,21),(17,21),(18,21),(19,21),(20,21),(21,21),(22,21),(23,21),(24,21),(28,21),(29,21),(30,21),(31,21),(32,21),(43,21),(44,21),(50,21),(51,21),(52,21),(53,21),(54,21),(55,21),(26,22),(27,22),(40,22),(41,22),(43,22),(44,22),(1,23),(2,23),(3,23),(4,23),(5,23),(6,23),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23),(13,23),(14,23),(15,23),(16,23),(17,23),(18,23),(19,23),(20,23),(21,23),(22,23),(23,23),(24,23),(27,23),(28,23),(29,23),(32,23),(33,23),(34,23),(38,23),(39,23),(45,23),(46,23),(50,23),(51,23),(52,23),(53,23),(54,23),(55,23),(0,24),(31,24),(32,24),(36,24),(38,24),(39,24),(48,24),(49,24),(56,24),(1,25),(2,25),(3,25),(4,25),(5,25),(6,25),(7,25),(8,25),(9,25),(10,25),(11,25),(12,25),(13,25),(14,25),(15,25),(16,25),(17,25),(18,25),(19,25),(20,25),(21,25),(22,25),(23,25),(24,25),(27,25),(28,25),(29,25),(33,25),(34,25),(40,25),(41,25),(45,25),(46,25),(49,25),(50,25),(51,25),(52,25),(53,25),(54,25),(55,25),(26,26),(27,26),(43,26),(44,26),(1,27),(2,27),(3,27),(4,27),(5,27),(6,27),(7,27),(8,27),(9,27),(10,27),(11,27),(12,27),(13,27),(14,27),(15,27),(16,27),(17,27),(18,27),(19,27),(20,27),(21,27),(22,27),(23,27),(24,27),(27,27),(28,27),(29,27),(33,27),(34,27),(38,27),(39,27),(40,27),(41,27),(44,27),(45,27),(46,27),(47,27),(48,27),(49,27),(50,27),(51,27),(52,27),(53,27),(54,27),(55,27),(0,28),(31,28),(32,28),(36,28),(37,28),(56,28),(1,29),(2,29),(3,29),(4,29),(5,29),(6,29),(7,29),(8,29),(9,29),(10,29),(11,29),(12,29),(13,29),(14,29),(15,29),(16,29),(17,29),(18,29),(19,29),(20,29),(21,29),(22,29),(23,29),(24,29),(25,29),(26,29),(27,29),(28,29),(29,29),(32,29),(33,29),(34,29),(37,29),(38,29),(39,29),(40,29),(41,29),(42,29),(43,29),(44,29),(45,29),(46,29),(47,29),(48,29),(49,29),(50,29),(51,29),(52,29),(53,29),(54,29),(55,29),(1,31),(2,31),(3,31),(4,31),(5,31),(6,31),(7,31),(8,31),(9,31),(10,31),(11,31),(12,31),(13,31),(14,31),(15,31),(16,31),(17,31),(18,31),(19,31),(20,31),(21,31),(22,31),(23,31),(24,31),(25,31),(26,31),(27,31),(28,31),(29,31),(30,31),(31,31),(32,31),(33,31),(34,31),(35,31),(36,31),(37,31),(38,31),(39,31),(40,31),(41,31),(42,31),(43,31),(44,31),(45,31),(46,31),(47,31),(48,31),(49,31),(50,31),(51,31),(52,31),(53,31),(54,31),(55,31),(1,32),(4,32),(7,32),(10,32),(13,32),(16,32),(19,32),(22,32),(25,32),(28,32),(31,32),(34,32),(37,32),(40,32),(43,32),(46,32),(49,32),(52,32),(55,32)], False)
    # 10: ([], True),
    # 20: ([(0, 0), (1, 0), (2, 0)], False)
}

with open("hitobjects.txt", "w") as f:
    for i in range(500):
        print("Generation:", i)
        if i in instructions:
            if instructions[i][1]:
                conway.clear()
            for x, y in instructions[i][0]:
                conway.place(x, y)
        # print(conway)
        x = conway.osu_field()
        for circle in render(x):
            f.write(f"{circle[0]}, {circle[1]}, {get_timestamp(i)}, 5,0,0:0:0:0:\n")
        conway.next_state()
    f.close()