#!/usr/bin/env python3
"""
Setup script for COVID-19 Genetic Risk Analysis Tutorial
"""

from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="covid19-genetic-risk-analysis",
    version="1.0.0",
    author="COVID-19 Genetic Risk Analysis Tutorial Team",
    author_email="your.email@institution.edu",
    description="A comprehensive tutorial for analyzing genetic risk variants associated with severe COVID-19",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/covid19-genetic-risk-analysis",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/covid19-genetic-risk-analysis/issues",
        "Documentation": "https://github.com/yourusername/covid19-genetic-risk-analysis/blob/main/docs/",
        "Source Code": "https://github.com/yourusername/covid19-genetic-risk-analysis",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "jupyter>=1.0.0",
        ],
        "bio": [
            "bioservices>=1.8.0",
            "gprofiler-official>=1.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml", "*.csv", "*.png", "*.jpg", "*.ipynb"],
    },
    entry_points={
        "console_scripts": [
            "covid19-test=scripts.test_tutorial:main",
            "covid19-generate-data=scripts.create_synthetic_dataset:main",
        ],
    },
    keywords=[
        "covid19", "genetics", "gwas", "network-analysis", "bioinformatics", 
        "tutorial", "education", "genomics", "risk-analysis"
    ],
)

