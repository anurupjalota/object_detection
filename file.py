import os
import time

start = time.time()
path = './images/'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'image_'+str(i)+'.jpg'))
    i = i +1
print(time.time() - start)