from setuptools import find_packages, setup

setup(
    name='protobuf_metta',
    packages=find_packages(include=['protobuf_metta']),
    version='0.1.0',
    description='Protocol Buffers to MeTTa converter',
    author='Nil Geisweiller',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
