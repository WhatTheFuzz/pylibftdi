"""
pylibftdi - python wrapper for libftdi

Copyright (c) 2010-2014 Ben Bass <benbass@codedstructure.net>
See LICENSE file for details and (absence of) warranty

pylibftdi: https://github.com/codedstructure/pylibftdi

This module contains some basic tests for the included examples.
"""

from __future__ import annotations

import unittest
from collections import OrderedDict
from typing import Any

from pylibftdi.examples.info import ftdi_info


class ExamplesTest(unittest.TestCase):
    """
    Test that some of the examples behave as expected.
    """

    def test_ftdi_info(self):
        """
        Test that the test_ftdi_info example runs without error.
        """
        info: OrderedDict[str, Any] = ftdi_info()

        # Assert that the dictionary contains the expected keys.
        for key in info.keys():
            self.assertIsInstance(key, str)
