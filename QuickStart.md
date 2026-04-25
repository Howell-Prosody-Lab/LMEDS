The user manual is easy to get lost in, so here's my take on getting started.
## 1. Set up the environment
If you're running Windows: first change your .cgi files in the cgi-bin folder to .py files (literally slow double click and type over the file extension)
If you're using Python 3.13, run
```bash
pip install legacy-cgi
```
Otherwise run
```bash
pip install cgi
pip install cgitb
```
You may have to screw around with it. My Python installation is FUBAR so I ended up having to copy the cgi.py and cgitb.py files from where they'd saved into the cgi-bin folder. 
## 2. Run the server
LMEDS can run locally or on the network. For now, we're going to use the local server.
Open the terminal. Navigate to LMEDS-main. Run lmeds_local_server.py. 
Alternately, open IDLE, open lmeds_local_server.py, and run it. You may have to mess around with python3 and/or pip3.
## 3. Run the program
Open a browser and visit http://127.0.0.1:8123/cgi-bin/lmeds_demo.py (if you're on Windows).
(If you're on Mac or Linux, change the permission octal of lmeds_demo.cgi and experiment_runner.cgi to 777, and then visit http://127.0.0.1:8123/cgi-bin/lmeds_demo.cgi.)
Click through to get an idea of how the program works.
THEN read the user manual to see how to adapt it to your needs.
## Making your own experiment
The easiest way to make an experiment is to edit another experiment, and it's still not all that easy. Go into the tests folder and wholesale copy the lmeds_demo folder (or any of the others, but this one gives you the most flexibility. Rename the folder something new, let's say demo_copy.
### "Rename" the sequence file
Go into demo_copy and open sequence.txt. Change the first line to *Demo_Copy. Take a look at the rest of the code--you'll change this to fit your experiment. This is the file that actually controls what pages appear. We'll come back to this. Save.
### Rename output folder
Go into output and rename the folder there to Demo_Copy.
### Copy configuration file
Go all the way up to the LMEDS root level and into cgi-bin. Copy lmeds_demo.cgi and/or lmeds_demo.py (whatever is there) and rename the copies demo_copy cgi/demo_copy.py.
### Edit configuration file
Open the new file(s) you just made and change the first argument of runExperiment from lmeds_demo to demo_copy.
### Go wild
You can run it now the same as you did lmeds_demo except the URI you'll visit is http://127.0.0.1:8123/cgi-bin/demo_copy.py or http://127.0.0.1:8123/cgi-bin/demo_copy.cgi. Do run it; make sure you changed everything you needed to change. (Don't forget the permission octals if you're not on Windows.) Now you can begin editing the english.txt file (to change the wording) and the sequence.txt file (to change what pages appear and what sound/video files and transcripts appear). Consult the demo and the manual to see how to edit them to your needs. Drop new sound and video files into the audio_and_video folder and new transcripts into the txt folder. 
## Nested experiments
Sometimes you'll have different versions of the same experiment, such as a different order of pages or a different language. We'll call the main experiment My_Experiment and the specific versions experiment_a and experiment_b. Your renamings should work like so:
- The cgi-bin folder should have a file called experiment_a.cgi and experiment_b.cgi (or .py...we don't need to keep explaining this, right?)
- BOTH OF THOSE should have My_Experiment as the first argument to runExperiment. Edit the sequence file and dictionary file arguments as needed.
- The tests folder should contain a folder called My_Experiment.
- That folder should contain whatever dictionaries and sequence files you need to run experiment_a and experiment_b. If you have different sequence files for the two, then one should begin *experiment_a and the other *experiment_b.
- The output folder should have a folder named experiment_a and another named experiment_b. At least if you have multiple sequence files. I'm not sure what happens if you have multiple dictionaries but one sequence file.
- The URI you visit will be http://127.0.0.1:8123/cgi-bin/experiment_a.py etc.
## Weirdnesses from the perspective of a programmer
Your .py (or .cgi) file in which the program actually lives goes in the cgi-bin folder, but all of its reference files go in a folder named after it in the tests folder.
The tests folder, speaking of which, means the LMEDS tests you're running and writing, not the tests used to make sure LMEDS works. 
You have to run the server file, not the file named after your experiment!
