try:
    from setuptools import settup
except ImportError:
    from distutils.core import setup
    
    config = {
        'description': 'My Project',
        'author': 'L',
        'url': 'URL to get it at.',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
    }

setup(**config)