# wkhtmltopdf-wrapper


A simple and direct python wrapper for the wkhtmltopdf lib (https://github.com/wkhtmltopdf/wkhtmltopdf)
inspired by inspired by Qoda\'s python-wkhtmltopdf

## Requirements

### System:

- Linux 32/64 or OSX only (Windows is not supported at this stage)
- wkhtmltopdf
- python 2.5+ / python3

## Installation

### wkhtmltopdf (Linux)

1. Install Fonts:

```bash
$ sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
```

2. Install wkhtmltopdf:

```bash
$ sudo apt-get install wkhtmltopdf    
```
or goto [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) for the latest release (Recommended)

### wkhtmltopdf (OSX)

```bash
$ brew install wkhtmltopdf
```
or goto [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) for the latest release (Recommended)

## wkhtmltopdf-wrapper (Any Platform)

1. PIP:

```bash
$ pip install wkhtmltopdf-wrapper
```
or 
```bash
$ pip install git+https://github.com/aguegu/python-wkhtmltopdf.git    
```

2. Development:

```bash
$ git clone https://github.com/aguegu/python-wkhtmltopdf.git
$ cd python-wkhtmltopdf
$ virtualenv .
$ pip install -r requirements.pip
```

# Usage


## Use from class::

```python
  from wkhtmltopdf import WKHtmlToPdf
  
  wkhtmltopdf = WKHtmlToPdf('-T 20 -B 20 -g --zoom 1.5')
  
  # the option_string would be sent to the wkhtmltopdf command line in 
  # the exactly the same shape.
  # so the options can be anything as long as the wkhtmltopdf supports
  # check its [usage](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt)
  
  wkhtmltopdf.render('http://www.example.com', '~/example.pdf')
  # the source url, and the output file
```  

## Use from method::

```python
  from wkhtmltopdf import wkhtmltopdf
  wkhtmltopdf('example.com', '~/example.pdf', '-T 20 -B 20 -g --zoom 1.5')
```

## Use from commandline (installed)::

```bash
  $ python -m wkhtmltopdf.main example.com ~/example.pdf -T 20 -B 20 -g --zoom 1.5
```
