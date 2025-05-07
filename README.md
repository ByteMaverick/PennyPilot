# Team 7 Project README

## Project Title
**PennyPilot**

## Group Members
- **Alex Luong**
- **Mohammed Ansari**

## Project Description
**PennyPilot** is a personal budgeting application designed to help users track and manage their finances with an intuitive and user-friendly GUI.

### Dependencies
- pandas
- transformers
- PyQt5
- pdfplumber
- matplotlib
- sqlalchemy
- torch

## Setup and Execution Instructions
1. Clone this repo with this command: "git clone https://github.com/ByteMaverick/PennyPilot.git"
2. In the project root directory, do "pip -r requirements.txt"
3. Open this project in PyCharm
4. Run View\main.py in PyCharm
5. If any dependencies are still missing, check imports at top of each .py file and install them with PyCharm
6. If there is an error about missing torch, do "pip3 install torch torchvision torchaudio"
7. When using the app, once prompted to open a CSV file after opening a profile, go to assets/ folder for example files to load.

## File Structure Overview
**View folder**
- assets\ - folder with sample CSV and PDF files to import into the application
- main.py - Entry point of applicaiton
- Other .py files - Create window of corresponding page (e.g. login, create account, etc.)

**controllers folder**
- AiTools.py - generate categories using transformers
- Other .py files - controller logic for corresponding part of application

**dao folder**
- .py files - DAO objects to manipulate database

**models folder**
- .py files - Model classes to create tables in database

**utils folder**
- __init__.py - recognize this folder as a package
- extractor.py - tools to extract month and keys

## Known Bugs or Limitations
None
