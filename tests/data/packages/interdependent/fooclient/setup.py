from setuptools import setup, find_packages

setup(
    name='fooclient',
    version='1.0',
    description="Test package",
    install_requires=[
        "foolib==1.0"
    ],
    py_modules=['fooclient']
)
