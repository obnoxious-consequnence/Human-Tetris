import random
import test

def t_pose():
    return 'T-Pose'

def y_pose():
    return 'Y-Pose'

def i_pose():
    return 'I-Pose'

def x_pose():
    return 'X-Pose'

def get_pose(pose):
    switcher = {
        0: t_pose(),
        1: y_pose(),
        2: i_pose(),
        3: x_pose(),
    }
    return switcher.get(pose, "Nothing") 

poses = [0, 1, 2, 3]
len_poses = len(poses)
for x in range(0, len(poses)):
    pose = random.choice(poses)
    poses.remove(pose)

    req_pose = get_pose(pose)
    pose_img = test.cam_picture(x, req_pose, len_poses)
    test.openpose(pose_img, req_pose)

