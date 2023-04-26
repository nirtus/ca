import csv
import pandas as pd
import ast
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from shapely.geometry import Point, Polygon

# Data parameteres
objectId = 2 # 0 - all objects. For specific object, change 0 to objectid
everynth = 1 # show every other point (f.e. 3 - show every 3rd point)

# Prerecorded tracking results for ploting
#track_file = 'test_video_200Adam64-4.csv'
#track_file = 'test_video2_200Adam64-4.csv'
track_file = 'test_video3_200Adam64-4.csv'

# Read CSV and return pandas df
def tracks(everynth = 1):
    # Create an empty DataFrame with the desired column names
    column_names = ["id", "type", "x", "y", "timestamp"]
    df = pd.DataFrame(columns=column_names)

    # Read tracks into DF
    with open('_data/_tracks/' + track_file, mode='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        cut_list = list(reader)
        
        # Iterate over each row in the list
        for index, row in enumerate(cut_list):
            if len(row) == 0 or index % everynth != 0:  # skip empty rows and select every other member
                continue
            else:
                # Sometimes several objects are detected during same time tick. For plotting, we need flatten dimmensions
                for line in row:
                    # Convert string to list and add to pandas df
                    lst = ast.literal_eval(line)
                    new_line = [str(x) for x in lst]
                    
                    df.loc[len(df)] = new_line

    df['id'] = df['id'].astype(int)
    df['type'] = df['type'].astype(int)
    df['x'] = df['x'].astype(int)
    df['y'] = df['y'].astype(int)
    df['timestamp'] = df['timestamp'].astype(float)
    return df

# Define a color mapping function
def color_map(value):
    if value < 128:
        return (255, 0, 0)    # red for low values
    else:
        return (0, 255, 0)    # green for high values

# Plot types
# Note: plot images are saved into "_data/images" folder. Image name is same as track_file
def scatter_3d(df):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x=[df['x']]
    y=[df['y']]
    z=[df['timestamp']]
    obj_id = df['id']

    ax.set_title(track_file)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel ('timestamp')
    ax.scatter(x, y, z, c=obj_id)

    plt.savefig(f'_data/_images/scatter_3d_{track_file}.png')

def scatter(df):
    img = Image.open('_data/_images/scene.png')
    draw = ImageDraw.Draw(img)

    # Set the font and size
    font = ImageFont.truetype("arial.ttf", 20)
    # Set the text to be drawn
    text = f"Objects count: {df['id'].nunique()}"
    # Draw the text on the image
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)

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
    ax.imshow(img)
    ax.scatter(df['x'], df['y'], c=df['id'], s=6)
    # Save the plot to a file
    plt.savefig(f'_data/_images/scatter_{track_file}.png')

def scatter_speed(df):
    img = Image.open('_data/_images/scene.png')
    draw = ImageDraw.Draw(img)

    # Draw sector for object speed calculations
    quadrilateral = [(579, 449), (510, 407), (635, 372), (713, 414)]
    draw.polygon(quadrilateral, fill="grey", outline="red")

    # Create a Polygon object from the quadrilateral coordinates
    polygon = Polygon(quadrilateral)

    # Make list of points inside the sector
    sp = []
    for index, row in df.iterrows():
        point = Point(row["x"], row["y"])
        if polygon.contains(point):
            sp.append([int(row['x']), int(row['y']), float(row['timestamp'])])

    # Calculate speed
    distance = 4 # Distance is taken based on maps.lt
    time = round(sp[-1][2] - sp[0][2], 2)
    speed = round(distance/time * 3.6, 2)
    print(speed, "km/h")

    # Set the font and size
    font = ImageFont.truetype("arial.ttf", 20)
    # Set the text to be drawn
    text = f"Sector speed: {str(speed)} km/h"
    # Draw the text on the image
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)

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
    ax.imshow(img)
    ax.scatter(df['x'], df['y'], c=df['id'], s=6)
    # Save the plot to a file
    plt.savefig(f'_data/_images/scatter_speed_{track_file}.png')

# List of plots
def draw_plots():
    # Data Frame
    df = tracks(everynth)

    # Calculate speed if specific object selected
    if objectId != 0:
        df = df[df['id'] == objectId]
        scatter_speed(df)
    else:
        scatter(df)
    
    scatter_3d(df)

    plt.show()

# Draw plots
draw_plots()