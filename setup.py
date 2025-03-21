from setuptools import setup

setup(
    name='ridemaster',
    version='0.1',
    description='Tool to assign rides',
    author='dhong',
    author_email='ddanielhongg@gmail.com',
    packages=['ridemaster'],
    install_requires=[
        'python-dotenv',
        'googlemaps',
    ],
)
