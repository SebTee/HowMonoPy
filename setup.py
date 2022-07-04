from setuptools import setup

setup(name="HowMonoPy",
      version="0.1",
      description="A Python wrapper for the c library from how-monochromatic.",
      url="https://github.com/SebTee/HowMonoPy",
      author="Sebastian Tee",
      maintainer="Sebastian Tee",
      license="MIT",
      package_dir={"": "src"},
      packages=["HowMonoPy"],
      package_data={"HowMonoPy": ["clib/*"]},
      zip_safe=True)
