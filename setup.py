import minegen
from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="minegen",
    version=minegen.__version__,
    packages=["minegen"],
    package_dir={"minegen": "minegen"},
    description="Minecraft achievement generator",
    long_description=long_description,
    url="https://github.com/adlgrbz/minegen",
    author="Adil Gürbüz",
    author_email="adlgrbz@tutamail.com",
    platforms=["Linux"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="minecraft achievement generator",
    install_requires=["pillow"],
    package_data={
        "minegen": [
            "data/items/*.png",
            "data/background.png",
            "data/minecraft-font.ttf",
        ],
    },
    entry_points={"console_scripts": ["minegen = minegen:launch"]},
)
