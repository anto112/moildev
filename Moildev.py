import ctypes

lib = ctypes.cdll.LoadLibrary('./moildev.so')


class Moildev(object):

    def __init__(self, name, cswidth, csheight, Icx, Icy, Ratio, ImWidth, ImHeight,
                 Para0, Para1, Para2, Para3, Para4, Para5, calibRatio):
        lib.moildev_new.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double]
        lib.moildev_new.restype = ctypes.c_void_p

        lib.test.argtypes = [ctypes.c_void_p]
        lib.test.restype = ctypes.c_void_p

        lib.cleanup_moildev.argtypes = [ctypes.c_void_p]
        lib.cleanup_moildev.restype = ctypes.c_void_p

        lib.moil_rotate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p),
                                    ctypes.POINTER(ctypes.c_void_p), ctypes.c_double]

        lib.moil_rotate.restype = None

        lib.moil_anypointM.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                       ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                       ctypes.c_double]
        lib.moil_anypointM.restype = None

        lib.moil_anypointM2.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                        ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                        ctypes.c_double]
        lib.moil_anypointM2.restype = None

        lib.moil_revPanorama.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p),
                                         ctypes.POINTER(ctypes.c_void_p),
                                         ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double]

        lib.moil_revPanorama.restype = None

        lib.moil_PanoEdge90.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
                                        ctypes.POINTER(ctypes.c_float), ctypes.c_int]

        lib.moil_PanoEdge90.restype = None

        lib.moil_panoramaM.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                                       ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ]
        lib.moil_panoramaM.restype = None

        lib.moil_panoramaM_Rt.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float),
                                          ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int, ctypes.c_double,
                                          ctypes.c_double, ctypes.c_double, ctypes.c_double]
        lib.moil_panoramaM_Rt.restype = None

        lib.max.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        lib.max.restype = ctypes.c_int

        self.obj = lib.moildev_new(name, cswidth, csheight, Icx, Icy, Ratio, ImWidth, ImHeight,
                                   Para0, Para1, Para2, Para3, Para4, Para5, calibRatio)

    def test(self):
        return lib.test(self.obj)

    def clean(self):
        return lib.cleanup_moildev(self.obj)

    def Rotate(self, w, h, src, dst, angle):
        src = src.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        dst = dst.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        lib.moil_rotate(self.obj, w, h, src, dst, angle)

    def AnyPointM(self, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification):
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_anypointM(self.obj, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification)

    def AnyPointM2(self, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification):
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_anypointM2(self.obj, mapX, mapY, w, h, alphaOffset, betaOffset, zoom, magnification)

    def PanoramaM(self, mapX, mapY, w, h, magnification, alpha_max):
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaM(self.obj, mapX, mapY, w, h, magnification, alpha_max)

    def PanoramaM_Rt(self, mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree):
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaM_Rt(self.obj, mapX, mapY, w, h, magnification, alpha_max, iC_alpha_degree, iC_beta_degree)

    def revPanorama(self, panoImage, result, w, h, alpha, beta):
        panoImage = panoImage.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        result = result.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
        lib.moil_revPanorama(self.obj, panoImage, result, w, h, alpha, beta)

    def PanoEdge90(self, w, h, mapX, mapY, alpha_width):
        mapX = mapX.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = mapY.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_PanoEdge90(self.obj, w, h, mapX, mapY, alpha_width)

    def Max(self, x, y):
        return lib.max(self.obj, x, y)
