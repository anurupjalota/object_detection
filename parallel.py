

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")


def tini(img,num):
    #image load
    image = cv2.imread(img)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    #load image in model
    net.setInput(blob)
    detections = net.forward()

    #look for match in image
    for i in np.arange(0, detections.shape[2]):
        
        #extract confidence from detected object
        confidence = detections[0, 0, i, 2]

        #filter out low confidence objects
        if confidence > min_confidence:
            
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            
            (startX, startY, endX, endY) = box.astype("int")

            # display the prediction
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
#             print("[INFO] {}".format(label))
            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
    
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # show the output image
    cv2.imwrite("./output/{}_output.jpg".format(num), image)


def parallel(k):
  if(k==1):
    for i in range(0,250):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==2):
    for i in range(250,500):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==3):
    for i in range(500,750):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==4):
    for i in range(750,1000):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==5):
    for i in range(1000,1250):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==6):
    for i in range(1250,1500):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==7):
    for i in range(1500,1750):
      tini("./images/image_{}.jpg".format(i),i)
  if(k==8):
    for i in range(1750,2000):
      tini("./images/image_{}.jpg".format(i),i)


pool = multiprocessing.Pool(processes=8)
result = pool.map(parallel, [1,2,3,4,5,6,7,8])