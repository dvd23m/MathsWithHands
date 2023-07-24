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

  

The file vcCalc contains the processes to calculate the operations and show the final result. There are three functions:  
- calculate: This function calculates the operation received per parameter.
- show_text: This function shows the texts about instructions, numbers, operations and result.
- processHand: This does all the process to capture images, keys pressed, and others.

To solve any operation, you must use the following keys:
- s: sum
- r: substract
- m: multiplication
- d: division
- c: clear operations
- esc: exit

## Future improvements
In future I will want to create two applications:
- A rock, scissors, paper game
- Sign language aplication to transfrom sings to text

## Author
David Molina, estudiante de Ciencia de Datos 

