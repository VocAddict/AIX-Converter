from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='AIX Converter',
    version='0.0.1',
    description='take English text and convert it to IPA and X-SAMPA',
    author=['vocaddict', 'mphilli'],
    long_description=long_description,
    include_package_data=True,
    packages=['aix_conv'],
)
