# -----------------------------------------------------------------------------------
# The script using sample ArUco marker of 3X3 cm as referance to measure the objects 
# height(d1), width(d2) and area = pi * d1/2 * d2/2
# here d1 and d2 are two different diameters of circular objects
# -----------------------------------------------------------------------------------

import cv2, numpy as np, math

# Load the image
img = cv2.imread('aruco_mark.png')
marker_size = 0.025

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(gray, 110, 130)
cv2.imshow('mask', mask)

cont, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Load the Aruco dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

# Initialize the detector
parameters = cv2.aruco.DetectorParameters() 
# if error occurs try use cv2.aruco.DetectorParameters_create() instead cv2.aruco.DetectorParameters()
# parameters = cv2.aruco.DetectorParameters_create()
# min_marker_size = int(marker_size * img.shape[0])
# parameters.minMarkerPerimeterRate = 0.03

# Detect the markers
corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

# Draw polygon around the marker
# int_corners = np.int0(corners)
# cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)
# Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 10

# Draw the detected markers and their IDs on the input image
img_c = img.copy()
dimg_markers = cv2.aruco.drawDetectedMarkers(img_c, corners, ids)
cx, cy, cw,ch = cv2.boundingRect(corners[0])
w, h = round(cw/pixel_cm_ratio,1), round(ch/pixel_cm_ratio, 1)

for i, corner in enumerate(corners):
    c = corner[0]
    x, y = int(np.mean(c[:, 0])), int(np.mean(c[:, 1]))
    # cv2.putText(dimg_markers, str(ids[i][0]), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.rectangle(dimg_markers, (cx,cy), (cx+cw, cy+ch), (255,0,0), 2)
    # cv2.rectangle(dimg_markers, (int(c[:, 0].min()), int(c[:, 1].min())), (int(c[:, 0].max()), int(c[:, 1].max())), (0, 255, 0), 2)
cv2.putText(dimg_markers, f'{w} x {h}', (x-70, y-110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('Markers', dimg_markers)

# large_cont = sorted(cont, key=lambda x: cv2.contourArea(x), reverse=True)
for c in cont:
    if cv2.contourArea(c) > 100:
        # cv2.drawContours(img, c, -1, 255, 3)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        w = round(w/pixel_cm_ratio, 1)
        h = round(h/pixel_cm_ratio, 1)
        ca = round(math.pi * (w/2) * (h/2))
        cv2.putText(img, f"w:{w}cm h:{h}cm a:{ca}sq.cm", (x,y-3), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)

    else:
        print("noise obj")

# Display the output image
cv2.imshow('Aruco marker detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
