# data-analyst-job-search-assistant
Ironhack Bootcamp Final Project

## ABOUT THE PROJECT
This project is written in python. The goal/purpose is to give user a job recommendation based on the personal skills/preferences that the user needs to give in the user interface. There are two versions here:
 - If you open the _notebook_ file (STEP 1, STEP 2, STEP 3), you will find a simple graphical user interface (GUI) when you run the main file (STEP 3)
 - If you open the _python_ file instead (main.py), you will go directly to the streamlit window on a webpage. There you will find a different experience in running a python code. 
 <br>If you run the main.py file, you will be asked to either mark the checkboxes with clicks, or upload your CV in pdf format. You will find detailed info on how to run through the code below.
 <br>The final output will be a recommended job for you, that has similar specification to the skillsets you put in.

## HOW TO RUN
 #### Streamlit
 - Open your terminal (iterm, git bash, cmd, etc.) and navigate to the folder.
 - Type "_streamlit run main.py_" without quotation marks.
 - It will open the page in your browser. Follow the instructions.
 - In the input section, you will need to pick either you fill in your skillsets manually or you upload your CV (pdf). If you do manual skillset, and then upload your CV, the previous skillset will be overwritten. And vice versa.
 - Please run the sections in the given order (1, 2, 3). You can try to go directly to number 3, but it might not work, because it requires your input before making a recommendation for you. The recommendation is personally tailored for the user, after all :)
 - If you choose to upload your CV, please put your pdf file inside the folder.

 #### jupyter notebook
 - The file _STEP 1_ is the scraping part; you need to run this through if you want to run the _STEP 2_ file.
 - BEWARE: _STEP 1_ file has some script that runs for a few hours, and by a few hours I mean almost a whole day.
 - It is advised to open the _STEP 1_ and _STEP 2_ only to look at the code and check how I did the scraping.
 - The main file, _STEP 3_ runs unrelated to the other notebook files, and it does the main functions (input and output), don't worry about running the whole notebook there.
 - The file _STEP 1_ might still have some errors. I didn't try to run it as a whole yet because it takes toooo much time. It should work, but I don't guarantee. I might change some parts of it in the future to improve running time.

## INSTALLATION
There are some things that might need to be installed if you want to run the codes.
 - pip install selenium (for STEP 1)
 - pip install streamlit (for main.py)
 - pip install tqdm (for all of them)
 - I forgot the rest. If the code throws an error: _there is no module called xxx_, then please do "_pip install xxx_"

## LIBRARIES
Some of the libraries being used here are _pandas, matplotlib, seaborn, beautifulsoup, selenium, plotly, easyGUI, streamlit, sklearn, etc_

## SPECIAL THANKS
This project is my final project of the Data Analytics Bootcamp in Ironhack. I would like to give my special thanks to the Teachers, Jan Molendijk, Erin Berardi, and Simão Lopes, for teaching me and other students with patience through the 9-weeks of full-time lecture-practice-homework-overtime-work sessions. And also for the whole class that helped in gathering the data (the scraping job was split into 17 parts and was done by 17 people excluding myself). And Also for my wife that has been patient in giving me time to code during the bootcamp <3 She won't read this ofc, but I'll write it anyways. Loveyou.