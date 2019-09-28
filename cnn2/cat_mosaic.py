import cv2
class CatMosaic:
    def __init__(self):
        self._fname = './data/cat.jpg'

    def img_mosaic(self):
        img = cv2.imread(self._fname, cv2.IMREAD_COLOR)
        mos = self.mosaic(img, (50,50,450,450),10)
        cv2.imwrite('cat-mosaic.png', mos)
        cv2.imshow('CAT', mos)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def mosaic(img, rect, size):
        (x1, y1, x2, y2) = rect
        w = x2 - x1
        h = y2 - y1
        i_rect = img[y1:y2, x1:x2]
        i_small = cv2.resize(i_rect, (size, size))
        i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
        img2 = img.copy()
        img2[y1:y2, x1:x2] = i_mos
        return img2