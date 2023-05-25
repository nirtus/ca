from PIL import Image
import pandas as pd
import pyodbc

def object_data(object_id):
    # Connect to the database
    server = 'BITUTE'
    database = 'ca'
    username = 'ca'
    password = '****'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    # Define the SQL query as a string with a parameter placeholder
    sql_query = "EXEC calculate_delta_speed ?"
    # Stream the results directly into a Pandas dataframe with the parameter value
    df = pd.read_sql(sql_query, conn, params=[object_id])
    # Close the connection
    conn.close()
    # Return results
    return df  

def resize_image(image_path: str, resize_percentage: float):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width = int(width * resize_percentage / 100)
        new_height = int(height * resize_percentage / 100)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image_path)
