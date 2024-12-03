import open3d as o3d
import numpy as np
import pandas as pd
import os
import random
import os
# Set paths and parameters

output_folder = input('path to output folder of defected files: ')#'D:\\Additech\\TEF\\wavelet detection\\defective_clouds_1'
num_defective_files = int(input('enter number of defected files you want to create: '))#10         # Number of defective files to generate
#points_to_select = 2             # Number of random points to select for the bulge
#bulge_magnitude = 30           # Magnitude of the bulge

# Load the point cloud data
input_file=input('path to the point cloud you want to create the defect in (in .txt format): ')
df = pd.read_csv(input_file, delimiter=';', header=None)#('D:\Additech\TEF\wavelet detection\simulated_cloud.txt', delimiter=';', header=None)

# Save the data in XYZ format
df.to_csv('point_cloud.xyz', header=False, index=False, sep=' ')
pcd = o3d.io.read_point_cloud("point_cloud.xyz")

# Get the minimum and maximum bounds of the point cloud
min_bound = pcd.get_min_bound()
max_bound = pcd.get_max_bound()

# Calculate the scale as the diagonal length of the bounding box
original_scale = np.linalg.norm(max_bound - min_bound)
print("original Scale of the point cloud:", original_scale)
target_scale = 1.25

scaling_factor = target_scale / original_scale

pcd.scale(scaling_factor, center=pcd.get_center())
min_bound = pcd.get_min_bound()
max_bound = pcd.get_max_bound()
final_scale = np.linalg.norm(max_bound - min_bound)
print("final Scale of the point cloud:", final_scale)
#np.savetxt("F:\Additech\TEF\wavelet detection\scaled_point_cloud.txt", np.asarray(pcd.points), delimiter=';')
os.remove('point_cloud.xyz')
try:
    Input=input('Press B or b for bulge defect creation, Press C or c for crack defect creation')
    original_points = np.asarray(pcd.points)
    points_to_select = 2

    if Input=='B' or Input=='b':
    # Function to displace points outward to create the bulge
        def apply_bulge_to_points(points, picked_indices, magnitude):
            # Compute the centroid of the picked points as the bulge center
            bulge_center = np.mean(points[picked_indices], axis=0)
            
            # Define a bulge radius based on the maximum distance of selected points from the center
            distances = np.linalg.norm(points[picked_indices] - bulge_center, axis=1)
            bulge_radius = np.max(distances)
            
            # Apply the bulge effect to all points near the selected region
            for i, point in enumerate(points):
                distance = np.linalg.norm(point - bulge_center)
                if distance < bulge_radius:
                    direction = (point - bulge_center) / distance
                    displacement = (1 - distance / bulge_radius) * magnitude
                    points[i] = point + direction * displacement

            return points

        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)

        # Generate multiple defective files
        for i in range(num_defective_files):
            # Create a copy of the original points to ensure each file starts with the unmodified point cloud
            points = original_points.copy()

            # Randomly pick points for bulging
            picked_indices = np.random.choice(len(points), points_to_select, replace=False)
            bulge_magnitude = random.uniform(0.02, 0.1)#random.randint(0.02,0.1) 
            # Apply bulge effect to the selected random points
            modified_points = apply_bulge_to_points(points, picked_indices, bulge_magnitude)
            
            # Save each defective point cloud to a separate file
            output_file = os.path.join(output_folder, f'bulge_defective_cloud_{i+1}.txt')
            np.savetxt(output_file, modified_points, delimiter=';')
            #print(f"Defective file saved: {output_file}")
            df = pd.read_csv(output_file, delimiter=';', header=None)#('D:\Additech\TEF\wavelet detection\simulated_cloud.txt', delimiter=';', header=None)

            # Save the data in XYZ format
            df.to_csv('output_point_cloud.xyz', header=False, index=False, sep=' ')
            pcd = o3d.io.read_point_cloud("output_point_cloud.xyz")
            os.remove('output_point_cloud.xyz')
            os.remove(output_file)
            # Get the minimum and maximum bounds of the point cloud
            min_bound = pcd.get_min_bound()
            max_bound = pcd.get_max_bound()

            # Calculate the scale as the diagonal length of the bounding box
            new_original_scale = np.linalg.norm(max_bound - min_bound)
            print("original Scale of the point cloud: ", new_original_scale)
            new_target_scale = original_scale

            scaling_factor = new_target_scale / new_original_scale

            pcd.scale(scaling_factor, center=pcd.get_center())
            min_bound = pcd.get_min_bound()
            max_bound = pcd.get_max_bound()
            final_scale = np.linalg.norm(max_bound - min_bound)
            print("final Scale of the point cloud: ", final_scale)
            #output_file=f"F:\Additech\TEF\wavelet detection\compare with simulated\scaled_final_point_cloud_{i+1}.txt"
            np.savetxt(output_file, np.asarray(pcd.points), delimiter=';')
            print(f"Defective file saved: {output_file}")
                        
                    
                    

    elif Input=='C' or Input=='c':
        def generate_zigzag_path(start, end, num_zigs=5, amplitude=0.05):
            #"""Generate a zigzag path between start and end points."""
            direction = end - start
            length = np.linalg.norm(direction)
            unit_direction = direction / length

            # Perpendicular vector for zigzag (arbitrary perpendicular vector)
            if unit_direction[0] == 0 and unit_direction[1] == 0:
                perpendicular = np.array([1, 0, 0])  # If direction is along Z axis, use X axis
            else:
                perpendicular = np.cross(unit_direction, np.array([0, 0, 1]))

            # Normalize perpendicular vector
            perpendicular = perpendicular / np.linalg.norm(perpendicular)

            # Generate zigzag points
            zigzag_points = []
            for i in range(num_zigs + 1):
                t = i / num_zigs
                point_on_line = start + t * direction
                offset = amplitude * np.sin(i * np.pi) * perpendicular
                zigzag_points.append(point_on_line + offset)

            return np.array(zigzag_points)

        def remove_points_along_path(points, path, radius=0.05):
            #"""Remove points from the point cloud that are within a certain radius of the zigzag path."""
            mask = np.ones(len(points), dtype=bool)  # Initially keep all points
            for segment_start, segment_end in zip(path[:-1], path[1:]):
                # Find points within the radius of the line segment
                line_dir = segment_end - segment_start
                line_length = np.linalg.norm(line_dir)
                if line_length == 0:
                    continue
                line_dir = line_dir / line_length
                to_points = points - segment_start
                projections = np.dot(to_points, line_dir)
                closest_points = segment_start + np.outer(projections, line_dir)
                distances = np.linalg.norm(points - closest_points, axis=1)

                # Remove points that are within the radius
                mask &= distances > radius

            return points[mask]

        points = np.asarray(pcd.points)
        
        radius = 0.05    # Radius for removing points along the crack path

        for i in range(num_defective_files):
            # Randomize parameters for each crack
            num_zigs = random.randint(5, 15)   # Random number of zigzags between 5 and 15
            amplitude = random.uniform(0.05, 0.2)  # Random amplitude between 0.05 and 0.2

            # Randomly select two distinct points from the point cloud
            random_indices = random.sample(range(len(points)), 2)
            random_start_point = points[random_indices[0]]
            random_end_point = points[random_indices[1]]

            # Generate a zigzag path between the two points
            zigzag_path = generate_zigzag_path(random_start_point, random_end_point, num_zigs=num_zigs, amplitude=amplitude)

            # Remove points along the zigzag path
            points_with_crack = remove_points_along_path(points, zigzag_path, radius=radius)

            # Save the modified point cloud as a text file using np.savetxt
            output_file = os.path.join(output_folder, f'crack_defective_cloud_{i+1}.txt')    
            np.savetxt(output_file, points_with_crack, delimiter=";")
            
            #print(f"Point cloud with crack {i + 1} saved as '{output_file}'")
            df = pd.read_csv(output_file, delimiter=';', header=None)#('D:\Additech\TEF\wavelet detection\simulated_cloud.txt', delimiter=';', header=None)

            # Save the data in XYZ format
            df.to_csv('output_point_cloud.xyz', header=False, index=False, sep=' ')
            pcd = o3d.io.read_point_cloud("output_point_cloud.xyz")
            os.remove('output_point_cloud.xyz')
            os.remove(output_file)
            # Get the minimum and maximum bounds of the point cloud
            min_bound = pcd.get_min_bound()
            max_bound = pcd.get_max_bound()

            # Calculate the scale as the diagonal length of the bounding box
            new_original_scale = np.linalg.norm(max_bound - min_bound)
            print("original Scale of the point cloud: ", new_original_scale)
            new_target_scale = original_scale

            scaling_factor = new_target_scale / new_original_scale

            pcd.scale(scaling_factor, center=pcd.get_center())
            min_bound = pcd.get_min_bound()
            max_bound = pcd.get_max_bound()
            final_scale = np.linalg.norm(max_bound - min_bound)
            print("final Scale of the point cloud: ", final_scale)
            #output_file=f"F:\Additech\TEF\wavelet detection\compare with simulated\scaled_final_point_cloud_{i+1}.txt"
            np.savetxt(output_file, np.asarray(pcd.points), delimiter=';')
            print(f"Point cloud with crack {i + 1} saved as '{output_file}'")
            #print(f"Defective file saved: {output_file}")
except:
     print('error in choice of defect letter input or cannot read file')