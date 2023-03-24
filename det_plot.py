import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Format and return line with coordinates
def coord_format(frame, row):
    if row != None:
        row_ex = row.strip('[').strip(']').strip(' ')
        row_ex = row_ex.split(',')
        row_x = int(row_ex[1])
        row_y = int(row_ex[2])
        return (640-row_x, 480-row_y, frame)
    else:
        return(0, 0, frame)

# Read CSV and return plot dots
def build_dots(file, everyth, start, end):
    plot_tracks = []
    with open('_data/_tracks/' + file, mode='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        cut_list = list(reader)[start:end] # cut list form start to end list item
        #print(cut_list)
        
        # Iterate over each row in the list
        frame = 0
        for index, row in enumerate(cut_list):
            frame += 1
            if len(row) == 0 or index % everyth != 0:  # skip empty rows and select every other member
                plot_tracks.append(coord_format(frame, None))
            else:
                for line in row:
                    plot_tracks.append(coord_format(frame, line))
            
    return plot_tracks

# Show plot
def plot_show(dots):
    # Create a figure and a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the scatter plot
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    zs = [dot[2] for dot in dots]
    ax.scatter(xs, ys, zs)

    # Set the axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('frame')

    # Show the plot
    plt.show()


# Plot parameteres
everyth = 2
start = 1000
end = 2000

# Plots
dots = build_dots('predict_and_track_100Adam48.csv', everyth, start, end)
plot_show(dots)

dots = build_dots('predict_and_track_200Adam64.csv', everyth, start, end)
plot_show(dots)

dots = build_dots('predict_and_track_200SGD32.csv', everyth, start, end)
plot_show(dots)

