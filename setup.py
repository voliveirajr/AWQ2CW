try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'AMQ2CW',
    'author': 'Volmar Oliveira Junior',
    'author_email': 'volmar.oliveira.jr@gmail.com',
    'version': '0.1',
    'name': 'AMQ2CW'
}

setup(**config)