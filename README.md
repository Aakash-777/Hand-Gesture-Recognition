# Hand-Gesture-Recognition

Used Google's mediapipe library to detect human hands and generate landmarks on them , used the opencv library from python to mark those landmarks and use them suitably.

# Working
Basically it works like this:
We fetch all the hand landmark values (indexes) and its current coordinates in our video frame and from there we apply conditions on those coordinate values to detect different hand gestures

For example when we show the "call me hand gesture"  our thumb tip index is at the top followed by the index , middle , ring(folded ) and the pinky finger at the bottommost, so we can get those x and y coordinate values to check wheather the fingers are in that position or not using their index values.

Then based on each hand gesture detected we can call a function which resembles the gesture , like we can define and call a function to voice call someone when the "call me" gesture is shown by th user

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fface-and-hand-landmarks-detection-using-python-mediapipe-opencv%2F&psig=AOvVaw1M_t2TygKzc14T9XXJdQNJ&ust=1712103453809000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLCK9cOgooUDFQAAAAAdAAAAABAJ

# Future Applications
1) We can also use the face landmarks or the full body landmarks to add differnt functionalities to our codebase
2) It can not only be used in devices like smartphones to detect gesture to do something but can also be used for helping the physically challenged people
3) It can also be used in camera drones to reconize different hand gestures to perform multiple tasks , like when we show a thumbs up , it will take a photo of us during its flight , also it will keep gracking us based on our full body movement , like that.
