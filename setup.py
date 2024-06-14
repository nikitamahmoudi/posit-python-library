from setuptools import setup, find_packages

setup(
    name='posit-python-library',
    version='1.0.0',
    packages=find_packages(),
    description='Python library for posit number representation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Niki Mahmoudi',
    author_email='niki.mahmoudi22@gmail.com',
    url='https://github.com/nikitamahmoudi/posit-python-library',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
