from setuptools import setup

setup (
    name='ujs-jsonsyntax',
    version='0.1.0',
    description='JSON syntax checker',
    long_description=open('README.rst').read(),
    url='http://github.com/usingjsonschema/ujs-jsonsyntax-python',
    author='Joe McIntyre',
    author_email='j_h_mcintyre@yahoo.com',
    keywords='bookujs json',
    license='MIT',
    packages=['jsonsyntax'],
    entry_points={
        'console_scripts':[
            'jsonsyntax=jsonsyntax.jsonsyntax:main',
            'jsonsyntaxp=jsonsyntax.jsonsyntax:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development'
    ])
