import csv
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from shapely.geometry import Point, Polygon

# Data parameteres
everynth = 1 # show every other point (f.e. 3 - show every 3rd point)
start = 0 # start point
end = -1 # end point
objectId = 2 # all objects. For specific object, change 0 to objectid 
track_file_index = 5

# Prerecorded tracking results for ploting
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
                # Sometimes several objects are detected during same time tick. For plotting, we need flatten dimmensions
                for line in row:
                    fline = track_format(line)
                    
                    if objectId == 0: # All objects
                        plot_tracks.append(fline)
                    else:
                        if fline[0] == objectId: # Single object by id
                            plot_tracks.append(fline)

    #for line in plot_tracks:
        #print(line) 

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
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Draw sector for object speed calculations
    quadrilateral = [(579, 449), (510, 407), (635, 372), (713, 414)]
    draw.polygon(quadrilateral, fill="grey", outline="red")

    # Create a Polygon object from the quadrilateral coordinates
    polygon = Polygon(quadrilateral)

    # Check if each point in the DataFrame is inside the sector
    sp = []
    for index, row in df.iterrows():
        point = Point(row["x"], row["y"])
        if polygon.contains(point):
            sp.append([int(row['x']), int(row['y']), row['time']])

    # Calculate speed
    distance = 4 # Distance is taken based on maps.lt
    time = round(sp[-1][2] - sp[0][2], 2)
    speed = round(distance/time * 3.6, 2)
    print(speed, "km/h")

    # Set the font and size
    font = ImageFont.truetype("arial.ttf", 20)
    # Set the text to be drawn
    text = f"{str(speed)} km/h"
    # Draw the text on the image
    draw.text((560, 400), text, font=font)

    # # Draw start and end sectors
    # start_point_1 = (579, 449)
    # start_point_2 = (713, 414)

    # end_point_1 = (510, 407)
    # end_point_2 = (635, 372)

    # draw.line((start_point_1, start_point_2), fill=(255, 255, 0), width=4)
    # draw.line((end_point_1, end_point_2), fill=(255, 255, 0), width=4)
    # # EOF Draw start and end sectors


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
def draw_plots(track_file):
    # Data Frame
    df = pd.DataFrame(
        tracks(track_file, everynth, start, end),
        columns = ["id", "type", "x", "y", "time"]
    )

    #scatter_3d(df, track_file)
    scatter(df, 'x', 'y', track_file)

    plt.show()

# Draw plots
draw_plots(track_files[track_file_index])