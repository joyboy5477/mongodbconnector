# Import necessary functions from setuptools
from setuptools import setup, find_packages

# Open the README.md file to use it as the long description for the package.
# 'encoding='utf-8'' ensures that the file is read with the correct text encoding.
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     

# Define the version of the package.
# This should be updated with each new release of the package.
__version__ = "0.0.4"

# Define the name of the GitHub repository where the package is hosted.
REPO_NAME = "mongodbconnector"

# Define the name of the package as it will appear on the Python Package Index (PyPI).
# Users will install your package from PyPI using this name.
PKG_NAME= "mongodbconnector" 

# Define the GitHub username of the author of the package.
# This is useful for linking to the author's profile and for attribution.
AUTHOR_USER_NAME = "joyboy5477" 

# Define the email address of the author of the package.
# This allows users to contact the author with questions or issues.
AUTHOR_EMAIL = "vishwaka@usc.edu"

# Call the setup function, which is the central feature of setuptools.
# This function takes several arguments that define the metadata and behavior of the package.
setup(
    # The name of the package.
    name=PKG_NAME,
    
    # The current version of the package. It's important for package maintenance and updates.
    version=__version__,
    
    # The author's name or username.
    author=AUTHOR_USER_NAME,
    
    # The author's email address.
    author_email=AUTHOR_EMAIL,
    
    # A short, one-line description of the package.
    description="A python package for connecting with database.",
    
    # A long description of the package. This is displayed on the package's PyPI page.
    # Typically, it's the contents of the README.md file, which can include markdown formatting.
    long_description=long_description,
    
    # The content type of the long description. Here it is specified that the description is in Markdown.
    long_description_content_type="text/markdown",
    
    # A URL to the homepage of the package, which is typically its GitHub repository.
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    # Additional URLs that are related to the project, like where to submit bugs or find the documentation.
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    
    # A dictionary mapping package names to directory names.
    # An empty string for the key tells setuptools that the packages are located directly under "src".
    package_dir={"": "src"},
    
    # Using find_packages() to automatically find all packages and subpackages under "src".
    # In this case, "where='src'" tells find_packages to look for packages in the "src" directory.
    packages=find_packages(where="src"),
)

# This script, when executed, will use the setuptools module to install your package.
# It is also used when you create a distribution of your package (e.g., a wheel or a source archive) that can be uploaded to PyPI.
