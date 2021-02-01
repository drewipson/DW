import setuptools

with open("./README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DW",
    version="0.0.3",
    author="Drew Ipson",
    author_email="drewipson@gmail.com",
    description="A small python package full of useful methods for data cleaning and manipulation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewipson/DW",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)