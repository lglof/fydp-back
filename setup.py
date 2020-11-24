from setuptools import find_packages, setup

setup(
    name='SOARback',
    packages=find_packages(include=['SOARback']),
    version='0.1.2',
    description='SYDE461/462 Group 03 Backend',
    author='lglof, asilverfox, derek',
    license='MIT',
    setup_requires=['pytest-runner'],
    test_requires=['pytest==4.4.1'],
    test_suite='tests',
)