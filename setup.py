import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="debloch",
    version="0.3",
    author="Tarik Ronan Drevon",
    author_email="tarik.drevon@stfc.ac.uk",
    description="Blochwave simulator for Continuous Electron Diffraction",
    long_description=long_description,
    long_description_content_type="",
    url="https://pypi.org/project/debloch",
    project_urls={
        'Documentation': 'https://pyscatspheres.readthedocs.io/en/latest/',
        'Source':'https://github.com/ccp4/debloch',
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License ",
        "Operating System :: POSIX :: Linux ",
    ],
    python_requires='>=3.8',
    install_requires=['EDutilities>=0.2',
        #'TDdisplay',
        'numpy','scipy','matplotlib','colorama','pandas',
        'crystals',
        # 'easygui','tifffile','bsd','pickle5','bs4'
        ],
)
