import numpy as np
import cv2
from sklearn.cluster import KMeans

#import matplotlib.pyplot as plt
#from google.colab.patches import cv2_imshow


class IMG:
  def __init__(self, dir):
    image = cv2.imread(dir)
    dst = self.img_correction(image)

    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    dst = dst.reshape((dst.shape[0] * dst.shape[1], 3))

    clt = KMeans(n_clusters = 3,max_iter=50, n_init=3)
    clt.fit(dst)

    hist = self.centroid_histogram(clt)

    m = list(hist).index(max(hist))
    rgb = clt.cluster_centers_[m]
    rgb = np.uint8([[[round(rgb[0]), round(rgb[1]), round(rgb[2])]]])

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hsv = self.map_hsv(hsv)
    self.hsv = hsv
  
  def map_hsv(self, hsv):
    h, s, v = cv2.split(hsv)
    h *= 2
    s = s/255*100
    v = v/255*100
    hsv = (int(h),int(s),int(v))
    return hsv

  def increase_brightness(self, img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    bgr = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bgr
  
  def img_correction(self, img):
    h, w, c = img.shape
    img = img[h//8:h*7//8, w//8:w*7//8]
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
    img = self.increase_brightness(img,60)
    blur = cv2.pyrUp(img)

    corr = blur.astype(np.float)
    corr =((corr/255)**1.7)*255

    corr = corr.astype(np.float32)
    #cv2_imshow(corr)
    return corr
  
  def centroid_histogram(self, clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
  

class HSV:
  def __init__(self, hsv):
    self.hsv = hsv

  def get_color(self):
    h = self.hsv[0]
    s = self.hsv[1]
    v = self.hsv[2]
    color_dict = {
        0:"붉은", 1:"주황", 2:"노란", 3:"녹", 4:"청", 5:"파란", 6:"보라", 7:"분홍",
        100:"흰", 101:"회", 102:"검은"
    }
    gray = False
    black = False
    dark = False
      
    gray_dict={
      1: 80, 2: 60, 3: 40, 4: 30,
      5: 25, 6: 25, 7: 25, 8: 25,
      9: 20, 10: 20
    }
    black_dict={
      1: 30, 2: 30, 3: 25, 4: 25, 5: 25
    }
    
    if s>10:
      if h>330 or h<20: c = 0
      elif h<30:        c = 1
      elif h<70:        c = 2
      elif h<145:       c = 3
      elif h<200:       c = 4
      elif h<260:       c = 5
      elif h<290:       c = 6
      else:             c = 7

      if v < gray_dict[s//10]: gray = True
      if gray and (s//10>5 or v < black_dict[s//10]): black = True

      if black:       c = 102
      elif gray:      c = 101
      else:
        dark_dict={
            4: 50, 5: 50, 6: 50, 7: 50, 8: 50, 9: 60, 10: 60
        }
        if s//10>3 and v<dark_dict[s//10]: 
          dark = True

      
    else:
      if v>80:          c = 100
      elif v>30:        c = 101
      else:             c = 102
    
    if dark:
        dark_color={
            0:"검붉은", 1:"갈", 2:"카키", 5:"남"
        }
        if c in dark_color.keys():
          color = dark_color[c]
    else:
      color = color_dict[c] 
    
    color += "색"
  
    return color