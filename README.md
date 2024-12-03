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

All the images are of visualization from python library open3d

### Ideal Pictures of DDF (a car part) and Engine point cloud

#### DDF
![image](https://github.com/user-attachments/assets/b283ff31-5672-43b6-b36d-003d26e61a2d)

#### Engine
![image](https://github.com/user-attachments/assets/f644cfbd-83f1-4e31-88ae-abbafe0c3e37)





