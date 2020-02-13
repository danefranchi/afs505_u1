"""Conway's Game of Life, creater: Dane Franchi, reviewer: Gunnar Newell (reviewed for 100pts)

   ..module:: Game_of_life
      :platform Windows
      :synopsis: Runs Conway's Game of life on 30 X 80 grid.

   .. moduleauthor:: Dane Franchi dane.franchi@wsu.edu
   """


def main():

   """ Play the Conway's Game of Life """

   """arguments are read from code given"""

   from sys import argv
   script = argv[0]
   desired_ticks = argv[1]
   grid_start = argv[2:]

   desired_ticks = int(desired_ticks)



   """create three girds:
   binary_grid to hold binary code: "1" for on, "0" for off
   temp_grid to hold new values while calcultions are run, also in binary
   X_grid for holding and printing game results
   binary_grid and temp_grid are encompassed by extra layer of 0's to make for easier calculations.
   """

   binary_grid =[]
   temp_grid = []
   X_grid = [""]


   for i in range(0,32):
      binary_grid.append([0]*82)
      temp_grid.append([0]*82)
   for i in range(1,31):
      X_grid.append(['-']*81)




   """translate starting values from code given by user"""

   for on in grid_start:
      on = on.split(":")
      row = int(on[0])
      column = int(on[1])
      X_grid[row][column] = "X"
      binary_grid[row][column] = 1


   """tick_count set to zero to keep track of number of times while loop runs. """

   tick_count = 0

   while tick_count <= desired_ticks:

      """print X_grid on each run through, first run is count zero"""

      for i in range(1,31):
         for j in range(1,81):
            print(X_grid[i][j], end = '')

         print()

      """calculate the number of neighbors from binary_grid and store result in temp_grid
      to make the formula easier all nine cells where add.
      If count is "3", then the center cell is either on with 2 neighbors or off with 3 neighbors.
      if (count - the center value) is "3", then it is either on with 3 neighbors or off with 3 neighbors.
      This acconds for all cells which are to be on
      temp_grid is cleared to '0' then set to '1' as needed
      """


      for i in range(1,31):
         for j in range(1,81):
            neighbor_count = neighbors(i,j,binary_grid)            
            temp_grid[i][j] = 0
            if neighbor_count == 3 or (neighbor_count - binary_grid[i][j]) == 3:
               temp_grid[i][j] = 1

      """temp_grid is used to update binary_grid and X_grid; converting '1' to 'X' and '0' to '-' """

      for i in range(1,31):
         for j in range(1,81):
            binary_grid[i][j] = temp_grid[i][j]
            if temp_grid[i][j] == 1:
               X_grid[i][j] = "X"
            else:
               X_grid[i][j] = "-"

      """The following line was add to create a space between grids"""

      print("Grid above is after", tick_count, "ticks.")

      """tick_count is increased by one to keep count of number of times game is calculated"""

      tick_count += 1

def neighbors(i,j,binary_grid):
   """counts all neighhbors and self"""

   neighbor_count = 0
   for n in range(i-1,i+2):
      for m in range(j-1,j+2):
         neighbor_count += binary_grid[n][m]
   return(neighbor_count)




print(main.__doc__)

if __name__ == "__main__":
   main()
