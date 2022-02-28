from setuptools import setup, find_packages

setup(
    name='django_version_viewer',
    description="Django app for viewing pip packages and their versions",
    keywords="django python version pip",
    version='2.1.0',
    packages=find_packages(),
    install_requires=(
    ),
    extras_require={
        'testing': ["mock", "six", 'flake8', 'coverage'],
    },
    url="https://github.com/ImaginaryLandscape/django-version-viewer",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
    ]
)
