# import the opencv library
import cv2

# import the reading text from image library
import pytesseract

# set defaulet settings
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# define a video capture object
vid = cv2.VideoCapture(0)

special_time_frame_counter = 0

while (True):

    # Capture the video frame
    # by frame
    check, frame = vid.read()

    flipped = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('c'):
        print("...")
        # reading text from frame
        catched_text = pytesseract.image_to_string(frame, lang='rus')
        # catched_text = pytesseract.image_to_string(frame)

        print(catched_text, end='\r')

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()