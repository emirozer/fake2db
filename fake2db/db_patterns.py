import logging

try:
    from faker import Factory
except ImportError:
    logging.error('faker is not installed on the python packages..')

faker = Factory.create()



def simple_registration(number_of_rows):
    '''Represents the simple registration holding database
    just columns of email & passwords
    this method will fill the target database with fake emails and passwords

    Note: passwords will be created as md5 hashes
    Note 2 : number_of_rows parameter will be an integer
    Note3: emails are safe
    '''
    list_of_emails = []
    list_of_passwords = []

    for n in range(0,number_of_rows):
        list_of_emails.append(faker.safe_email())
        list_of_passwords.append(faker.md5(raw_output=False))

    logging.info(list_of_emails)
    logging.info(list_of_passwords)

    fake_data = {'emails': list_of_emails,
                 'passwords': list_of_passwords}

    return fake_data

def detailed_registration(number_of_rows):
    '''Represents the detailed registration holding database
    Columns of the following information:
    name, lastname, address, phone, email, password

    Note: passwords will be created as md5 hashes
    Note2 : number_of_rows parameter will be an integer
    Note3: emails are safe

    '''
    list_of_names = []
    list_of_lastnames = []
    list_of_addresses = []
    list_of_phones = []
    list_of_emails = []
    list_of_passwords = []

    logging.info('Populating list objects with fake data..')

    for n in range(0,number_of_rows):
        list_of_names.append(faker.name())
        list_of_lastnames.append(faker.last_name())
        list_of_addresses.append(faker.address())
        list_of_phones.append(faker.phone_number())
        list_of_emails.append(faker.safe_email())
        list_of_passwords.append(faker.md5(raw_output=False))

    fake_data = {'names': list_of_names,
                 'lastnames': list_of_lastnames,
                 'addresses': list_of_lastnames,
                 'phones': list_of_phones,
                 'emails': list_of_emails,
                 'passwords': list_of_passwords}

    return fake_data
