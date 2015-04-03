#!/usr/bin/env python
from subprocess import Popen
from subprocess import PIPE

class WKHtmlToPdf(object):
    
    def __init__(self, options_str=''):
        self.options_str = options_str

    def render(self, url, output_file):
        command = 'wkhtmltopdf %s "%s" "%s" >> /tmp/wkhtp.log' % (
            self.options_str,
            url,
            output_file
        )
        try:
            p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
            stdout, stderr = p.communicate()
            retcode = p.returncode

            if retcode == 0:
                # call was successful
                return
            elif retcode < 0:
                raise Exception("Terminated by signal: ", -retcode)
            else:
                raise Exception(stderr)

        except OSError as exc:
            raise exc

def wkhtmltopdf(url, output_file, options_str=''):
    wkhp = WKHtmlToPdf(options_str)
    wkhp.render(url, output_file)

if __name__ == '__main__':
    import sys
    options_str = ' '.join(sys.argv[3:])
    wkhtmltopdf(sys.argv[1], sys.argv[2], options_str)