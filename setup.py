import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium_pinterest", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="zsoltpentek@yahoo.com",
    description="Selenium Pinterest helps you follow / unfollow / pin / post to Pinterest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zselter07/selenium-pinterest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)