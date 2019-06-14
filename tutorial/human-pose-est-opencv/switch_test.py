import random
import test


def t_pose():
    return 'T_Pose'

def y_pose():
    return 'Y_Pose'

def i_pose():
    return 'I_Pose'

def x_pose():
    return 'X_Pose'

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
    main_menu.assignment_menu(req_pose)
    
    pose_img = main_menu.cap_screen(x, req_pose, len_poses)

    test.openpose(pose_img, req_pose)