# Thoughtworks test

############################################################

Explanation of the chosen application design

0) General thoughts
   The 3 problems have a really similar folder structure. I have decided to put each object
   class in a separate folder. Although in these problems there are no examples of inheritance
   that make the folder useful to group them, I am used to do it that way. It also helps to
   easily see which files contain the main methods. Some methods for a cleaner code are used
   in the 3 problems (process_input, clean_screen); I could have put them in the same file in
   the project folder, but as those are small and simple methods, I decided to leave them in
   each of the problems. I haven't used much Exception handling, as the problems didn't really
   need them, and it wasn't needed for the tests either.

1) Trains Application
   To have an application that worked simply, while being useful for testing, I decided to
   make it interactive. The user can specify which mode does he want, and the parameters for
   that mode. Tests on the input from the user are made, and an output is given to be more
   'user friendly'. I have decided to also accept lower letters to define paths and strips, as
   all stations are in capital letters, so there's no possible doubt about that.

2) Conference Track Management
   At the beginning I didn't have much clear how to solve the assignation problem. I tried to
   simply order from longer to shorter and assign them, but that obviously didn't work; some
   talks didn't have enough space in the end to be assigned (just a 15 minute period was free).
   Finally, apart from ordering them, I assigned them, always making sure that there were at
   least 30 mins left in case the time didn't match with the total.

3) Merchant's Guide to the Galaxy
   For this problem I had to make some assumptions about how the statements in the input were
   shaped. I divided them in 4 types:
   X is Y
   x1 .. xn coin is val Credits
   how much is x1 .. xn ?
   how many Credits is x1 .. xn coin ?
   Any statement that doesn't follow this logic won't be processed. Also I noticed the first
   time I thought the problem was solved that the value of coins could be floats, so I had
   to modify the application accordingly (didn't take more than 2 mins). 

############################################################

   A general view of the folders structure can be seen in:  
       ProjectFolder.png                                    

############################################################

To run the applications, type from the main folder:

1) Trains Application
       python TrainsPythonGA/src/TrainApp.py $optional_input_path

2) Conference Track Management
       python ConferencetrackmanagementPythonGA/src/SchedulerApp.py $optional_input_path

3) Merchant's Guide to the Galaxy
       python MerchantsguidetothegalaxyPythonGA/src/CoinValueQuestionsParser.py $optional_input_path

############################################################

As requested, several tests have been added.
In order to run them, execute them from the main folder. Paths to each of the tests files can be
found in the file:

       tests_runner.txt

I had already made a script that run all tests, but as no executables can be send I had to delete it.
