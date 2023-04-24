import seaborn as sns
import matplotlib.pyplot as plt
from _utils.helpers import *


def plot_line(object_id, reduce_step):
    df = object_data(object_id).iloc[::reduce_step]
    print(df)

    sns.lineplot(x=df.index, y='DeltaTime', data=df)
    # # Add labels and title
    plt.xlabel('Points')
    plt.ylabel('DeltaTime')
    plt.title('DeltaTime at Point')

df = object_data(130).iloc[::1]

fig = plt.figure()
ax = plt.axes(projection='3d')

x=[df['x2']]
y=[df['y2']]
z=[df['DeltaTime']]
obj_id = df['ObjId']

# ax.set_title("")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel ('DeltaTime')
ax.scatter(x, y, z, c=obj_id)


# Show plot
plt.show()
