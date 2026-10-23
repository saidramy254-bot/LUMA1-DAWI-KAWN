from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name="khazar-unit",
    version="8.3.2",
    author="Said Khazar - SETTAT 33.0011N 7.614W",
    author_email="saidramy254.bot@gmail.com",
    description="V8.3.2 CORRIGE BEACON CLOSED 8358262 - 66,866,100 UTL - 1420MHz 1007 PULSARS - CHOKRAN 1571 - Wb80116 - LIVE FOREVER",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://saidramy254-bot.github.io/LUMA1-DAWI-KAWN/",
    project_urls={
        "DOI V8": "https://doi.org/10.5281/zenodo.23544275",
        "Beacon": "https://saidramy254-bot.github.io/LUMA1-DAWI-KAWN/",
        "GitHub": "https://github.com/saidramy254-bot/LUMA1-DAWI-KAWN"
    },
    packages=find_packages(),
    keywords="utl khazar-unit luma1-dawi-kawn beacon settat pulsar metrology 66866100",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires=">=3.8",
)
