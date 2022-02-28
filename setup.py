# noqa: D100

from setuptools import setup

setup(
    name="pyjucontrol",
    version="0.1.0",
    description="A JU-Control client library",
    author="Dreanaught",
    author_email="Dreanaught@example.com",
    license="MIT",
    url="https://github.com/Dreanaught/pyjucontrol",
    python_requires=">3.9",
    packages=["pyjucontrol"],
    keywords=["homeautomation", "jucontorl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Home Automation",
    ],
    install_requires=["aiohttp"],
    scripts=[],
)