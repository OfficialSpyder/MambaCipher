from setuptools import setup, find_packages

setup(
    name="MambaCipher",
    version="1.0.0",
    author="Sukhpal Kherera",
    author_email="www.sukhkher125@gmail.com",
    description="A custom proprietary encryption and encoding system for secure tokenization.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OfficialSpyder/MambaCipher",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
