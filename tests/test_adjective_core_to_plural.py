
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflex import Adjective


class TestAdjectiveToPlural(unittest.TestCase):
    '''
    test_args has the format [
        {
            "in":     ..., # (required)
            "out":    ..., # (required)
            "desc":   ..., # (optional)
            "kwargs": ...  # (optional)
        }, ...
    ]
    '''
    test_args = [
        {'in': 'An', 'out': 'Some'},
        {'in': 'Her', 'out': 'Their'},
        {'in': 'His', 'out': 'Their'},
        {'in': 'Its', 'out': 'Their'},
        {'in': 'My', 'out': 'Our'},
        {'in': 'Our', 'out': 'Our'},
        {'in': 'Some', 'out': 'Some'},
        {'in': 'That', 'out': 'Those'},
        {'in': 'Their', 'out': 'Their'},
        {'in': 'These', 'out': 'These'},
        {'in': 'This', 'out': 'These'},
        {'in': 'Those', 'out': 'Those'},
        {'in': 'Your', 'out': 'Your'},
        {'in': 'a', 'out': 'some'},
        {'in': 'an', 'out': 'some'},
        {'in': 'her', 'out': 'their'},
        {'in': 'his', 'out': 'their'},
        {'in': 'its', 'out': 'their'},
        {'in': 'my', 'out': 'our'},
        {'in': 'our', 'out': 'our'},
        {'in': 'some', 'out': 'some'},
        {'in': 'that', 'out': 'those'},
        {'in': 'their', 'out': 'their'},
        {'in': 'these', 'out': 'these'},
        {'in': 'this', 'out': 'these'},
        {'in': 'those', 'out': 'those'},
        {'in': 'your', 'out': 'your'},
    ]

    def test_adjective_to_plural(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"plural({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": {}
                }}
                self.assertEqual(Adjective(test_case["in"]).plural(**test_case["kwargs"]), test_case["out"], test_case["desc"])


if __name__ == "__main__":
    unittest.main()
