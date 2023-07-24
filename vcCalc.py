import handsProcessing as hp
import cv2

def calculate(digit1, digit2, operation):
    '''
    This function calculates the operation received per parameter

    params:
        digit1(int): The first num
        digit2(int): The second ones
        operation(string): The sign of operation to solve
    
    return: int or float (in division) with result of calculation
    '''
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
    return r

def show_text(frame, text, position=(0, 0), size=1, color=(0, 255, 0)):
    '''
        This function only shows the text

        params:
            - frame: The frame 
            - text(string): The text to show
            - positon: Tuple with x, y values
            - size(int): The size of text
            - color: Triplet with rgb 
    '''
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_PLAIN, size, color)


def processHand():
    # Init variables
    totalFingers = 0
    digit1, digit2 = 0, 0
    operation = None
    res = -1
    
    # Create object of class Mano
    detectedHand = hp.Mano()

    while True:
        # Capture cam image  
        ret, frame = cap.read()
        # Mirror efect
        frame = cv2.flip(frame, 1)
        # Get hand
        frame = detectedHand.getHand(frame, draw=True)
        
        # Get vector of fingers and count ones
        handPosition = detectedHand.coordHands(frame) # Position of hands
        wHand = detectedHand.getWhatHand() # hand is using
        listOfFingers = detectedHand.vectorOfFingers(handPosition, wHand)
        
        # Create a rectangle to put the texts
        header = 'Press: [s] to sum [r] to subtract [d] to divide [m] to multiply [c] to clean [esc] to exit'
        _, w, _ = frame.shape
        cv2.rectangle(frame, (0, 0), (w-1, 100), (0, 0, 0), cv2.FILLED)
        show_text(frame, header, (0, 20), size=0.85, color=(0, 255, 0))
        
        # Push key and check them        
        key = cv2.waitKey(1) 
        match key:
            case 83 | 115: # s
                operation, digit1 = '+', totalFingers
            case 82 | 114: # r
                operation, digit1 = '-', totalFingers
            case 68 | 100: # d
                operation, digit1 = '/', totalFingers
            case 77 | 109: # m
                operation, digit1 = 'x', totalFingers
            case 27: # Scape
                break
            case 32: # Space
                digit2 = totalFingers
                res = 1
            case 99: # C
                operation = None
                digit1, digit2 = 0, 0
                res = -1

        if listOfFingers := detectedHand.vectorOfFingers(handPosition, wHand):
            totalFingers = listOfFingers.count(1)
            show_text(frame, f"Choose the number: {totalFingers}",  (130,50), 1.5, (0, 255, 0))

        if operation:
            show_text(frame, f"{digit1} {operation}", (190, 90), size=2)
        
        # We have digit1 and digit2 then calculate the operation
        if digit2 and res == 1:
            result = calculate(digit1, digit2, operation)
            show_text(frame, f"{digit2} =", (270, 90), size=2)
            show_text(frame, f"{result}", (350, 90), size=2)
      
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


