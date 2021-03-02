from setuptools import setup, find_packages


requirements = [
    "pillow", "opencv-python-headless", "numpy", "pyclipper",
]

tests_requirements = [
    "pytest", "pytest-cov"
]

lint_requirements = [
    "flake8",
]

doc_requirements = [
    "sphinx"
]

setup(
    name='pimento',
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    url='https://github.com/antoinehumbert/pimento',
    license='Apache License 2.0',
    author='Antoine HUMBERT',
    author_email='antoine.humbert.dev@gmail.com',
    description='Python IMage ENhanced TOols',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
    ],
    install_requires=requirements,
    extras_require={
        "tests": tests_requirements,
        "lint": lint_requirements,
        "doc": doc_requirements,
    }
)
