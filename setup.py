from distutils.core import setup

setup(
    name='pyble',
    version='0.01',
    author='Mingze',
    author_email='mzxu@outlook.com',
    packages=['ble','samples'],
    scripts=['README.md'],
    license="MIT",
    url='https://github.com/mzxu/pyble',
    install_requires=["pyserial"],
    description='Bluetooth Low Energy Python module based on TI cc2540',
    long_description=open('README.md').read()
    )