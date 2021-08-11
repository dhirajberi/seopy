from distutils.core import setup
import setuptools

def readme():
    with open(r'README.txt') as f:
        README = f.read()
    return README

setup(
    name = 'seopy', ###################################
    packages = setuptools.find_packages(),

    version = '1.0',
    license='MIT',
    description = 'Instantly analyze your SEO issues',
    author = 'Dhiraj Beri',
    author_email = 'dhirajberi.official@gmail.com',
    url = 'https://github.com/cyborg7898/Geet-Song-Downloader-', #Github link
    download_url = 'https://github.com/Ankit404butfound/awesomepy/archive/1.0.tar.gz',#No need to change
    keywords = ['seo', 'seopy'],
    install_requires=[
          'selenium',
      ],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
)
