from setuptools import setup

setup(
    packages=['mcag'],
    name = 'mcag',
    version = '0.1.0',
    author='Adil Gurbuz',
    author_email='adlgrbz@protonmail.com',
    url='https://github.com/adlgrbz/achievement-generator',
    install_requires=[
        'pillow==6.1.0',
    ],
    entry_points='''
        [console_scripts]
        mcag=achievement-generator.mcag:main
    ''',
)
