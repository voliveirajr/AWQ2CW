try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'JMX2CW',
    'author': 'Volmar Oliveira Junior',
    'author_email': 'volmar.oliveira.jr@gmail.com',
    'version': '0.1',
    'name': 'JMX2CW'
}

setup(**config)