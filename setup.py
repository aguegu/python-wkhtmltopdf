from setuptools import setup, find_packages

setup(
    name='wkhtmltopdf-wrapper',
    version='0.3.3',
    description='A Simpler python wrapper for wkhtmltopdf, inspired by Qoda\'s python-wkhtmltopdf',
    long_description="%s\n\n%s" % (open('README.rst', 'r').read(), open('AUTHORS.rst', 'r').read()),
    author='aGuegu',
    author_email='weihong.guan@gmail.com',
    license='BSD',
    url='http://github.com/aguegu/wkhtmltopdf-wrapper',
    packages=find_packages(),
    dependency_links=[],
    install_requires=[],
    include_package_data=True,
    keywords = "wkhtmltopdf pdf",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
