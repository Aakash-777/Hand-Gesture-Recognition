# Hand-Gesture-Recognition

Used Google's mediapipe library to detect human hands and generate landmarks on them , used the opencv library from python to mark those landmarks and use them suitably.

# Working
Basically it works like this:
We fetch all the hand landmark values (indexes) and its current coordinates in our video frame and from there we apply conditions on those coordinate values to detect different hand gestures

For example when we show the "call me hand gesture"  our thumb tip index is at the top followed by the index, middle, ring (all three folded) and the little finger at the bottommost, so we can get those x and y coordinate values to check whether the fingers are in that position or not using their index values.

Then based on each hand gesture detected we can call a function which resembles the gesture, like we can define and call a function to voice call someone when the "call me" gesture is shown by the user

![HandLandmarks](https://github.com/Aakash-777/Hand-Gesture-Recognition/assets/108759537/2af50c10-1c3b-4947-b8c7-5680fc283ec0)

![image](https://github.com/Aakash-777/Hand-Gesture-Recognition/assets/108759537/f4e23555-197c-440c-93ca-b86d9cf0b58d)
X and Y coordinate values of every landmark indexes in each frame

![image](https://github.com/Aakash-777/Hand-Gesture-Recognition/assets/108759537/89a350b9-7825-494a-b927-e8ab33877ad7)
In the above image as you can see my index and little finger are up so its 1 and the middle and ring are folded so its 0.

![image](https://github.com/Aakash-777/Hand-Gesture-Recognition/assets/108759537/0180272b-ea26-42e3-9f7b-e54b66459871)
Called a specific function to a specific gesture

# Future Applications
1) We can also use the face landmarks or the full body landmarks from the library itself to add different functionalities to our codebase.
2) It can be used in various devices like smartphones to elevate hands free use or for the needs of physically challenged users.
3) It can also be used in camera drones to recognize different hand gestures to perform multiple autonomous tasks, like when we show a thumbs up, it can take a photo of us during its flight, also it will keep tracking us based on our full body movements.
