from setuptools import setup, find_packages

setup(
    name="salah-ahmedyn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
    ],
    author="Salah Ahmed",
    description="Professional Async SDK for EzRemove API",
    python_requires=">=3.7",
)
