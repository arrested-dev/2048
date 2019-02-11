##from pytesseract import image_to_string
from PIL import ImageGrab, Image
import numpy as np
import cv2
import time
import json

### top right window boundaries 342 x 537
# inside playable permimeter 281 x 281

# mid pixel - 171`
# playable absolute boundaries (30.5, 203, 312.5, 486)

def capture_window(x1, y1, x2, y2):
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2
    im = np.array(im.getdata(),dtype='uint8').reshape((im.size[1],im.size[0],3))
    return im

##def capture_window():
##    im = ImageGrab.grab()
##    im = np.array(im.getdata(),dtype='uint8').reshape((im.size[1],im.size[0],3))
##    return im

##
x_offset = 0
y_offset = 0
t1 = time.time()
count = 0


# performance test ~ 11fps
##while True:
##    t1 = time.time()
##    while True:
##        if (time.time() - t1) > 1.0:
##            print(count)
##            count = 0
##            break
##        rgb = capture_window(33 + x_offset, 206 + y_offset, 313 + x_offset, 484 + y_offset)
##        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
##        edges = cv2.Canny(gray, 10, 10)
##        count += 1


###########################################################################################

## ### color binds
bindings = {(237, 224, 200): 4, (238, 228, 218): 2, (242, 177, 121): 8, (205, 193, 180): 0, (245, 149, 99): 16, (246, 124, 95): 32, (246, 94, 59): 64, (237, 207, 114): 128}
game_over = (237, 207, 115)

###########################################################################################



def crop_further(percent, image):
    try:
        image = Image.fromarray(image)
    finally:
        offset = int(image.height * (percent/100))
        return image.crop((0 + offset, 0 + offset, image.height - offset, image.width - offset))


rgb = capture_window(38 + x_offset, 210 + 3 + y_offset, 308 + x_offset, 481 + y_offset)
##gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
##edges = cv2.Canny(gray, 10, 10)
##cv2.imshow('window', edges)
##img = Image.fromarray(gray)
##img.show()

##crop_further(3, gray).show()

def output_grid(gridx, gridy, image):
    try:
        image = Image.fromarray(image)
    finally:
##      print('bounds:', 'height', image.height, 'width', image.width)
        grids = []
        i0 = 0
        for i1 in range(int(image.height/gridy), image.height + 10, int(image.height/gridy)):
            j0 = 0
            for j1 in range(int(image.width/gridx), image.width + 10, int(image.width/gridx)):
                grids.append(image.crop((i0, j0, i1, j1)))
##              print('cropped', i0, j0 , i1, j1)
                j0 = j1
            i0 = i1 
        return grids


def get_major_color(image):
    colors = image.getcolors()
    return tuple(max(colors)[1])


def get_num(image, xy):
    def new_bind(color, xy):
        input('tile %d is unrecognized, please create a new binding'%(xy + 1))
        num = int(input("New color bind! Enter number for tile #%d: " %(xy + 1)))
        global bindings
        bindings[tuple(color)] = num
        print('new color', color, 'binded to', num)
        print('waiting for 5 seconds')
        time.sleep(5)
    color = get_major_color(image)
    if color not in bindings:
        new_bind(color, xy)
        file = open('bindings.txt', 'a')
        file.write(str(bindings))
        file.write('\n')
        file.close()
    return bindings[color]



##grids = output_grid(4,4, crop_further(0, rgb))
##grids = [crop_further(3, grid) for grid in grids]
##print(get_major_color(grids[-1]))
##print(get_major_color(grids[-2]))
##




def capture():
    state = []
    t1 = time.time()
    im_rgb = capture_window(38 + x_offset, 210 + 3 + y_offset, 308 + x_offset, 481 + y_offset)
    grids = output_grid(4, 4, crop_further(0, im_rgb))
    grids = [crop_further(3, grid) for grid in grids]
    for grid in range(len(grids)):
        state.append(get_num(grids[grid], grid))
##    print('state update:', state)
    print('elapsed time', time.time() - t1)

    return state



def cnvt2grid(state):
    grid = [[0 for j in range(4)] for i in range(4)]
    k = 0 
    for j in range(4):
        for i in range(4):
            grid[i][j] = state[k]
            k += 1
    return grid


        
if __name__ == '__main__':

        # save to file
##        try:
##            file = open('bindings.txt', 'r')
##            bindings = json.loads(file.read())
##            file.close()
##        except:
##            file = open('bindings.txt', 'w')
##            file.write(json.dumps(bindings))
##            file.close()
        # MAIN LOOP
        while 1:
            
            state = []
            t1 = time.time()
            im_rgb = capture_window(38 + x_offset, 210 + 3 + y_offset, 308 + x_offset, 481 + y_offset)
            grids = output_grid(4, 4, crop_further(0, im_rgb))
            grids = [crop_further(3, grid) for grid in grids]
            for grid in range(len(grids)):
                 state.append(get_num(grids[grid], grid))
            print('state update:', state)
            print('elapsed time', time.time() - t1)
            
         
         
            
        














