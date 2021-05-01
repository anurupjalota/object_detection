import os
import cv2

# Video Generating function
def generate_video():
    video_name = 'test_output/mygeneratedvideo6.mp4'
    images = ["./frames/frame{}.jpg".format(i) for i in range(len(os.listdir('./frames')))]

    # print(len(images))
    # print(type(images[0]))
    # print(images[0])

    frame = cv2.imread(images[0])

    # setting the frame width, height width
    # the width, height of first image
    height, width = frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video = cv2.VideoWriter(video_name, fourcc, 25, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(image))
    
    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release() # releasing the video generated


# Calling the generate_video function
generate_video()
