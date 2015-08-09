import sys
from setuptools import setup, find_packages

setup(
    name='stormalias',
    version='0.0.1',
    packages=find_packages(),
    package_data={'alias': ['templates/*.html', 'static/css/*.css',
                            'static/css/themes/alias/*.css', 'static/css/themes/alias/img/*.png',
                            'static/js/*.js', 'static/js/core/*.js', 'static/favicon.ico']},
    include_package_data=True,
    url='https://bitbucket.org/hieuht/storm-alias',
    license='MIT',
    author='Hieu Ha Trung',
    author_email='hieuht@vnoss.org',
    description='Management your alias.',
    entry_points={
        'console_scripts': [
            'stormalias = alias.__main__:main',
            ],
        },
    install_requires=list(filter(None, [
        "flask",
        "optparse" if sys.version_info[:2] < (2, 7) else None,
        ])),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Systems Administration',
    ]
)
