from setuptools import setup, find_packages
import os

setup(
    name='fake2db',
    version='0.5.1',
    author='Emir Ozer',
    author_email='emirozer@yandex.com',
    url='https://github.com/emirozer/fake2db',
    description=
    'Generate test databases filled with fake data (NOW CUSTOM SCHEMA CREATION SUPPORTED)(current support - sqlite, mysql, postgresql, mongodb, redis, couchdb)',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    entry_points={'console_scripts': ['fake2db = fake2db.fake2db:main']},
    install_requires=[
        'fake-factory>=0.5.3',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ], )
