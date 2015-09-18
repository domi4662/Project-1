# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# Filename: project1.py
#
# Abstract: This Program will read some images (for this project nine images), and it will
# calculate the median of the each pixels of these images to obtain a new image that contains the median
# of each pixel calculated before. 
# 
# Author: Carlos Eduardo Domingues dos Santos
# Date: 09/15/2015
#
# '/Users/ceds1705/Downloads/Project1Images/'
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
    

def getImages():
   folder = raw_input("Type the directory of the images: ")
   pictures = [] # Array of pictures 
   counter = 0
   try:
       for counter in range(0, 9): # Getting Images
           imagePath = folder + str(counter + 1) + '.png'
           pictures.append(makePicture(imagePath)) # Inserting images in the array
   except:
       print "Problem encountered to load images. Please the check directory."
       return pictures
   return pictures
   
def createNewImage(imgs):
    try:
        print "Processing new image..."
        height = getHeight(imgs[0]) # Get the height of first image
        width = getWidth(imgs[0]) # Get the width of first image
        newPic = makeEmptyPicture(width, height) # Creating an empty picture
        imgs.append(newPic)
        for x in range(0, width):
            for y in range(0, height):
                rColor = [] # Array to store red pixels of the images
                gColor = [] # Array to store green pixels of the images
                bColor = [] # Array to store blue pixels of the images
                for i in range(0, 10):
                    pixel = getPixel(imgs[i], x, y) # Get pixels of the images
                    rColor.append(getRed(pixel)) # Get red color of the pixel  
                    gColor.append(getGreen(pixel)) # Get green color of the pixel
                    bColor.append(getBlue(pixel)) # Get blue color of the pixel
                newColor = makeColor(findMedian(rColor), findMedian(gColor), findMedian(bColor)) # Create new color of the pixel which the median
                setColor(pixel, newColor) # Set this color to this pixel in the new image
        folder = raw_input("Type the directory where you want to save the image: ")
        repaint(imgs[i]) # Reprint the image created
        writePictureTo(imgs[i], folder + str(i+1) + '.png') # Save the image in this directory
        return true
    except:
        print "Images not found."
        return false
            
def findMedian(color):
    color.sort() # Sort an array of colors
    if(len(color) % 2 != 0): # Median for an odd set
        median = (color[len(color)/2]) 
    else:  # Median for an even set
        median = (color[len(color)/2] + color[len(color)/2 - 1])/2 
    return median
    
def main():
    image_created = false 
    imgs = [] # Array of images
    imgs = getImages() # Get images and stores in the array
    image_created = createNewImage(imgs)  
    if(image_created == true):
        print "Image created successful!!"
    else:
        print "Failed to create new Image."
    return 0

init_program = main() # Initialize program
