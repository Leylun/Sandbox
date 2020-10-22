# CP1404 Assignment 2: Travel Tracker 2.0 by Tristan Harrington

## 1. How long did the entire project (assignment 2) take you?
The total time taken to complete the Travel_Tracker_2 task was between 8-10 hours. This time was distributed to tasks in this manner:
  - Class_Creation (1.5-2 hours) __(Updated)__
  - Class_Testing (0.5 hours)
  - Kivy_Creation (2-2.5 hours) __(Updated)__
  - Travel_Tracker_2 Creation (1-1.5 hours)
  - Travel_Tracker_2 Testing and Error Checking (3-3.5 hours)

It can be easily observed that Testing and Error Checking took a large amount of time to complete, this can be due to the large number of minor changes that were made into the 
task; such as simple print statements. This is supplied further evidence due to the comparatively miniscule time to test and error check multiple classes.

## 2. What are you most satisfied with?
During the development stage of this app, it was discovered that a large number of code from the original Travel_Tracker could be reused and repurposed. This allowed for time to be focused in other directions of development. Thus streamlining the process of creating large components such as saving/loading data and sorting lists of class objects.

It is also noted that the __getitem__ function proved increasingly useful for calling attributes from the place class into the child placeCollection class. This allowed the code to directly call attributes like the visited/priority value and define them directly, which was critical in the sorting method found within the placeCollection class.   

## 3. What are you least satisfied with?
During the coding stage, it was exceptionally aggrivating to use __Github__ as it became difficult to commit and push data to the correct locations. This problem eventually spiraled and caused a major data loss, to both the kivy_GUI/Installation and class codes. Whilst rewriting the code proved far easier in the next iteration, (shown with the updated status) it was still a major problem that could not be solved due to the issue of recursive data loss.

## 4. What worked well in your development process?
Whilst creating the initial backbone for the code, it was extremely simple to utilize the kivy language. Creating __Spinners__ and __BoxLayouts__ proved to be simplistic in nature but offered a variety of choices and adjustments further helping initial development. Whilst it was assumed that this major part would prove difficult due to a lack of similarity, it was surprisingly easy to navigate and research if needed.

## 5. What about your process could be improved the next time you do a project like this?
The most vital part of code in this project that could be improved would certainly entail the sorting algorithm. The current sorting algorithm whilst crude, was the most efficient that could be hypothesised; this was due to the inherent restrictions of trying to incorporate 4 different sorts into a singular method. If given more time, it would most definitely be more efficient to redesign this method with audience readability in mind.

## 6. Describe what learning resources you used and how you used them.
A major resource that was used during the development process was the demos given for kivy, examples include; __spinner_demo.py/.kv__ and __dynamic_widgets.py/.kv__ these proved highly helpful in creating the project. Originally a dropdown was attempted for the sorting methods, however after trying multiple times and not succeeding, it was replaced by the superior __spinner:__ layout. Using the demos it was simple to repurpose the spinner to the standards required for the project.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
Whilst trying to create the place_object_buttons to standards required for the project, it was proving exceedingly hard to bind the button to an on_press event; and when it would seem to function, each button would produce the last place_object output. Several different methods to rewrite the code were utilized and simply failed, these ranged from trying to define all buttons with a list, to simply hard coding the buttons to produce these outputs. With a bit of research it was discovered that using __lambda__ within the .bind function would seperate the buttons from each other. Allowing the correct outputs to be produced. __Example:__ example_but.bind(on_press=lambda example_but: method(input))

Another exceedingly annoying issue was discovered whilst trying to call an object's attributes while in another class. To tackle this problem during the first iteration, a function was created within the initial class to simply return all attributes. This allowed for recorded values to be retrieved, regardless this method became ineffective when the requirement to write data back into the class arose. This was eventually solved with the previously stated __getitem__ function which tackled both of these issues simultaneously, directly connecting the class's attribute when called. 

## 8. Briefly describe your experience using classes and if/how they improved your code.
As the previously mentioned challenge was solved, classes became greatly helpful in directly improving readability and efficiency of the code. Allowing for variables to be stored directly in their attributes instead of a list or other variable_type; this alongside object orientated coding, created an efficient system for retrieving and storing data. Classes showed their inherent usefulness once more within the coding stage, allowing for functions that directly operated on the object's attributes; creating a simple system to do repeatable tasks without the direct need to call the attributes themselves.
