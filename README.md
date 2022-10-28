# Synthetic Data Generation in Satellite Imagery (Pipeline)

## Creating a Conda Environment
```
conda create -n synthetic_data_generation python=3.9
```
## Installation
```
pip install -r requirements.txt
```
## Usage
```
python main.py
```

## Synthetic 3D Objects to Dataset Generation

- Introduction
- 3D .STL Image 
- Transform Angle / Rotation
- Overlay Images – Synthetics Data

## Data augmentation

- Overcome challenge of limited data
- Diversity of the training data
- Smooth out the machine learning model
- Reduce the overfitting of data
- Help improve the performance and results


## 3D STL Image Animation

<!-- ![3D Airplane Animation](./imgs/3d-img-animation.gif) -->

![3D Airplane Animation](./imgs/3d-img-animation.gif)

## WorkFlow Diagram
![workflow1](./imgs/WorkFlow1.png)

## Overlay Images - Synthetic Data Generation

### Convert 3D objects to 2D images with rotation and tilt
![](./imgs/3dto2d%20(1).png)
![](./imgs/3dto2d%20(2).png)
![](./imgs/3dto2d%20(3).png)
![](./imgs/3dto2d%20(4).png)
![](./imgs/3dto2d%20(5).png)
![](./imgs/3dto2d%20(6).png)

<!-- <img src="./imgs/3dto2d%20(1).png" width=300 height=300>
<img src="./imgs/3dto2d%20(2).png" width=300 height=300>
<img src="./imgs/3dto2d%20(3).png" width=300 height=300>
<img src="./imgs/3dto2d%20(4).png" width=300 height=300>
<img src="./imgs/3dto2d%20(5).png" width=300 height=300>
<img src="./imgs/3dto2d%20(6).png" width=300 height=300> -->


### 2D Image to Tansparent Objects Generation
![2D Image to Tansparent Objects Generation](./imgs/img2tobj.png)
<br />

## Base as a background image from satellite imagery
![](./imgs/satellite_img1.jpg)
<!-- <img src="./imgs/satellite_img1.jpg" width=300 height=300> -->

## Overlay Images Overview
![](./imgs/overlay%20(1).png)
![](./imgs/overlay%20(2).png)
![](./imgs/overlay%20(3).png)
![](./imgs/overlay%20(4).png)
![](./imgs/overlay%20(5).png)
![](./imgs/overlay%20(6).png)
![](./imgs/overlay%20(7).png)
![](./imgs/overlay%20(8).png)

## Adding overlay images to background satellite imagery
![](./imgs/s_img%20(1).png)
![](./imgs/s_img%20(2).png)
![](./imgs/s_img%20(3).png)
![](./imgs/s_img%20(4).png)
<!-- <img src="./imgs/s_img%20(1).png" width=200 height=200>
<img src="./imgs/s_img%20(2).png" width=200 height=200>
<img src="./imgs/s_img%20(3).png" width=200 height=200>
<img src="./imgs/s_img%20(4).png" width=200 height=200> -->

## Execution time on local machine
![](./imgs/execution1.png)




