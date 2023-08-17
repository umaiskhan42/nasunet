import os

directory = r"E:\NasUnet-master\NasUnet-master\binary_masks"  # Specify the directory where the images are located

for i in range(225):
    old_name = os.path.join(directory, f'frame{i:03d}.png')
    new_name = os.path.join(directory, f'frame{i+225:03d}.png')
    os.rename(old_name, new_name)