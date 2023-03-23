import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Plot tracking results
# Open the CSV file

def coord_format(frame, row):
    row_ex = row.strip('[').strip(']').strip(' ')
    row_ex = row_ex.split(',')

    row_x = int(row_ex[1])
    row_y = int(row_ex[2])
    return (640-row_x, 480-row_y, frame)

def build_dots(reader, everyth, start, end):
    cut_list = list(reader)[start:end] # cut list form start to end list item
    #print(cut_list)
    
    # Iterate over each row in the list
    frame = 0
    for index, row in enumerate(cut_list):
        if len(row) == 0 or index % everyth != 0:  # skip empty rows and select every other member
            continue
        else:
            frame += 1
            for line in row:
                plot_tracks.append(coord_format(frame, line))
            
    #return plot_tracks


plot_tracks = []
with open('_data/_tracks/tracks.csv', mode='r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    build_dots(reader, 2, 2900, 3200)

# PLOT

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
xs = [dot[0] for dot in plot_tracks]
ys = [dot[1] for dot in plot_tracks]
zs = [dot[2] for dot in plot_tracks]
ax.scatter(xs, ys, zs)

# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('frame')

# Show the plot
plt.show()









# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Example dot coordinates
# dots = [(1, 2, 3), (2, 4, 5), (3, 1, 2), (4, 5, 4), (5, 3, 1)]

# # Create a figure and a 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Create the scatter plot
# xs = [dot[0] for dot in dots]
# ys = [dot[1] for dot in dots]
# zs = [dot[2] for dot in dots]
# ax.scatter(xs, ys, zs)

# # Set the axis labels
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# # Show the plot
# plt.show()
