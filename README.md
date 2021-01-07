# Machine Learning and Statistics

# **Project**

Task: to create a web service that uses machine learning to make predictions based on the data set powerproduction excel file. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. The web service should respond with predicted power values based on speed values sent as HTTP requests.


For more information please visit the Githib repository: 
https://github.com/JuliaMal/Machine_learning_project

The Github repository contains the following files:
   1. Project.ipynb - This is a Jupyter notebook that contains the main body of work (training the model using the data set), explanations, notes, references. etc.
   2. powerproduction.csv - This is the power production dataset used for analysis.
   3. ReadMe.md - This is a Markdown file, containing explanation what is saved in the Github repository and instructions how to run Jupyter notebook.
   4. .gitignore - This file tells git which files (or patterns) should be ignored. In our case it's Python.
   5. app.py - python script that runs a webservice
   6. templates - contains index.html file
   7. dockerfile - to build and run the we service in a container
   8. requirements.txt 

   #1 How to download this repository:

        1. Go to Github or click on the link provided earlier.
        2. Clich the "Clone or Download" button
        3. Choose between the options "Open in Desktop" or "Download ZIP"

   #2 How to run the code:

        1. The Jupyter Notebook software is included in the Python installation we obtained from Anaconda. 
        2. First you need to install Python from Anaconda.
        3. Then open a terminal window.
        4. Make sure that you're in the same directory as the saved in the repository, you have downloaded in step #1 (Type cd Path_to_the_folder, e.g. cd C:\User\GMIT\Assessment_tasks)
        5. Type jupyter notebook or jupyter lab to launch the Jupyter Notebook App.
        6. The notebook interface will appear in a new browser window or tab.
    
    #3 How to run the FLASK:
        1. in the command prompt type: set FLASK_APP=app.py
        2. python -m flask run