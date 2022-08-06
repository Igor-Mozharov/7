from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='test package',
      author='Mozharov Igor',
      author_email='r5@ukr.net',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean-folder=clean_folder.main:main']}
      )
