import numpy as np

# Path to your .npz motion file
motion_file = "G1_walk.npz"

# Load the .npz file
data = np.load(motion_file, allow_pickle=True)

print(data["body_names"])

# Print all keys to verify what’s inside
print("Available keys in the file:", list(data.keys()))

# Print DOF names
if "dof_names" in data:
    dof_names = data["dof_names"]
    print("\nDegrees of Freedom (DOF) names:")
    for name in dof_names:
        print(f" - {name}")
else:
    print("\nNo 'dof_names' found in the file.")

# Print body names
if "body_names" in data:
    body_names = data["body_names"]
    print("\nBody names:")
    for name in body_names:
        print(f" - {name}")
else:
    print("\nNo 'body_names' found in the file.")
