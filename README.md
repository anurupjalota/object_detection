# Object Detection using MultiProcessing 
In this Repo, we have experimented with images and video for object detection. 

## Image Detection on a dataset of 6000 images.
We used MobileNet_SSD model for detection.

### Serial Object Detection of Images
In this, a single function is executed to implement object detection.
**TOTAL_TIME: 18min 49s**

### Parallel Object Detection of Images using a single function 
In this, a single function is executed on multiple processors (6 to be precise) to implement object detection.
**TOTAL_TIME: 73.2ms** (wow, right?)

###Parallel Object Detection of Images using multiple functions
In this, two functions, one for preprocessing and one for detection was used. 
We tried many combinations but we got the best performance in the following configuration:

1 processor for preprocessing and 2 processors for detection
**TOTAL_TIME: 21.7 ms**

## Video Detection
How video detection is being done?
It follows the steps mentioned below:
a. first it splits the video into frames
b. the frames are preprocessed for detection
c. object detection is used on those processed frames
d. detected frames are then again stitched back to get the complete video back with objects detected.

### Serial Objection Detection of a video
In this, a single function is executed to implement object detection.
**TOTAL_TIME: 15min 3s**

### Parallel and partially Serial Objection Detection of a video
In this, 4 separate functions are executed, out of which 3 are executed parallelly and the last one(for stitching) is executed serially.
2 queues are used between the parallel processors for extracted frames.

The configuration was like this:
1 processor for extracting frames from video
2 processors for preprocessing of those frames
3 processors for detection of those frames
and then, video stitching serially.
**TOTAL_TIME: 1min 54s**

### Fully Parallel Objection Detection of a video
In this, 4 separate functions are executed parallelly and this time 3 queues are maintained between them.
1 processor for each function. 
This was better than the above configuration.
**TOTAL_TIME: 54.9ms**

## Now let us conclude the real power of HPC:
Compare the last time (54.9ms) with the serial time of video (15min 3s). As we can see the speed up is almost **16000 times**. Pretty crazy, right? 
