## MOIL SDK For Python

MOIL SDK for python is a collection of functions support python to developments fisheye image applications. this function using share object library C++ wrapper by ctypes python

1. import library

   ```
   from Moildev import Moildev
   ```

2. API Reference

   2.1 init configuration

   This is the initial configuration that you need provide the parameter. The camera parameter is the result from calibration camera by MOIL laboratory.  before the successive functions can work correctly, configuration is necessary in the beginning of program.

   ```
   moildev = Moildev(camera_name, sensor_width, sensor_height, Icx, Icy, ratio, 
   			imageWidth, imageHeight, parameter0, parameter1, parameter2, parameter3,
               parameter4, parameter5, calibrationRatio)
   ```

   parameter:

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

   Example:

   ```
   moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
   					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)
   ```

   2.2 anypointM

   ```
   moildev.AnyPointM(mapX, mapY, w, h, alphaOffset, betaOffset, zoom, m_ratio)
   ```

   purpose:

   Anypoint Mode 1, the purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters, the result X-Y Maps can be used later to remap the original fisheye image to the target angle image. The result rotation is betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch).

   parameter:

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

   **Example** :

   ```
   from Moildev import Moildev
   moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048, 
   					2592, 1944, 4.05,0, 0, 0, 0, -47.96, 222.86)
   
   m_ratio = 2592/ sensor_width;
   mapX = np.zeros((h, w), dtype=np.float32)
   mapY = np.zeros((h, w), dtype=np.float32)
   image_input = imread( "image.jpg")
   
   moildev.AnyPointM(mapX, mapY, w, h, alphaOffset, betaOffset, self.zoom, m_ratio)
   result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
   ```

   2.2 

