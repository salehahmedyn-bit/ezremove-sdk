from setuptools import setup, find_packages

setup(
    name="salah-ahmedyn",
    version="0.1.0",
    packages=[
        "ezremove",
        "ezremove.pyarmor_runtime_000000"
    ],
    package_data={
        "ezremove.pyarmor_runtime_000000": ["*.so", "*.py"],
    },
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.8.0",
    ],
)
