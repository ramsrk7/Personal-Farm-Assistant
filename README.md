# PERSONAL FARM ASSISTANT

A chatbot created using RASA platform for managing multiple farms efficiently.

## Installation

1. Setup a Virtual Environment

```bash
python3 -m venv ./venv
```
2. Activate virtual environment.

```bash
source ./venv/bin/activate
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rasa.

```bash
pip3 install -U --user pip && pip3 install rasa
```

## Running

1. Change directory to the project folder.

```bash
cd RASA3
```
2. Activate Virtual Environment.

```bash
source ./venv/bin/activate
```
3. Open another terminal and follow step 1 and 2.

4. In the first terminal,

```bash
rasa train
```
5. In the second terminal, run

```bash
rasa run action
```
6. In the first terminal,

```bash
rasa shell
```

If unable to train, download the pretrained model and add the folder to the directory from following link - https://drive.google.com/drive/folders/1KUhAcC0-rmwnU9s2kD1vj6KMZLsozQpk?usp=sharing.  

## Sample Conversation:
**Your input ->**  Hi!                                                                     
**Bot ->** I'm your personal farm assistant. It's nice to see you how are you?   
**Your input ->**  Good.                                                                   
**Bot ->** That's wonderful.  
**Your input ->**  I need some information about middle                                    
**Bot ->** What do you want to know about middle?  
**Your input ->**  is there any new messages?                                              
**Bot ->** Checking...  
You have 1 unread message.  
**Your input ->**  read it                                                                 
**Bot ->** From supervisor at middle: We need to harvest soon.  on 13/11/21 10:00.   
**Your input ->**  whats the crop growth like?                                             
**Bot ->** Crop growth in middle farm is at stage 3.   
**Your input ->**  hows the temperature?                                                   
**Bot ->** The weather in middle farm is 4.37 degree celsius. 
**Bot ->** What else would you like to know about middle farm?  
**Your input ->**  Wind speed?                                                             
**Bot ->** The speed of wind is 7.58 km/hr. 
Would you like to know anything else about middle farm?  
**Your input ->**  Are the gates open?                                                     
**Bot ->** Gates are already opened.  
**Your input ->**  close it                                                                
**Bot ->** Closed gates.  
**Your input ->**  bye                                                                      
**Bot ->** Bye, have a nice day.   
