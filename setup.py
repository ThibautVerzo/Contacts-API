from setuptools import find_packages, setup

setup(
    name='contactsapi',
    description='API for contact management',
    long_description=open('README.md').read(),
    url='https://github.com/ThibautVerzo/Contacts-API.git',
    author='Thibaut Verzotti',
    author_email='thibaut.verzotti@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['contactsapi=contactsapi.commands:run']}
)