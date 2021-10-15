from setuptools import setup, find_packages

setup(
    name="xlsx_validator",
    version="1.0",
    author="Pandaaaa906",
    author_email="ye.pandaaaa906@gmail.com",
    description="Thanks to pydantic, we got a nicer way to extra & validate rows from xslx",
    url="https://github.com/Pandaaaa906/xlsx_validator",
    packages=find_packages(exclude=['tests']),
)
