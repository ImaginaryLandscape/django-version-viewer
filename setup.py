from setuptools import setup

setup(
    name='django_version_viewer',
    version='0.0.1a7',
    packages=['django_version_viewer'],
    install_requires=(
    ),
    description="Django app for viewing pip packages and their versions",
    long_description=open('README.md', 'r').read(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Framework :: Django :: 1.8'
    ]
)
