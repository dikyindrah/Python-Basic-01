from setuptools import find_packages, setup

setup(
    name='mtklib',
    packages=find_packages(include=['mtklib']),
    version='0.1.0',
    description='Test membuat library python',
    author='dikyindrah',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test',
)