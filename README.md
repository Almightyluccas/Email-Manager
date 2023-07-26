# Email Manager

Welcome to the Email Manager application! This Python-based application allows you to interact with your IMAP server, fetch emails, and 
delete the ones that are no longer needed. 

The current release is focused on providing basic functionality and setting a strong foundation for further expansion. 
I am excited about the opportunity to bring more features to this project as this is something I will be using myself.

## Features

- Fetch all emails from the IMAP server.
- Mark emails for deletion based on their date.
- Delete marked emails.
- Display a list of all the mailboxes.

## Installation

Make sure Python 3.x is installed on your system. You can download it [here](https://www.python.org/downloads/).

1. Clone the repository:
``` shell script
git clone https://github.com/Almightyluccas/Email-Manager.git
```
2. Change directory into the project:
```shell script
cd Email-Manager
```
3. Install the required libraries:
```shell script
pip install -r requirements.txt
```
**Note:** You may want to use a virtual environment to install the packages and run the program.

## Usage

You can use the Email Manager in two ways - through the command line interface (CLI) or the graphical user interface (GUI) which is currently not available.

Run the program with command-line arguments in the following format:

```shell script
python emailManager.py [date] [email] [password] [provider]
```
- `date`: Date before which all emails are marked for deletion.
- `email`: Your email address.
- `password`: Your email password.
- `provider`: Your email provider (currently supported: gmail, outlook, yahoo, aol).

### Graphical User Interface

You can also use the GUI version by running the `emailManager.py` script without any arguments:

```shell script
python emailManager.py
```
or
```shell script
python emailManager.py GUI
```
Follow the prompts in the GUI to manage your emails.

## Note

- **Please be careful**: Emails marked for deletion will be permanently deleted. Make sure you have made the right selection before confirming the deletion.
- If you encounter an error running the script with `python`, try using `python3` instead:
```shell script
python3 emailManager.py
```
instead of

```shell script
python emailManager.py
```








