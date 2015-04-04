# wkhtmltopdf-wrapper

A simple and direct python wrapper for the [wkhtmltopdf lib](https://github.com/wkhtmltopdf/wkhtmltopdf)
inspired by inspired by [Qoda's python-wkhtmltopdf](https://github.com/qoda/python-wkhtmltopdf)

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

2. Install wkhtmltopdf

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
$ pip install git+https://github.com/aguegu/wkhtmltopdf-wrapper.git
```

2. Development:

```bash
$ git clone https://github.com/aguegu/wkhtmltopdf-wrapper.git
$ cd python-wkhtmltopdf
$ virtualenv .
$ pip install -r requirements.pip
```

# Usage

the option_string would be sent to the wkhtmltopdf command line in exactly the same shape. so the options can be anything as long as the wkhtmltopdf supports. check its [usage](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt).
This lib is just as simple as that. If anything goes wrong, just check the doc. If the command execute ok with  wkhtmltopdf dircetly, this wrapper should work too. 

As I check [qoda/python-wkhtmltopdf](https://github.com/qoda/python-wkhtmltopdf), where this repo forked from, it tried to prase args. But it only include a small set of the arguments the command supports. Furthermore, it set default values to this set of arguments and pass them all to the command. For me, it is totally unnecessary and even mistakeful. There is default setting setup and doc in the command. Some arugments may not even work together, as `--page-size` and `--page-height`, `--page-width`. So my solution is just pass the option in as a string, Lazy, flexible and effective.

### from class:

```python
  from wkhtmltopdf import WKHtmlToPdf
  
  wkhtmltopdf = WKHtmlToPdf('-T 20 -B 20 -g --zoom 1.5')
  # option_string
  
  wkhtmltopdf.render('http://www.example.com', '~/example.pdf')
  # source url, output file path
```  

### from method:

```python
  from wkhtmltopdf import wkhtmltopdf
  wkhtmltopdf('example.com', '~/example.pdf', '-T 20 -B 20 -g --zoom 1.5')
```

### from commandline (installed):

```bash
  $ python -m wkhtmltopdf.main example.com ~/example.pdf -T 20 -B 20 -g --zoom 1.5
```

