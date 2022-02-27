from distutils.core import setup
from setuptools import find_packages
setup(
  name = 'Topsis-Garvit-101903778',         
  packages = find_packages(),   
  version = '0.1',      
  license='MIT',        
  description = 'A Python package to find TOPSIS for multi-criteria decision analysis method',   # Give a short description about your library
  author = 'Garvit Nangia',                   
  author_email = 'nagiagarvit@live.com',      
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TOPSIS','TIET'],   
  install_requires=[            
          'pandas',
          'tabulate',
          'sys',
          'math',
          'os',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
