The user manual is easy to get lost in, so here's my take on getting started.
## 1. Set up the environment
If you're running Windows: first change your .cgi files in the cgi-bin folder to .py files (literally slow double click and type over the file extension)
If you're using Python 3.13, run
```bash
pip install legacy-cgi
```
Otherwise run
```base
pip install cgi
pip install cgitb
```
You may have to screw around with it. My Python installation is FUBAR so I ended up having to copy the cgi.py and cgitb.py files from where they'd saved into the cgi-bin folder. 
## 2. Run the server
LMEDS can run locally or on the network. For now, we're going to use the local server.
Open the terminal. Navigate to LMEDS-main. Run lmeds_local_server.py. 
Alternately, open IDLE, open lmeds_local_server.py, and run it.
## 3. Run the program
Open a browser and visit http://127.0.0.1:8123/cgi-bin/lmeds_demo.py
Click through to get an idea of how the program works.
THEN read the user manual to see how to adapt it to your needs.
## Weirdnesses from other programs
Your .py (or .cgi) file in which the program actually lives goes in the cgi-bin folder, but all of its reference files go in a folder named after it in the tests folder.
The tests folder, speaking of which, means the LMEDS tests you're running and writing, not the tests used to make sure LMEDS works. 
You have to run the server file, not the file named after your experiment!
