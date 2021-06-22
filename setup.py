# from distutils.core import setup
##How to package
##From your root package dir...
##python3 setup.py sdist
##twine check dist/*
##twine upload dist/*


from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="digitaloceanobjects",
    packages=[
        "digitaloceanobjects",
        "digitaloceanobjects.common",
        "digitaloceanobjects.digitaloceanapi",
        "digitaloceanobjects.digitaloceanobject",
    ],
    version="0.0.20",
    license="MIT",
    description="digitaloceanobjects, represents all digital ocean services as objects, hiding all those horrible api calls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zoran ilievski",
    author_email="pythonic@clientuser.net",
    url="https://github.com/zorani/digitalocean-objects",
    download_url="https://github.com/zorani/digitalocean-objects/archive/refs/tags/v0.0.20.tar.gz",
    keywords=["digitalocean", "api", "objects", "digitaloceanapi"],
    install_requires=["cloudapi"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
