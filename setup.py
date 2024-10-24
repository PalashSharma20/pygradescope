from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package for interacting with Gradescope'
LONG_DESCRIPTION = 'A package that allows you to interact with Gradescope using Python.'

setup(
        name="pygradescope", 
        version=VERSION,
        author="Palash Sharma",
        author_email="<hi@palashsharma.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add requests?
        keywords=['python', 'gradescope', 'api', 'automation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
        ]
)
