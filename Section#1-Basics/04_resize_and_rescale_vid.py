import cv2 as cv

# Reading videos
video = cv.VideoCapture("Resources/Videos/dog.mp4")

def changeRes(width, height):
    # Only works for live video
    video.set(3, width)
    video.set(4, height)
    
# rescale function
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    frame_resized = rescaleFrame(frame, scale=.5)
    # cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break
video.release()
cv.destroyAllWindows()