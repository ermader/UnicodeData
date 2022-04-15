from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="UnicodeData",
    version="0.2",
    packages=find_packages(),
    package_data={
        "":  ["Data/*.dat"],
    },

    python_requires=">=3.9",
    install_requires=[
        "fonttools >= 4.2.2",
    ],

    author="Eric Mader",
    author_email="eric.mader@gmx.us",
    description="A port of ICU UnicodeSet object and character data access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ermader/UnicodeData/",
    license_files=["LICENSE.md"],

    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.8",
        "Topic :: Text Processing :: Fonts",
    ]
)
