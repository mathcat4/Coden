from setuptools import setup
with open("README.md") as file:
          long_description = file.read()
setup(name='coden',
      version='0.6',
      description='Has functions on topic "codes"',
      long_description = long_description,
      long_description_content_type="text/markdown",
      author='Tanmay Earappa',
      author_email='Tams.Mathe@gmail.com',
      license = 'MIT',
      packages=['coden'],
      url = "https://github.com/Tams-Tams/Codes/tree/master/coden_0.6.git",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      
      zip_safe=False)
