# Synthetic-Defect-Creation-in-3D-Point-Clouds

One of the major challenge faced today is the lack of sufficient data on defects, especially for manufacturing parts. These defects are random and unpredictable, varying in orientation, magnitude or place of defect. Hence, it is necessary to create datasets that can replicate the randomness of real world defects, particularly in the manufactruing sector. Many of the defect detection AI models require huge amount of datasets to train and GAN models require a huge dataset to train its generator and discriminator model in order produce accurate results. For this reason a python script has been developed that can create as many 3D defected point cloud files as determined by the user once the algorithm is provided with the ideal 3D point cloud.

## Types of Defects that the Algorithm can Generate

1. ### Bulge Defect
   For bulge defect the algorithm randomly chooses a point on the point cloud and it explodes/expands the points around that point in a certain radius.

2. ### Crack Defect
   For crack defect the algorithm removes points from the point cloud causing hollow spaces in 3D point cloud.

## Algorithm Explanation

1. Once the ideal point cloud is input by the user, the user is then asked to enter the number of defected point cloud files that he would like to generate.
2. Once the number of defected files is determined by the user, the algorithm then gives two choices, either to generate a bulge defect or generate a crack defect.
3. According to the choice of the user, a number of different defected 3D point cloud files are generated in the directory chosen by the user.
4. This dataset can now be used for GAN models or other AI models.

## Examples and Results

All the images are of visualization from python library open3d and as samples only 3 defected files were generated for each case

### Ideal Pictures of DDF (a car part) and Engine point cloud

#### DDF
![image](https://github.com/user-attachments/assets/b283ff31-5672-43b6-b36d-003d26e61a2d)

#### Engine
![image](https://github.com/user-attachments/assets/f644cfbd-83f1-4e31-88ae-abbafe0c3e37)

### Case 1: DDF PCD with Bulge Defect

#### Output file 1
![defective pcd 1](https://github.com/user-attachments/assets/b0042ceb-8588-4c63-b924-83e9b6efa608)

#### Output file 2
![defective pcd 2](https://github.com/user-attachments/assets/2102ec52-4714-48e2-bf9c-004fe27558e7)

#### Output file 3
![defective pcd 3](https://github.com/user-attachments/assets/2aade3d6-5a59-48c7-acd1-95b024908fd9)

### Case 2: DDF PCD with Crack Defect

#### Output file 1
![defected pcd 1](https://github.com/user-attachments/assets/c58ba5f7-5298-4208-82d0-70ab3ba347f5)

#### Output file 2
![defected pcd 2](https://github.com/user-attachments/assets/798c700c-1407-4c67-81bf-69f276d98d53)

#### Output file 3
![defected pcd 3](https://github.com/user-attachments/assets/e97af2c3-eac0-48da-b9c1-e4a9a47d5232)

### Case 3: Engine PCD with Bulge Defect

Note: For better visibility and understanding of defect the results of engine bulge defect below are shown after testing the defected files on the defected detection algorithm available in one of my repositories
#### Output file 1
![ideal and defected aligned 1](https://github.com/user-attachments/assets/9e51155c-61c3-4ee4-8421-ba188c616498)

#### Output file 2
![ideal and defected aligned 2](https://github.com/user-attachments/assets/d21f85a8-4038-4504-a2bc-2c203ff33a02)

#### Output file 3
![image](https://github.com/user-attachments/assets/1811c5c6-40c9-45f9-9f5b-5d9bf056f290)

### Case 3: Engine PCD with Crack Defect

#### Output file 1
![defective pcd 2](https://github.com/user-attachments/assets/8912be4a-656e-44e2-9bc6-0c2a1005bba2)

#### Output file 2
![defective pcd 1](https://github.com/user-attachments/assets/ce5923d7-ad24-4e8f-bd43-bd560a53361c)

#### Output file 3
![defected pcd 3](https://github.com/user-attachments/assets/b283803a-75d6-4f76-a218-3ecc118630c4)

## Conclusion

With this algorithm a hufe dataset of defected algorithms can be built. In addition to it, the defect detection algorithm in one of my repositories can be used to verify the defects as well










