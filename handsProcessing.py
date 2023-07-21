# Import libraries
import cv2
import mediapipe as mp

# Create class
class Mano:
    def __init__(self, mode=False, maxHands = 1,  model_complexity=1, confDetection = 0.5, confSegui = 0.5):
        # Attributes
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.confDetection = confDetection
        self.confSegui = confSegui

        # Objects from hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.maxHands, self.model_complexity, self.confDetection, self.confSegui)
        self.drawHands = mp.solutions.drawing_utils
        # Marks of fingers
        self.fingerPoints = [(8, 6), (12, 10), (16, 14), (20, 18)]
        self.fingerThumb = (4, 2)

    # Methods
    def getHand(self, frame, draw = False):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frame_rgb)
        self.fingerMarks = self.results.multi_hand_landmarks
        self.fingerData = self.results.multi_handedness

        if self.fingerMarks:
            for m in self.fingerMarks:
                if draw:
                    self.drawHands.draw_landmarks(frame, m, self.mp_hands.HAND_CONNECTIONS)
        return frame
    
    def getWhatHand(self):
        whatHand = None
        if self.fingerData:
            for i in self.fingerData:
                whatHand = i.classification[0].label
        return whatHand
        
    def coordHands(self, frame):
        fingerCoordList = []
        if self.fingerMarks:
            for mark in self.fingerMarks:
                for lm in mark.landmark:
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    fingerCoordList.append((cx, cy))
        return fingerCoordList

    def vectorOfFingers(self, handPosition, wHand):
        fingers = []
        if handPosition:
            # All fingers excluding the thumb finger
            for f in self.fingerPoints:
                if handPosition[f[0]][1] < handPosition[f[1]][1]:
                    fingers.append(1)
                else: 
                    fingers.append(0)
            
            # Check whether hand is left or right to count the thumb finger
            match wHand:
                case "Right":
                    if handPosition[self.fingerThumb[0]][0] < handPosition[self.fingerThumb[1]][0]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                case "Left":
                    if handPosition[self.fingerThumb[0]][0] > handPosition[self.fingerThumb[1]][0]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
            return fingers
