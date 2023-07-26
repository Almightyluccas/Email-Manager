import sys
from imapInterface import IMAPInterface
from consoleUI import ConsoleUI
import customtkinter


imapURLDict = {
    'gmail': 'imap.gmail.com',
    'outlook': 'imap-mail.outlook.com',
    'yahoo': 'imap.mail.yahoo.com',
    'aol': 'imap.aol.com'
}


# Terminal Arguments Use
if len(sys.argv) > 1 and sys.argv[1].upper() != 'GUI':
    if len(sys.argv) == 5:
        consoleUI = ConsoleUI()

        date = str(sys.argv[1].upper())
        emailInput = str(sys.argv[2])
        passwordInput = sys.argv[3]
        if sys.argv[4].lower() in imapURLDict:
            emailProvider = imapURLDict[sys.argv[4].lower()]
        else:
            consoleUI.displayProviderInputError()

        emailClient = IMAPInterface(emailInput, passwordInput, emailProvider)
        emailsMarkedDeletion = emailClient.fetchEmailBeforeDate(date)

        consoleUI.displayMarkedForDeletion(emailsMarkedDeletion)

        deleteConformation = consoleUI.requestConformationForDeletion()
        if deleteConformation == 'y':
            numDeleted, errors = emailClient.deleteMarkedEmails(date)

            if numDeleted > 0:
                consoleUI.displaySuccessMsgDeletingEmail(numDeleted)
            else:
                consoleUI.displayNoEmailToBeDeleted()

            if errors:
                consoleUI.displayErrorsDeletingEmail(errors)
        elif deleteConformation == 'n':
            consoleUI.displaySuccessMsgUnmarkingForDeletion()

        emailClient.closeConnection()
    else:
        print('Not enough arguments provided for terminal use. Exiting...')
        sys.exit(1)


# GUI use
elif (len(sys.argv) == 1) or (len(sys.argv) > 1 and sys.argv[1].upper() == 'GUI'):
    print('GUI Launching...')

else:
    print('Invalid command line arguments. Exiting...')
    sys.exit(1)
