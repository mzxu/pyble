from setuptools import setup
setup(
    name='pyble',
    version='0.02',
    author='Mingze',
    author_email='mzxu@outlook.com',
    packages=['ble','samples'],
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    url='https://github.com/mzxu/pyble',
    install_requires=["pyserial"],
    description='Bluetooth Low Energy Python module based on TI cc2540',
    long_description="Bluetooth Low Energy Python module based on TI cc2540.",
    )