from setuptools import setup, find_packages
setup(
        name="blastneuron",
        packages=find_packages(exclude=["^\."]),
        package_data={
                        '': []
                    },
        exclude_package_data={'': ["Readme.txt"]},
        install_requires=["subprocess32", "pathlib2"],
        python_requires=">=2.7",
    )