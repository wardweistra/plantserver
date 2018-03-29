from setuptools import setup, find_packages

NAME = 'PlantServer'
VERSION = '0.1'
mainscript = 'runserver.py'

setup(
    name=NAME,
    version=VERSION,
    description='Flask server to communicate with Arduino plant',
    url='https://github.com/wardweistra/plantserver',
    author='Ward Weistra',
    author_email='w@rdweistra.nl',
    license='GNU General Public License V3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    scripts=[mainscript],
)
