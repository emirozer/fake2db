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

    logging.info('[SIMPLE]Populating list objects with fake data..')

    for n in range(0,number_of_rows):
        list_of_emails.append(faker.safe_email())
        list_of_passwords.append(faker.md5(raw_output=False))

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

    logging.info('[DETAILED]Populating list objects with fake data..')

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

def user_agent(number_of_rows):
    '''Represents the user agent information holding db
    Columns of the following:
    ipv4, country_code, user_agent
    '''
    list_of_ips = []
    list_of_countrycodes = []
    list_of_useragents = []

    logging.info('Populating list objects with fake data..')

    for n in range(0, number_of_rows):
        list_of_ips.append(faker.ipv4())
        list_of_countrycodes.append(faker.country_code())
        list_of_useragents.append(faker.user_agent())

    fake_data = {'ips': list_of_ips,
                 'countrycodes': list_of_countrycodes,
                 'useragents': list_of_useragents
             }

    return fake_data

def company(number_of_rows):
    '''Represents the company information holding db
    Columns of the following:
    company name, start-up date, company email, domain name,city
    '''
    list_of_names = []
    list_of_sdates = []
    list_of_emails = []
    list_of_domains = []
    list_of_cities = []

    logging.info('[COMPANY]Populating list objects with fake data..')

    for n in range(0, number_of_rows):
        list_of_names.append(faker.company())
        list_of_sdates.append(faker.date(pattern="%d-%m-%Y"))
        list_of_emails.append(faker.company_email())
        list_of_domains.append(faker.safe_email())
        list_of_cities.append(faker.city())

    fake_data = {'names': list_of_names,
                 'sdates': list_of_sdates,
                 'emails': list_of_emails,
                 'domains': list_of_domains,
                 'cities': list_of_cities
             }

    return fake_data

def customer(number_of_rows):
    '''Represents the customer information holding db
    Columns of the following:
    name, last_name, address, country, city, registry_date,
    birthdate, email, phone_number, locale'''

    (list_of_names,list_of_lastnames,list_of_addresses) = ([],[],[])
    (list_of_countries, list_of_cities, list_of_registrydates) = ([],[],[])
    (list_of_birthdates, list_of_emails, list_of_phonenumbers) =([],[],[])
    list_of_locales = []

    logging.info('[CUSTOMER]Populating list objects with fake data..')

    for n in range(0, number_of_rows):
        list_of_names.append(faker.company())
        list_of_lastnames.append(faker.last_name())
        list_of_addresses.append(faker.address())
        list_of_countries.append(faker.country())
        list_of_cities.append(faker.city())
        list_of_registrydates.append(faker.date(pattern="%d-%m-%Y"))
        list_of_birthdates.append(faker.date(pattern="%d-%m-%Y"))
        list_of_emails.append(faker.safe_email())
        list_of_phonenumbers.append(faker.phone_number())
        list_of_locales.append(faker.locale())

    fake_data = {'names': list_of_names,
                 'lastnames': list_of_lastnames,
                 'addresses': list_of_addresses,
                 'countries': list_of_countries,
                 'cities': list_of_cities,
                 'registrydates': list_of_registrydates,
                 'birthdates': list_of_birthdates,
                 'emails': list_of_emails,
                 'phonenumbers': list_of_phonenumbers,
                 'locales': list_of_locales
             }

    return fake_data