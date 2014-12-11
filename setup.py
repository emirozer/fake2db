from setuptools import setup, find_packages
import os

setup(
    name='fake2db',
    version='0.0.2',
    author='Emir Ozer',
    author_email='emirozer@yandex.com',
    url='https://github.com/emirozer/fake2db',
    description='Generate test databases filled with fake data (current support - sqlite, mysql)',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    entry_points={'console_scripts':
                  ['fake2db = fake2db.fake2db:main']},
    install_requires=[
        'faker==0.4.2',
        'fake-factory>=0.4.2',
        'pymongo>=2.7.2',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
