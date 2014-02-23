import logging

try:
    from faker import Factory
except ImportError:
    logging.error('faker is not installed on the python packages..')

faker = Factory.create()



def simple_registration(rows):
    '''Represents the simple registration holding database
    just columns of email & passwords
    this method will fill the target database with fake emails and passwords
    Note: passwords will be created as md5 hashes
    Note 2 : rows parameter will be an integer
    '''
    list_of_emails = []
    list_of_passwords = []

    for n in range(0,rows):
        list_of_emails.append(faker.safe_email())
        list_of_passwords.append(faker.md5(raw_output=False))

    logging.info(list_of_emails)
    logging.info(list_of_passwords)

    return {emails: list_of_emails, passwords: list_of_passwords}
