from distutils.core import setup

# from setuptools import setup, find_packages

# read the contents of your README file
from os import path

# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, "README.html"), encoding="utf-8") as f:
#    long_description = f.read()

setup(
    name="cloudapi_digitalocean",
    # package_dir={"": "src"},
    packages=[
        "cloudapi_digitalocean",
        "cloudapi_digitalocean.common",
        "cloudapi_digitalocean.digitaloceanapi",
        "cloudapi_digitalocean.digitaloceanobjects",
    ],
    version="0.0.5",
    license="MIT",
    description="cloudapi_digitalocean, represents all digital ocean services as objects, hiding all those horrible api calls.",
    # long_description=long_description,
    # long_description_content_type="text/html",
    author="zoran ilievski",
    author_email="pythonic@clientuser.net",
    url="https://github.com/zorani/cloudapi_digitalocean",
    download_url="https://github.com/zorani/cloudapi_digitalocean/archive/refs/tags/v0.0.5.tar.gz",
    keywords=["digitalocean", "api"],
    install_requires=["cloudapi"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
