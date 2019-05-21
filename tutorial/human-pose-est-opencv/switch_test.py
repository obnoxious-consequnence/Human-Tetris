import random

def t_pose():
    return 'Do a T-Pose'

def y_pose():
    return 'Do a Y-Pose'

def i_pose():
    return 'Do a I-Pose'

def x_pose():
    return 'Do a X-Pose'

def get_pose(pose):
    switcher = {
        0: t_pose(),
        1: y_pose(),
        2: i_pose(),
        3: x_pose(),
    }
    return switcher.get(pose, "nothing") 

poses = [0, 1, 2, 3]
for x in range(0, len(poses)):
    # pose = random.choice(poses)
    pose = random.choice(poses)
    poses.remove(pose)
    print(get_pose(pose))