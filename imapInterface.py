import email
import imaplib
from datetime import datetime


class IMAPInterface:

    def __init__(self, username, password, imapURL):
        self.mail = imaplib.IMAP4_SSL(imapURL)
        self.mail.login(username, password)

    def fetchAllEmails(self):
        if not self.mail:
            raise ValueError("Not connected to the mail server. Call 'connect()' first.")

        self.mail.select("inbox")
        result, data = self.mail.search(None, "ALL")
        if result == 'OK':
            emailIds = data[0].split()
            allEmails = []

            for emailId in emailIds:
                result, data = self.mail.fetch(emailId, "(RFC822)")
                if result == 'OK':
                    allEmails.append(data[0][1])

            return allEmails
        else:
            print("Failed to fetch emails.")
            return []

    def fetchEmailForDeletion(self, deleteBeforeDate):

        self.mail.select("inbox")
        result, data = self.mail.uid('search', None, f'(BEFORE "{deleteBeforeDate}")')
        deletedEmails = []

        if result == 'OK':
            emailIdList = data[0].split()
            for num in emailIdList:
                result, emailData = self.mail.uid('fetch', num, '(BODY.PEEK[HEADER])')
                if result == 'OK':
                    if emailData[0] is not None and emailData[0][1] is not None:
                        rawEmail = emailData[0][1].decode("utf-8", errors='ignore')
                        emailMessage = email.message_from_string(rawEmail)
                        dataTuple = email.utils.parsedate_tz(emailMessage['Date'])

                        if dataTuple:
                            localDate = datetime.fromtimestamp(email.utils.mktime_tz(dataTuple))
                            subject = emailMessage['Subject']
                            senderName, senderEmail = email.utils.parseaddr(emailMessage['From'])

                            deletedEmails.append({
                                'Date': localDate,
                                'Sender Name': senderName,
                                'Sender Email': senderEmail,
                                'Subject': subject,
                                'UID': num
                            })
                    else:
                        print("No email data for UID ", num)

        return deletedEmails

    def deleteMarkedEmails(self, deleteBeforeDate):
        markedEmails = self.fetchEmailForDeletion(deleteBeforeDate)
        successfullyDeleted = 0
        errors = []

        for mail in markedEmails:
            try:
                self.mail.uid('store', mail['UID'], '+FLAGS', '\\Deleted')
                successfullyDeleted += 1
            except Exception as e:
                errors.append(f"Error deleting email with UID {mail['UID']}: {str(e)}")
        try:
            self.mail.expunge()
            return successfullyDeleted, errors
        except Exception as e:
            return 0, [f"Error occurred during expunge: {str(e)}"]

    def listAllMailboxes(self):
        return self.mail.list()

    def closeConnection(self):
        self.mail.close()
        self.mail.logout()
