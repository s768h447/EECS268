#   Samuel Harrison 3/30/2022

class Mover:

    def __init__(self, Presets, Maze):

        self.blobPos = Presets[2], Presets[3]

        self.mapSize = Presets[0], Presets[1]

        self.peopleConsumed = 0

        self.Maze = Maze

        self.lastPos = []

    def mark(self, entry):

        self.lastPos.append(list(entry))

    def move(self):

        if len(self.lastPos) == 0:

            self.Maze[self.blobPos[0]][self.blobPos[1]] = 'B'

            if self.peopleConsumed != 0:

                return

        if self.Maze[self.blobPos[0]][self.blobPos[1]] == 'P':

            self.peopleConsumed += 1

        if self.Maze[self.blobPos[0]][self.blobPos[1]] == '@':

            count = 0

            for row in self.Maze:

                count += 1

                for index in row:

                    if index == '@' and count > self.blobPos[0]:

                        self.blobPos = count - 1, self.blobPos[1]

            #   FIND NEXT SEWER

        else:

            self.Maze[self.blobPos[0]][self.blobPos[1]] = 'B'

        #   going up
        if self.Maze[self.blobPos[0] - 1][self.blobPos[1]] not in ['#', 'B'] and self.blobPos[0] - 1 >= 0:

            self.blobPos = self.blobPos[0] - 1, self.blobPos[1]

            self.mark(self.blobPos)

        #   going right
        elif self.Maze[self.blobPos[0]][self.blobPos[1] + 1] not in ['#', 'B'] and self.blobPos[1] + 1 >= 0:

            self.blobPos = self.blobPos[0], self.blobPos[1] + 1

            self.mark(self.blobPos)

        #   going down
        elif self.Maze[self.blobPos[0] + 1][self.blobPos[1]] not in ['#', 'B'] and self.blobPos[0] + 1 >= 0:

            self.blobPos = self.blobPos[0] + 1, self.blobPos[1]

            self.mark(self.blobPos)

        #   going left
        elif self.Maze[self.blobPos[0]][self.blobPos[1] - 1] not in ['#', 'B'] and self.blobPos[1] + 1 >= 0:

            self.blobPos = self.blobPos[0], self.blobPos[1] - 1

            self.mark(self.blobPos)

        else:

            self.blobPos = self.lastPos[-1:][:1][0]

            self.lastPos = self.lastPos[:-1]

        self.move()

def main():

    fileinput = input('Input a File: ')


    with open(fileinput, 'r') as file:

        #   takes the file and uses list comprehension to iterate through, removing escapes
        data = [line.strip('\n') for line in file.readlines()]

    #   gets presets and puts in a list of ints
    presets = [int(num) for num in ','.join(','.join(data[:2]).split(' ')).split(',')]

    #   gets map in a list of lists
    maze_map = [list(row) for row in ' '.join(data[2:]).split(' ')]

    #print(maze_map[1][0])

    #   counts sewers in a list
    sewers = []

    [[sewers.append(index) for index in row if index == '@'] for row in maze_map]

    #   checks if the number of sewers is even
    if len(sewers) % 2 != 0:

        print('Invalid Sewer Count')

    else:

        maze = Mover(presets, maze_map)

        maze.move()

        for row in maze.Maze:

            print(''.join(row))

        print(f'Total Eaten: {maze.peopleConsumed}')





main()