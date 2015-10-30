import os
from setuptools import setup


setup(
    name='filesanitize',
    version='1.0.1',
    url='https://github.com/marcinn/filesanitize',
    license='BSD',
    author='Marcin Nowak',
    author_email='marcin.j.nowak@gmail.com',
    description='Filesanitize is a small library for making save paths and filenames by removing accents and special chars',
    py_modules=['filesanitize'],
    install_requires=['translitcodec==0.4'],
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: Utilities',
    ]
)
