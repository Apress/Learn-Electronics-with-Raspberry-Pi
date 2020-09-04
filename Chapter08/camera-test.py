import picamera

camera = picamera.PiCamera()

camera.capture('/home/pi/photo1.jpg')
camera.close()