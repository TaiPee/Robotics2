import cv2 as cv
import numpy as np
import requests
from haversine import haversine
import geonav_conversions as gc


##########   CONSTANTS   ##########
# Obtaining Google Maps API IMAGE
GPS_MARKERS = [(38.7376103903459,-9.13892521638698),(38.735631349807996,-9.138723252002077)] # 1st is zero of frame and 2nd is a point in the negative part of y-axis
GPS_CENTER = (38.736747422021644,-9.138782702055112)
MARKER_ICON_LINK = 'https://i.postimg.cc/g2NNh7XK/Pixel-red.png'
MAP_ID = {'lines':'9d133c1ebd1d6a7e',
          'filled':'cadcb0f8ca8bbcec'}

MAP_PARAMETERS = {
    'center':f'{GPS_CENTER[0]},{GPS_CENTER[1]}',
    'zoom':18,
    'size':'1280x1280',
    'scale':2,
    'markers':f'icon:{MARKER_ICON_LINK}|{GPS_MARKERS[0][0]},{GPS_MARKERS[0][1]}|{GPS_MARKERS[1][0]},{GPS_MARKERS[1][1]}',
    'map_id':MAP_ID['lines'], # 'lines' or 'filled'
    'key':'AIzaSyCKuSK8xL3HkvP0xINBxb3n1yDxWWvwxHk',
    # 'maptype':'satellite'
}

GOOGLE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'

# Google Maps API image processing
BOTTOM_LEFT_LOGO_PROPORTIONS = (0.95, 0.11)
BOTTOM_RIGHT_LOGO_PROPORTIONS = (0.97, 0.8)



def transparent2white_background(filename):
    image_4channel = cv.imread(filename, cv.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:,:,3]
    rgb_channels = image_4channel[:,:,:3]

    # White Background Image
    white_background_image = np.ones_like(rgb_channels, dtype=np.uint8) * 255

    # Alpha factor
    alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = white_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    return final_image.astype(np.uint8)
    

def remove_logos(filename):
    image_4channel = cv.imread(filename, cv.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:,:,3]

    x_pixels = alpha_channel.shape[0]
    y_pixels = alpha_channel.shape[1]

    # Remove bottom left logo
    X = int(BOTTOM_LEFT_LOGO_PROPORTIONS[0] * x_pixels)
    Y = int(BOTTOM_LEFT_LOGO_PROPORTIONS[1] * y_pixels)
    alpha_channel[X:,:Y] = np.zeros_like(alpha_channel[X:,:Y])

    # Remove bottom right logo
    X = int(BOTTOM_RIGHT_LOGO_PROPORTIONS[0] * x_pixels)
    Y = int(BOTTOM_RIGHT_LOGO_PROPORTIONS[1] * y_pixels)
    alpha_channel[X:,Y:] = np.zeros_like(alpha_channel[X:,Y:])


    image_4channel[:,:,3] = alpha_channel
    return image_4channel


def process_image(filename):
    new_filename = filename.split('.')[0] + '_processed.png'

    img = remove_logos(filename)

    cv.imwrite(new_filename, img)
    img = transparent2white_background(new_filename)
    cv.imwrite(new_filename, img)

    print(f'Image processed at: {new_filename}')
    return new_filename

def obtain_map(url=GOOGLE_URL, params=MAP_PARAMETERS, filename='maps_process/mapx.png'):
    with requests.get(url, params) as response:
        print(f'Getting image from: {response.url}')
        if response.status_code:
            with open(filename, 'wb') as f:
                f.write(response.content)
                print(f'Image downloaded at: {filename}')
        response.close()


def detect_markers(filename):
    def are_neighbours(p1, p2, threshold=3):
        distance = np.linalg.norm(p1 - p2)
        return distance <= threshold

    # Obtain mask with pixels
    lower = np.array([36, 28, 237], dtype = "uint8") 
    upper = np.array([36, 28, 237], dtype = "uint8")

    img = cv.imread(filename)
    mask = cv.inRange(img, lower, upper)

    # Extract pixels
    marker_pixels = np.transpose(np.nonzero(mask))
    
    # Select only one point of each cluster
    marker_points = np.empty((0,2))
    while marker_pixels.size > 0:
        pixel = marker_pixels[0]
        marker_points = np.append(marker_points, [pixel], axis=0)

        mask = [not are_neighbours(pixel, pixel_i) for pixel_i in marker_pixels]

        marker_pixels = marker_pixels[mask]

    return marker_points

def create_R_matrix(image_points, gps_points):
    pts = {
        'up_pt': {
            'image_pnt':image_points[0],
            'gps_pnt':gps_points[0]
        },
        'down_pt': {
            'image_pnt':image_points[1],
            'gps_pnt':gps_points[1]
        }
    }

    ix1 = pts['up_pt']['image_pnt'][0]
    iy1 = pts['up_pt']['image_pnt'][1]
    ix2 = pts['down_pt']['image_pnt'][0]
    iy2 = pts['down_pt']['image_pnt'][1]
    (ry1, rx1, _) = gc.LLtoUTM(GPS_MARKERS[0][0],GPS_MARKERS[0][1])
    (ry2, rx2, _) = gc.LLtoUTM(GPS_MARKERS[1][0],GPS_MARKERS[1][1])

    # Solving system of equations to determine parameters based on 2 points
    A = np.array([[ix1, iy1, 1, 0],
                  [iy1, -ix1, 0, 1],
                  [ix2, iy2, 1, 0],
                  [iy2, -ix2, 0, 1]])
    b = np.array([rx1, ry1, rx2, ry2])   

    x = np.linalg.solve(A, b)
    a, b, tx, ty = x

    # Construct R matrix
    R = np.array([[a, b, tx], [-b, a, ty], [0, 0, 1]])

    return R


if __name__ == "__main__":
    filename = 'maps_process/ist_map.png'
    obtain_map(filename=filename)
    filename = process_image(filename)

    print(create_R_matrix(detect_markers(filename), GPS_MARKERS))
