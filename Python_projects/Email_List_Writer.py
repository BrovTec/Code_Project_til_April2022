
from string import Template #${KONTAKT_NAME}" gesehen? sogenannter Template-String 



#Collect Name and Email
def getContacts(file):
    names = []
    emails = []
    with open (file, mode='r', encoding='utf') as contactsFile:
        for a_contact in contactsFile:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

#Template-Objekt from txt file 
def readTemplate(file):
    with open(filename, 'r', encoding='utf-8') as templateFile:
        templateFileNachricht = templateFile.read()
    return Template(templateFileNachricht)