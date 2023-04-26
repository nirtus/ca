import csv
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Data parameteres
everynth = 3 # show every other point (f.e. 3 - show every 3rd point)
start = 0 # start point
end = -1 # end point

# Prerecorded tracking results for ploting
track_file = 'test_video3_200Adam64-4.csv'

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
def tracks(everyth, start, end):
    plot_tracks = []
    with open('_data/_tracks/' + track_file, mode='r') as file:
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
# Note: plot images are saved into "_data/images" folder. Image name is same as track_file
def scatter_3d(df, track_file):
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

def scatter(df, x, y, track_file):
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

# List of plots
def draw_plots():
    # Data Frame
    df = pd.DataFrame(
        tracks(everynth, start, end),
        columns = ["id", "type", "x", "y", "time"]
    )

    scatter_3d(df, track_file)
    scatter(df, 'x', 'y', track_file)

    plt.show()

# Draw plots
draw_plots()