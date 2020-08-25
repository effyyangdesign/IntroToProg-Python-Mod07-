# Assignment 07 Step Documentation

**Dev:** *Yizhou Yang*   **Date:** *08.25.2020*


**Introduction**
This essay documents the steps I took to finish Assignment 07 to practice pickling and exception handling. 

**Steps:**
I decided to make a program to take appointments and save to disk as a binary file, then also read it back to display the existing appointment. 

I used lab7-01 completed in the lecture as my model for pickling and unpickling between memory and file. Then, I decided to incorporate exception handling in the process of getting user input about the appointment they want to make.

#### image 1
![image 1](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/image1.png "image 1")

Then I realized that this is numeric function does not work too well to determine whether the date input is in the correct format. I tried couple attempts, including testing whether the dateInput is integer or string. Upon realizing dateInput would always comes in as a string. I decided to take another approach and raise a custom error.  I decided if anyone inputs more than 4 digits, then it will prompt an exception.  

#### image 2
![image 2](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/Image2.png "image 2")

After that I encountered the first question with pickling. I realized that because dump and load are all loading/writing one line. From reading “Reading Data from a File and Unpickling It” in Chapter 7 of the text book, I can only see unpickling line by line. However this is not too helpful as I would not know how many lines already exists in the appointment document. 

#### image 3
![image 3](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/Image3.png "image 3")


As I am researching how to unpickle multiple lines,  I saw this EOFError method on stackoverflow (https://stackoverflow.com/questions/20716812/saving-and-loading-multiple-objects-in-pickle-file). It is very similar to my thought of keep looping this pickle.dump, which lead to me out of “Ran out of input” error. Now this error can serve as an terminator to stop the loop. 

#### image 4
![image 4](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/Image4.png "image 4")

Upon this Exception, I found multiple exception idea, including “FileNotExistError” which would very likely occur if user wants to view existing appointment but yet no appointment file exist. However by introducing try/except at the opening stage of this function, objFile initiation becomes an error as well. Therefore, I decided to put in a generic Exception just to catch all possible issue.

#### image 5
![image 5](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/Image5.png "image 5")

I also tried to add another function to delete existing appointment. However I ran into lots of issue because my binary file is in the format of one long list. That is because I just dump the list into the binary file using “pickle.dump”. However when attempting to retrieve it from pickled file, it has proven to be more complicated than regular file. I referenced this method (https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/) to get into the list, then into the dictionary to compare the key. Yet somehow that was not successful. I decided to leave this function out for this Assignment but I would love to discuss and see how my classmates handle such issue. 


#### image 6
![image 6](https://github.com/effyyangdesign/IntroToProg-Python-Mod07-/blob/master/docs/Image5.png "image 6")
