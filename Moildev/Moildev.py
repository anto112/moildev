import ctypes
import os
import sys


dir = os.path.dirname(os.path.realpath(__file__)) #os.path.dirname(sys.modules["moildev"].__file__)
path = os.path.join(dir, "moildev.so")
lib = ctypes.cdll.LoadLibrary(path)


class Moildev:
    """Python wrapper for Moildev library."""

    def __init__(self, name, sensor_width, sensor_height, Icx, Icy, ratio, imageWidth, imageHeight,
                 parameter0, parameter1, parameter2, parameter3, parameter4, parameter5, calibrationratio):
        """
        This is the initial configuration that you need provide the parameter. The camera parameter is the result from
        calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration is
        necessary in the beginning of program.


        Args:
            . camera_name - A string to describe this camera
            . sensor_width - Camera sensor width (cm)
            . sensor_height - Camera Sensor Height (cm)
            . Icx - image center X coordinate(pixel)
            . Icy - image center Y coordinate(pixel)
            . ratio : Sensor pixel aspect ratio.
            . imageWidth : Input image width
            . imageHeight : Input image height
            . parameter0 .. parameter5 : calibrationration parameters
            . calibrationrationratio : input image with/ calibrationration image width

        for more detail, please reference https://github.com/anto112/moildev
        """
        lib.moildev_new.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double]
        lib.moildev_new.restype = ctypes.c_void_p

        self.obj = lib.moildev_new(name, sensor_width, sensor_height, Icx, Icy, ratio, imageWidth, imageHeight,
                                   parameter0, parameter1, parameter2, parameter3, parameter4, parameter5,
                                   calibrationratio)

    def test(self):
        """
        Test to link with Moildev share library


        Returns:
            Hello from C++
        """
        lib.test.argtypes = [ctypes.c_void_p]
        lib.test.restype = ctypes.c_void_p
        return lib.test(self.obj)

    def clean(self):
        """
        clean the memory of pointer


        Returns:
            None

        """
        lib.cleanup_moildev.argtypes = [ctypes.c_void_p]
        lib.cleanup_moildev.restype = ctypes.c_void_p
        return lib.cleanup_moildev(self.obj)

    def Rotate(self, w, h, src, dst, angle):
        """
        Turn an image in a clockwise or counterclockwise direction.


        Args:
            w: image width
            h: image height
            src: original image
            dst: matrix for destination image ( the size same with original image)
            angle: the value angle for turn the image


        Returns:
            dst image


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_rotate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p),
                                    ctypes.POINTER(ctypes.c_void_p), ctypes.c_double]

        lib.moil_rotate.restype = None
        src = src.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        dst = dst.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        lib.moil_rotate(self.obj, w, h, src, dst, angle)

    def AnyPointM(self, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification):
        """
        Anypoint Mode 1, the purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom
        parameters, the result X-Y Maps can be used later to remap the original fisheye image to the target angle
        image. The result rotation is betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree
        rotation around the X-axis(pitch).


        Args:
            . mapX : memory pointer of result X-Map
            . mapY : memory pointer of result Y-Map
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . alphaOffset : alpha offset
            . betaOffset : beta offset
            . zoom : decimal zoom factor, normally 1..12
            . magnification : input imageWidth / sensor_width, m_ratio is normally equal to 1.


        Returns:
            New mapX and mapY.


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_anypointM.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                       ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                       ctypes.c_double]
        lib.moil_anypointM.restype = None
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_anypointM(self.obj, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification)

    def AnyPointM2(self, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification):
        """
        Anypoint mode 2, the purpose is to generate a pair of X-Y Maps for the specified thetaX, thetaY and zoom
        parameters, the result X-Y Maps can be used later to remap the original fisheye image to the target angle
        image. The result rotation is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation
        around the X-axis(pitch).


        Args:
            . mapX : memory pointer of result X-Map
            . mapY : memory pointer of result Y-Map
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . thetaX_degree : thetaX
            . thetaY_degree : thetaY
            . zoom : decimal zoom factor, normally 1..12
            . magnification : input imageWidth / sensor_width, m_ratio is normally equal to 1.


        Returns:
             New mapX and mapY.


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_anypointM2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                        ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                        ctypes.c_double]
        lib.moil_anypointM2.restype = None

        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_anypointM2(self.obj, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification)

    def PanoramaM(self, mapX, mapY, w, h, magnification, alpha_max):
        """
        To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image.


        Args:
            . mapX : memory pointer of result X-Map
            . mapY : memory pointer of result Y-Map
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . magnification : input imageWidth / sensor_width, m_ratio is normally equal to 1.
            . alpha_max : max of alpha. The recommended vaule is half of camera FOV. For example, use
                          90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.


        Returns:
            New mapX and mapY.


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_revPanorama.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p),
                                         ctypes.POINTER(ctypes.c_void_p),
                                         ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double]
        lib.moil_revPanorama.restype = None

        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaM(self.obj, mapX, mapY, w, h, magnification, alpha_max)

    def PanoramaM_Rt(self, mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree):
        """
        To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image. The panorama image centered at the 3D
        direction with alpha = iC_alpha_degree and beta = iC_beta_degree.


        Args:
            . mapX : memory pointer of result X-Map
            . mapY : memory pointer of result Y-Map
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . magnification : input imageWidth / sensor_width, m_ratio is normally equal to 1.
            . alpha_max : max of alpha. The recommended vaule is half of camera FOV. For example, use
              90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            . iC_alpha_degree : alpha angle of panorana center.
            . iC_beta_degree : beta angle of panorama center.


        Returns:
            New mapX and mapY.


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_panoramaM_Rt.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float),
                                          ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int, ctypes.c_double,
                                          ctypes.c_double, ctypes.c_double, ctypes.c_double]
        lib.moil_panoramaM_Rt.restype = None

        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaM_Rt(self.obj, mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree)

    def revPanoramaM(self, panoImage, result, w, h, alpha, beta):
        """
        To generate the image reverse image from panorama that can change the focus direction from the original images.
        The panorama reverse image centered at the 3D direction with alpha_max = max of alpha and beta = iC_beta_degree.


        Args:
            . panoImage : Input of panorama_Rt image
            . result :  Memory pointer of result image
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . alpha_max : max of alpha. The recommended vaule is half of camera FOV. For example, use
                        90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            . iC_beta_degree : beta angle of panorama center.


        Returns:
            New mapX and mapY.


        Examples:
            please reference: https://github.com/anto112/moildev

        """
        lib.moil_panoramaM.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                       ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ]
        lib.moil_panoramaM.restype = None
        panoImage = panoImage.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        result = result.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        lib.moil_revPanorama(self.obj, panoImage, result, w, h, alpha, beta)

    def PanoEdge90(self, w, h, mapX, mapY, alpha_width):
        """
        Args:
            w:
            h:
            mapX:
            mapY:
            alpha_width:

        Returns:

        """
        lib.moil_PanoEdge90.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
                                        ctypes.POINTER(ctypes.c_float), ctypes.c_int]

        lib.moil_PanoEdge90.restype = None

        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_PanoEdge90(self.obj, w, h, mapX, mapY, alpha_width)

    def Max(self, x, y):
        """
        to compare the value between x and y


        Args:
            x: value 1
            y: value 2


        Returns:
            the max value between x and y

        """
        lib.max.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        lib.max.restype = ctypes.c_int
        return lib.max(self.obj, x, y)
