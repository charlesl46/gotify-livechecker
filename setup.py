from setuptools import setup, find_packages

setup(
    name='gotify-livechecker',
    version='0.1',
    packages=find_packages(),
    install_requires=[  
        'gotify',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'livechecker=check:main',
        ],
    },
)
