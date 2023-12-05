from setuptools import setup, find_packages

setup(
    name='AnkiTest',
    version='1.0.0',
    description='Program for making test from anki database',
    author='Michał Nowakowski',
    author_email='michaldariusznowakowski@proton.me',
    url='https://link.do.repozytorium',
    packages=find_packages(
        include=['ankidata', 'ankidata.*', 'gui', 'gui.*', 'docxsave.*', 'doxysave', 'start.*', 'start']),
    install_requires=[
        'python-docx',
        'customtkinter',
        'anki',
        'packaging',
        'pillow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [
            'AnkiTest = start.core:main_function',
        ],
    }
)