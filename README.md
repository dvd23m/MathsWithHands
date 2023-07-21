# MathsWithHands

README UNDER CONSTRUCTION!!


## Description
This is my first computer vision project. With it we can do simple math operations such as addition, subtraction, multiplications and divisions by counting fingers showing to webcam.

## Solution
For do this proyect I use Python with the Mediapipe libary.  

At first I've created a file handsProcessing.py that contains "Mano" class with the necessary methods have been programmed. These methods are:  
-  getHand: Detect the postion of the hand.  
-  getWhatHand: This method gets if is left or right hand.  
-  coordHands: This method gets the coordinates of 21 points of the hand.
-  vectorOfFingers: With this method we can get a vector like this [0, 1, 1, 0. 0] that contains ones or zeros. One if finger is stretched, zero in otherwise. 

The file vcCalc contains the processes to calculate the operations and show the final result.

## Future improvements


## Author
David Molina, estudiante de Ciencia de Datos 

