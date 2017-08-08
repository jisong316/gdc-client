from setuptools import setup, find_packages
from gdc_client.version import __version__

setup(
    name="gdc_client",
    version=__version__,
    packages=find_packages(),
    package_data={},
    install_requires=[
        'parcel',
        'lxml==3.5.0b1',
        'PyYAML==3.11',
        'jsonschema==2.5.1',
        'pyOpenSSL==17.1.0',
        'ndg-httpsclient==0.4.2',
        'pyasn1==0.2.3',
    ],
    dependency_links=[
        'git+https://github.com/LabAdvComp/parcel.git@028a59d09f221f97465291b8c21ce28692d132cf#egg=parcel',
    ],
    scripts=[
        'bin/gdc-client',
    ],
)
