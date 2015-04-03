#!/usr/bin/env python

import os
import unittest

from wkhtmltopdf.main import WKHtmlToPdf, wkhtmltopdf


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://cn.bing.com"
        self.output_file = "/tmp/bing.pdf"
        self.wkhtmltopdf = WKHtmlToPdf()

    def test_wkhtmltopdf_callable(self):
        wkhtmltopdf(self.url, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

    def tearDown(self):
        try:
            os.remove(self.output_file)
        except OSError:
            pass


if __name__ == '__main__':
    unittest.main()
