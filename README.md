## MOIL SDK For Python

MOIL SDK for python is a collection of functions support python to developments fisheye image applications. this function using share object library C++ wrapper by **ctypes** python and work just in ***Linux Operating system (OS)***.

### 1. Import Library

```
from Moildev import Moildev
```

### 2. API Reference

#### 2.1 Initial configuration

This is the initial configuration that you need provide the parameter. The camera parameter is the result from calibration camera by MOIL laboratory.  before the successive functions can work    correctly,configuration is necessary in the beginning of program.

```
moildev = Moildev(camera_name, sensor_width, sensor_height, Icx, Icy, ratio, 
			imageWidth, imageHeight, parameter0, parameter1, parameter2, parameter3,
            parameter4, parameter5, calibrationRatio)
```

##### Parameter:

```
. camera_name - A string to describe this camera
. sensor_width - Camera sensor width (cm)
. sensor_height - Camera Sensor Height (cm)
. Icx - image center X coordinate(pixel)
. Icy - image center Y coordinate(pixel)
. ratio : Sensor pixel aspect ratio.
. imageWidth : Input image width
. imageHeight : Input image height  
. calibrationRatio : input image with/ calibration image width
. parameter0 .. parameter5 : calibration parameters
```

##### Example:

```
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)
```

#### 2.2 test

```
moildev.test()
```

##### Purpose:

The function will return feedback from share object library to make sure the library work properly.

##### Example:

```
from Moildev import Moildev
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)
moildev.test()
```

#### 2.3 AnypointM

```
moildev.AnyPointM(mapX, mapY, w, h, alphaOffset, betaOffset, zoom, m_ratio)
```

##### Purpose:

Anypoint Mode 1, the purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters, the result X-Y Maps can be used later to remap the original fisheye image to the target angle image. The result rotation is betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch).

##### Parameter:

```
. mapX : memory pointer of result X-Map   
. mapY : memory pointer of result Y-Map
. w : width of the Map (both mapX and mapY)
. h : height of the Map (both mapX and mapY)
. alphaOffset : alpha offset 
. betaOffset : beta offset
. zoom : decimal zoom factor, normally 1..12
. m_ratio : input imageWidth / sensor_width, m_ratio is normally equal to 1.  
```

##### Example :

```
from Moildev import Moildev
import cv2
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)

m_ratio = 2592/ sensor_width;
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
image_input = cv2.imread( "image.jpg")

moildev.AnyPointM(mapX, mapY, w, h, alphaOffset, betaOffset, self.zoom, m_ratio)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
```

#### 2.3 AnyPointM2

```
moildev.AnyPointM(mapX, mapY, w, h, thetaX_degree, thetaY_degree, zoom, m_ratio)
```

##### Purpose :

Anypoint mode 2, the purpose is to generate a pair of X-Y Maps for the specified thetaX, thetaY and zoom parameters, the result X-Y Maps can be used later to remap the original fisheye image to the target angle image. The result rotation is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch).

##### Parameter:

```
. mapX : memory pointer of result X-Map   
. mapY : memory pointer of result Y-Map
. w : width of the Map (both mapX and mapY)
. h : height of the Map (both mapX and mapY)
. thetaX_degree : thetaX 
. thetaY_degree : thetaY
. zoom : decimal zoom factor, normally 1..12
. m_ratio : input imageWidth / sensor_width, m_ratio is normally equal to 1.  
```

##### Example :

```
from Moildev import Moildev
import cv2
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)

m_ratio = 2592/ sensor_width;
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
image_input = cv2.imread( "image.jpg")

moildev.AnyPointM2(mapX, mapY, w, h, thetaX_degree, thetaY_degree, self.zoom, m_ratio)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
```

#### 2.4 PanoramaM

```
PanoramaM(mapX, mapY, w, h, m_ratio, alpha_max)
```

##### Purpose :

To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later to generate a panorama image from the original fisheye image.

##### Parameter:

```
. mapX : memory pointer of result X-Map   
. mapY : memory pointer of result Y-Map
. w : width of the Map (both mapX and mapY)
. h : height of the Map (both mapX and mapY)
. m_ratio : input imageWidth / sensor_width, m_ratio is normally equal to 1. 
. alpha_max : max of alpha. The recommended vaule is half of camera FOV. For example, use
  90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
```

##### Example :

```
from Moildev import Moildev
import cv2
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)

m_ratio = 2592/ sensor_width;
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
image_input = cv2.imread( "image.jpg")

moildev.PanoramaM(mapX, mapY, w, h, m_ratio, alpha_max)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
```

#### 2.4 PanoramaM_Rt

```
PanoramaM_Rt(mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree)
```

##### Purpose:

To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later to generate a panorama image from the original fisheye image. The panorama image centered at the 3D direction with alpha = iC_alpha_degree and beta = iC_beta_degree.

##### Parameter:

```
. mapX : memory pointer of result X-Map   
. mapY : memory pointer of result Y-Map
. w : width of the Map (both mapX and mapY)
. h : height of the Map (both mapX and mapY)
. m_ratio : input imageWidth / sensor_width, m_ratio is normally equal to 1.   
. alpha_max : max of alpha. The recommended vaule is half of camera FOV. For example, use
  90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
. iC_alpha_degree : alpha angle of panorana center.
. iC_beta_degree : beta angle of panorama center. 
```

##### Example :

```
from Moildev import Moildev
import cv2
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)

m_ratio = 2592/ sensor_width;
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
image_input = cv2.imread( "image.jpg")

moildev.PanoramaM_Rt(mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
```

#### 2.5 revPanorama

```
revPanorama(panoImage, result, w, h, iC_alpha_degree, iC_beta_degree)
```

##### Purpose:

....

....

##### Parameter:

```
. panoImage : Input of panorama_Rt image
. result :  Memory pointer of result image
. w : width of the Map (both mapX and mapY)
. h : height of the Map (both mapX and mapY)
. iC_alpha_degree : alpha angle of panorana center.
. iC_beta_degree : beta angle of panorama center. 
```

##### Example :

```
from Moildev import Moildev
import cv2
moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)

m_ratio = 2592/ sensor_width;
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
image_input = cv2.imread( "image.jpg")

moildev.PanoramaM_Rt(mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
moildev.revPanorama(panoImage, result, w, h, iC_alpha_degree, iC_beta_degree)
result = result
```

### 3. About Us

Omnidirectional, Surveillance and Imaging laboratory Ming Chi University of Technology, Taiwan



