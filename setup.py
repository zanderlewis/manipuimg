from setuptools import setup, find_packages

setup(
    name='manipuimg',
    version='0.0.1',
    author='WolfTheDev',
    author_email='wolfthedev@gmail.com',
    description='A simple image manipulation library',
    url='https://github.com/WolfTheDeveloper/manipuimg',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'matplotlib',
    ],
)