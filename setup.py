"""
setup.py

This file is essential for packaging and distributing Python projects.
It uses setuptools to define configuration such as project metadata,
dependencies, and packaging instructions.
"""

from setuptools import find_packages, setup
from typing import List


def get_requirements(filename: str = "requirements.txt") -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.

    Args:
        filename (str): Path to the requirements file.

    Returns:
        List[str]: A list of package requirements without empty lines or '-e .'.
    """
    requirements: List[str] = []
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements.append(requirement)
    except FileNotFoundError:
        print(f"⚠️  {filename} file not found. Proceeding without install_requires.")

    return requirements


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sourav",
    author_email="skumar.choudhary2612@gmail.com",
    description="A Python project for network security applications.",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.7",
    
)
