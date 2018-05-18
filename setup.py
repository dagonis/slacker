from setuptools import setup


setup(
    name='slackest',
    version='0.1',
    packages=['slackest'],
    description='Slack API client',
    author='Kevin Tyers',
    author_email='ktyers@gmail.com',
    url='http://github.com/dagonis/slackest/',
    install_requires=['requests >= 2.2.1'],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='slack api'
)
