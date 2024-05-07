import cv2
vidcap = cv2.VideoCapture('/home/am_zam/inpainting_video/E2FGVI/results/_results.mp4')
success,image = vidcap.read()
count = 0
while success:
  if count < 10:
    cv2.imwrite("0000%d.jpg" % count, image)     # save frame as JPEG file
  elif count < 100:
    cv2.imwrite("000%d.jpg" % count, image)     # save frame as JPEG file
  elif count < 1000:
    cv2.imwrite("00%d.jpg" % count, image)     # save frame as JPEG file
  elif count < 10000:
    cv2.imwrite("0%d.jpg" % count, image)     # save frame as JPEG file
  else:
    cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
