# slack_grader

This is a simple Python tool intended for educators who would like to move
to having asynchronous communication with students via a slack channel and 
want to be able to print a report showing basic participation levels, including
names, total commments, and comment contents. The report is saved as text file.

To use this tool, you must be an admin of the slack channel you want to use it
with, and you must have Python 3 installed on your computer (don't worry! That
part is super easy!)

This tool requires Python 3 to be installed on your computer.
It should function equally well on all OS that run Python 3.

SETUP:
If you're using the free version of Slack, you can ONLY export from public 
channels.

To export from slack:

1. Click on the workspace name at the top left corner of the screen, then 
select "Administration" from the menu, followed by "Workspace settings."

2. Hit the "Import/Export Data" tab and then select "Export."

3. Make sure to select the amount of time you want to measure, e.g., 
30 days, exact date, etc.

4. The data will be saved as a .zip file. Unzip the file and move the .json file 
from the channel you want to measure into the 'files_to_grade' folder. Move the
users.json file into the 'user_file' folder. I recommend renaming these something
easy to recall and type in, e.g., 'Month1.json' or 'User1.json'.

5. Note: The free version of slack only saves the last 10,000 messages, so if 
the channel is used often, you may want to run the report sooner!

RUN: 

Run the 'slack_grader.py' file, either from command line, double-clicking, etc.
(Again, this won't work if you don't have Python 3 installed.) Follow the
prompts. The program will create a file with the information you indicate in the 
'reports' folder. Each report is named with a unique filename based on the time
the report is run (year-month-date-hour-minute-second).txt, which makes it 
unlikely running a new report would accidentally overwrite the previous report.

