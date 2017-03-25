def path(x, y, blocked, hops):
    grid = [
            [[0,'unvisited'] for _ in range(x)]
            for _ in range(y)
            ]
    for i in blocked:
        print(i)
        grid[i[0]][i[1]] = [0, 'blocked']

    grid[x-1][y-1][1] = 'visited'
    for i in range(x - 1):
        if grid[y - 1][i][1] != 'visited' and grid[y - 1][i][1] != 'blocked':
            grid[y - 1][i] = [1,'visited'] 
    for i in range(y - 1):
        if grid[i][x - 1][1] != 'visited' and grid[i][x - 1][1] != 'blocked':
            grid[i][x - 1] = [1,'visited'] 

    for i in range(x - 1, -1, -1):
        for j in range(y - 1, -1, -1):
            if grid[i][j][1] != 'visited' and grid[i][j][1] != 'blocked':
                grid[i][j][0] = grid[i+1][j][0] + grid[i][j+1][0]
                grid[i][j][1] = 'visited'

    if len(hops) > 0:
        for i in hops:
            print(i)
            grid[i[0][0]][i[0][1]][0] = grid[i[1][0]][i[1][1]][0]
            grid[i[0][0]][i[0][1]][1] = 'hop'
        for line in grid:
            print(line)
        for i in range(x - 1):
            for j in range(y - 1):
                if grid[i][j][1] != 'hop' and grid[i][j][1] != 'blocked':
                    grid[i][j] = [0, 'unvisited']
        for line in grid:
            print(line)

        grid[x-1][y-1][1] = 'visited'
        for i in range(x - 1):
            if grid[y - 1][i][1] != 'blocked' and grid[y - 1][i][1] != 'hop':
                grid[y - 1][i] = [1,'visited'] 
        for i in range(y - 1):
            if grid[i][x - 1][1] != 'blocked' and grid[i][x - 1][1] != 'hop':
                grid[i][x - 1] = [1,'visited'] 

        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                if grid[i][j][1] != 'blocked' and grid[i][j][1] != 'hop' and grid[i][j][1] != 'visited':
                    grid[i][j][0] = grid[i+1][j][0] + grid[i][j+1][0]
                    grid[i][j][1] = 'visited'


    for line in grid:
        print(line)
    num_paths = grid[0][0][0] 
    return num_paths

def get_blocked():
    n = input("How many blocked nodes are in this project?: ")
    blocked = []
    for i in range(int(n)):
       print("Enter the coordinates of a blocked node: ")
       x = int(input("X: "))
       y = int(input("Y: "))
       blocked.append((x,y))
    return blocked

def get_hops():
    n = input("How many jumps are in this project?: ")
    hops = []
    for i in range(int(n)):
        print("Enter the x and y values of the starting point of a jump followed by the x and y values of the end point: ")
        x1 = int(input("starting X: "))
        y1 = int(input("starting Y: "))
        x2 = int(input("ending X: "))
        y2 = int(input("ending Y: "))
        hops.append(((x1,y1),(x2,y2)))
    return hops


def main():
    print("This program will calculate the total number of paths to complete a project")
    x = int(input('Enter the x value of the grid: '))
    y = int(input('Enter the y value of the grid: '))
    blocked = get_blocked()
    if x == 1 or y == 1:
        if len(blocked) > 0:
            print("You cannot complete this project")
        else:
            print("There is only one path to complete this project")
    hops = get_hops()
    num_paths = path(x,y,blocked,hops)
    print('There are {} paths to complete the project.'.format(str(num_paths)))
    

if __name__ == '__main__':
    main()

