import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Data parameteres
everynth = 3
start = 0
end = -1
track_files = [
    'street_view2_100Adam48-4',
    'street_view2_200Adam64-4',
    'street_view2_200SGD32-2',
    'street_view2_200SGD64-4',
    'test_video3_100Adam48-4',
    'test_video3_200Adam64-4',
    'test_video3_200SGD32-2',
    'test_video3_200SGD64-4']

# Format and return line with coordinates
def track_format(row):
    if row != None:
        row_ex = row.strip('[').strip(']').strip(' ')
        row_ex = row_ex.split(',')
        id = int(row_ex[0])
        type = int(row_ex[1])
        x = int(row_ex[2])
        y = int(row_ex[3])
        time = float(row_ex[4])
        return (id, type, x, y, time)

# Read CSV and return plot dots
def tracks(file, everyth, start, end):
    plot_tracks = []
    with open('_data/_tracks/' + file + '.csv', mode='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        cut_list = list(reader)[start:end] # cut list form start to end list item
        
        # Iterate over each row in the list
        for index, row in enumerate(cut_list):
            if len(row) == 0 or index % everyth != 0:  # skip empty rows and select every other member
                continue
            else:
                for line in row:
                    plot_tracks.append(track_format(line))
                    print(track_format(line))
            
    return plot_tracks

# Define a color mapping function
def color_map(value):
    if value < 128:
        return (255, 0, 0)    # red for low values
    else:
        return (0, 255, 0)    # green for high values

# Plot types
def plot_3d(dots):
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

def plot_2d(dots):
    # Split the x and y coordinates into separate lists
    x = [dot[0] for dot in dots]
    y = [dot[2] for dot in dots]

    # Create scatter plot with dots
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('frame')
    plt.title('Scatter plot with dots')

    # Show plot
    plt.show()

def sns_3d(dots):
    xs = [dot[0] for dot in dots]
    ys = [dot[1] for dot in dots]
    zs = [dot[2] for dot in dots]

    seaborn_plot = plt.axes (projection='3d')
    seaborn_plot.scatter3D (xs, ys, zs)
    seaborn_plot.set_xlabel ('x')
    seaborn_plot.set_ylabel ('y')
    seaborn_plot.set_zlabel ('z')
    plt.show ()

def sns_lmr(dots):
    data = {
    'x': [dot[0] for dot in dots],
    'time': [dot[2] for dot in dots],
    'id': [dot[3] for dot in dots]
    }
    df = pd.DataFrame(data)
    sns.set_theme()
    # Plot the multiple linear regression
    sns.lmplot(x='x', y='time', hue='id', data=df)
    plt.show()

def sns_scatter_3d(df, track_file):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x=[df['x']]
    y=[df['y']]
    z=[df['time']]
    obj_id = df['id']

    ax.set_title(track_file)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel ('time')
    ax.scatter(x, y, z, c=obj_id)

def sns_scatter(df, x, y, track_file):
    img = Image.open('_data/_images/scene.png')
    # Calculate the new size based on the percentage
    percent = 100
    width, height = img.size
    new_width = int(width * percent / 100)
    new_height = int(height * percent / 100)

    # Resize the image
    img = img.resize((new_width, new_height))

    # variables in the dataset
    f, ax = plt.subplots(figsize=(12.8, 7.8))
    ax.set_title(track_file)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.imshow(img)

    ax.scatter(df[x], df[y], c=df['id'], s=6)

    # Save the plot to a file
    plt.savefig(f'_data/_images/{track_file}.png')

def draw_plots(track_file):
    # Data Frame
    df = pd.DataFrame(
        tracks(track_file, everynth, start, end),
        columns = ["id", "type", "x", "y", "time"]
    )

    sns_scatter_3d(df, track_file)
    sns_scatter(df, 'x', 'y', track_file)
    plt.show()

# Draw plots
draw_plots(track_files[1])


