class ConsoleUI:

    def requestConformationForDeletion(self):
        self.isNotUsed()
        result = input('Would you like to delete the marked emails? (y/n): ').lower()
        print()
        return result

    def displayMarkedForDeletion(self, emailsMarkedForDeletion):
        self.isNotUsed()
        print()
        print(65 * '*')
        print('The following emails have been successfully marked for deletion')
        print(65 * '*')
        print()
        for emailInfo in emailsMarkedForDeletion:
            print("Sender Name:", emailInfo['Sender Name'], "\tSender Email:", emailInfo['Sender Email'])
            print("Email Subject:", emailInfo['Subject'])
            print("Date:", emailInfo['Date'])
            print('\t\t************************************\t\t')
            print()
        print()

    def displaySuccessMsgUnmarkingForDeletion(self):
        self.isNotUsed()
        print(65 * '*')
        print('Your emails have been successfully unmarked for deletion')
        print(65 * '*')
        print('\n')

    def displaySuccessMsgDeletingEmail(self, numDeleted):
        self.isNotUsed()
        print(65 * '*')
        print(f'{numDeleted} marked {"emails" if numDeleted > 1 else "email"} have been successfully deleted!')
        print(65 * '*')
        print('\n')

    def displayNoEmailToBeDeleted(self):
        self.isNotUsed()
        print('No emails were deleted.')

    def displayErrorsDeletingEmail(self, errors):
        self.isNotUsed()
        print('\nErrors encountered during deletion:')
        for error in errors:
            print(error)

    def displayProviderInputError(self):
        self.isNotUsed()
        print('\n')
        print(120 * '*')
        print("There was an error with entered provider. "
              "Please enter an accepted email provider: 'gmail, outlook, yahoo, aol'")
        print(120 * '*')
        print('\n')

    def isNotUsed(self):
        pass
