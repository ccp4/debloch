import setuptools

#with open("latex/README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="debloch",
    version="0.2",
    author="Tarik Ronan Drevon",
    author_email="tarik.drevon@stfc.ac.uk",
    description="Blochwave simulator for Continuous Electron Diffraction ",
    long_description='contains a builtin Blochwave solver and a wrapper for FELIX, an efficient fortran implement blohwave based dynamical refinement solver ', #long_description,
    long_description_content_type="",
    url="https://www.ccp4.com/ccp4-ed/debloch",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License ",
        "Operating System :: POSIX :: Linux ",
    ],
    python_requires='>=3.8',
    install_requires=['EDutilities',
        #'TDdisplay',
        'numpy','scipy','matplotlib','colorama','pandas',
        'crystals',
        # 'easygui','tifffile','bsd','pickle5','bs4'
        ],
)
