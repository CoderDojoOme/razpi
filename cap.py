import picamera

img = picamera.PiCamera()
img.resolution = (800, 600)
img.rotation = 180
img.start_preview()
img.led = True
img.capture( "picture.jpg" )
