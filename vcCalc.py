import handsProcessing as hp
import cv2


def processHand():
    operation = None
    digit1, digit2 = 0, 0
    res = -1
    # Create object of class Mano
    detectedHand = hp.Mano()

    while True:
        ret, frame = cap.read()
        # Mirror efect
        frame = cv2.flip(frame, 1)
        # Get hand
        frame = detectedHand.getHand(frame, draw=True)
        # Get vector of fingers and count ones
        handPosition = detectedHand.coordHands(frame) # Position of hands
        wHand = detectedHand.getWhatHand() # hand is using
        listOfFingers = detectedHand.vectorOfFingers(handPosition, wHand) # Getting vector
        
        # Create a rectangle to put the texts
        header = 'Press: [s] to sum [r] to subtract [d] to divide [m] to multiply'
        _, w, _ = frame.shape
        cv2.rectangle(frame, (0, 0), (w-1, 100), (0, 0, 0), cv2.FILLED)
        cv2.putText(frame, header, (0,20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 0))
       
        
        key =  cv2.waitKey(1) 
        # ESC to leave
        if key & 0xFF == 27:
            break
        
        if listOfFingers:
            totalFingers = listOfFingers.count(1)
            cv2.putText(frame, f"Choose the number: {totalFingers}",  (130,50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0))

        match key:
            case 83 | 115:
                operation, digit1 = '+', totalFingers
            case 82 | 114:
                operation, digit1 = '-', totalFingers
            case 68 | 100:
                operation, digit1 = '/', totalFingers
            case 77 | 109:
                operation, digit1 = 'x', totalFingers

        if operation:
            cv2.putText(frame, f"{digit1} {operation}", (190, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
        
        if key == 32:
            digit2 = totalFingers
            res = 1
        
        if res == 1:
            match operation:
                case '+':
                    r = digit1 + digit2
                case '-':
                    r = digit1 - digit2
                case 'x':
                    r = digit1 * digit2
                case '/':
                    try:
                        r = digit1 / digit2
                    except ZeroDivisionError:
                        r = "[ERROR]"
            cv2.putText(frame, f"{digit2} =", (270, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
            cv2.putText(frame, f"{r}", (350, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))

        cv2.imshow("Hands", frame)
 
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    cap = cv2.VideoCapture(0)

    # Check if camera is working
    if not cap.isOpened():
        print("[ERROR] The camera doesn't work")
    else:
        processHand()