from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='capi',
      version='0.0.1',
      description='Central API',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='Netw0rk',
      url='http://gitlab.com/network-sdn/capi',
      author='Guillaume 0xa Ladhuie',
      author_email='gladhuie@gmail.com',
      license='MIT',
      packages=['capi'],
      install_requires=[

      ],
      include_package_data=True,
      zip_safe=False)