import numpy as np
from bvh import Bvh
import sys

def load_bvh_motion(bvh_file_path):
    with open(bvh_file_path, 'r') as f:
        mocap = Bvh(f.read())

    joint_names = mocap.get_joints_names()
    frame_time = mocap.frame_time
    n_frames = mocap.nframes

    motion_data = []

    for i in range(n_frames):
        frame_data = []
        for joint in joint_names:
            try:
                channels = mocap.joint_channels(joint)
                if channels:
                    joint_data = mocap.frame_joint_channel(i, joint, channels)
                    frame_data.extend(joint_data)
                else:
                    print(f"Warning: No channels found for joint {joint}")
            except Exception as e:
                print(f"Error with joint {joint}: {e}")
                frame_data.extend([0.0] * 6)  # Use a default value for missing data

    motion_data = np.array(motion_data, dtype=np.float32)
    frame_times = np.arange(n_frames) * frame_time

    return {
        'motion': motion_data,
        'frame_times': frame_times
    }

def save_as_npz(output_path, motion_dict):
    np.savez_compressed(output_path, **motion_dict)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bvh_to_npz.py input_file.bvh output_file.npz")
        sys.exit(1)

    input_bvh = sys.argv[1]
    output_npz = sys.argv[2]

    print(f"Converting {input_bvh} to {output_npz}...")
    motion_dict = load_bvh_motion(input_bvh)
    save_as_npz(output_npz, motion_dict)
    print("Conversion complete.")
