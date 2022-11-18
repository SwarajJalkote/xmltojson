from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='xmltojson',
  version='1.0.0',
  description='XML to JSON convertor with additional options to make the conversion more efficient and flexibility to add or remove columns from the conversion',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/SwarajJalkote/xmltojson.git',  
  author='Swaraj Jalkote',
  author_email='swarajjalkote98@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  py_modules=['xmltojson'],
  package_dir={'':'src'},
  keywords=['xml', 'json', 'convertor'], 
  install_requires=['setuptools', 'pandas'] 
)