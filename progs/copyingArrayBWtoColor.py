'''
Created on Apr 11, 2018
@author: ishank
'''

def merge_arrays(bw, colors, pos):
    
    if len(bw) + pos[0] > len(colors) or len(bw[0]) + pos[1] > len(colors[0]):
        return False
    
    for row in range(len(bw)):
        for col in range(len(bw[row])):
            if bw[row][col] == 0:
                colors[row + pos[0]][col + pos[1]] = "0xFF0000"
            else:
                colors[row + pos[0]][col + pos[1]] = "0xFFFFFFFF"
            
bw = [[0,1,0],
      [1,0,1],
      [0,1,0]]
colors = [["0xAABBCC", "0xCCABAAA1", "0xAABBCC", "0xAABBCC", "0xCCABCCC1", "0xAABBCC"],
          ["0xAABBCC", "0xCCABCCC1", "0xAABBCC", "0xAABBCC", "0xBBABCCC1", "0xAABBCC"],
          ["0xAABBCC", "0xBBABCCC1", "0xAABBCC", "0xAABBCC", "0xCCABAAA1", "0xAABBCC"],
          ["0xAABBCC", "0xCCABCCC1", "0xAABBCC", "0xAABBCC", "0xBBABCCC1", "0xAABBCC"],
          ["0xAABBCC", "0xCCABCCC1", "0xAABBCC", "0xAABBCC", "0xBBABCCC1", "0xAABBCC"],
          ["0xAABBCC", "0xCCABAAA1", "0xAABBCC", "0xAABBCC", "0xCCABCCC1", "0xAABBCC"]]

print(merge_arrays(bw, colors, (3, 3)))
for row in colors:
    print(row)

