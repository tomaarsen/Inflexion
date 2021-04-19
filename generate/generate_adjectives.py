#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, json
from datetime import datetime
from typing import List, Tuple, Optional

from generate_tests import TestWriter

"""
Compiled variants of useful regexes used all around this file
"""
xms  = re.VERBOSE | re.MULTILINE | re.DOTALL
COMMENT_LINE_PAT = re.compile(r" \A \s* \#",         flags=xms)
COMMENT_PAT      = re.compile(r" \# .* ",            flags=xms)
BLANK_LINE_PAT   = re.compile(r" \A \s* $ ",         flags=xms)
WS               = re.compile(r" [\s]* ",            flags=xms)
WORD_SEQ         = re.compile(r" \S* (?: \s \S+)* ", flags=xms)
DATA_PAT         = re.compile(r"""
    \A
        {WS}
        ( {WORD_SEQ} )      # singular
        {WS}=>{WS}
        ( {WORD_SEQ} )      # plural
        {WS}
        (?:{COMMENT_PAT})?  # Optional trailing comment
    \Z
""".format(WS=WS.pattern, WORD_SEQ=WORD_SEQ.pattern, COMMENT_PAT=COMMENT_PAT.pattern),
    flags=xms)
"""
CONS     = re.compile(r"\(CONS\)", flags=xms)
VOWEL    = re.compile(r"\(VOWEL\)", flags=xms)
VOWELY   = re.compile(r"\(VOWELY\)", flags=xms)
DASH     = re.compile(r"-")
STAR     = re.compile(r"\*")
RESTRICT = re.compile(r"( \[.*?\] )+", flags=xms)
SPLIT    = re.compile(r"(.*?) [|] (.*)", flags=xms)
"""

class Adjective(object):
    def __init__(self, match):
        super().__init__()

        self.sing = match.group(1)
        self.plur = match.group(2)

    def __str__(self) -> str:
        return f"Singular: {self.sing}\nPlural  : {self.plur}"

class Reader(object):
    def __init__(self, fname: str):
        types = ["plural", "singular"]
        self.literals = {key:{} for key in types}
        self.words    = {key:set() for key in types}
        self.fname    = fname

    def get_readlines(self) -> List[str]:
        with open(self.fname, "r") as f:
            return f.readlines()

    def parse_file(self):
        lines = self.get_readlines()
       
        # Read lines in reverse so the first lines are eventually checked before the later ones
        for line in lines[::-1]:
            # Skip empty or comment lines
            if COMMENT_LINE_PAT.match(line) or BLANK_LINE_PAT.match(line):
                continue
           
            # Extract data
            match = DATA_PAT.match(line)
            if match:
                sing = match.group(1)
                plur = match.group(2)
                self.literals["plural"][sing]   = plur
                self.literals["singular"][plur] = sing
                self.words["plural"].add(plur)
                self.words["singular"].add(sing)
            else:
                # TODO: Change exception
                raise Exception("Unknown input:", line)
           

class CodeWriter(object):
    def __init__(self, reader, fname):
        super().__init__()
        self.reader = reader
        self.fname = fname
   
    def write_file(self):
        version = datetime.strftime(datetime.now(), '%Y%m%d.%H%M%S')
        generated_code = f'''\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import re

VERSION = {version}

adj_is_singular = {json.dumps(sorted(self.reader.words["singular"]), indent=4)}

adj_is_plural = {json.dumps(sorted(self.reader.words["plural"]), indent=4)}

adj_singular_of = {json.dumps(self.reader.literals["singular"], indent=4, sort_keys=True)}

adj_plural_of = {json.dumps(self.reader.literals["plural"], indent=4, sort_keys=True)}

def is_plural(word: str) -> bool:
    """Detect whether `word` is in plural form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: True if `word` is deemed plural.
    """
    return word in adj_is_plural or\\
           word.lower() in adj_is_plural or\\
           (word not in adj_is_singular and word.lower() not in adj_is_singular)

def is_singular(word: str) -> bool:
    """Detect whether `word` is in singular form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: True if `word` is deemed singular.
    """
    return word in adj_is_singular or\\
           word.lower() in adj_is_singular or\\
           (word not in adj_is_plural and word.lower() not in adj_is_plural)

def convert_to_plural(word: str) -> str:
    """Convert `word` to plural form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: The plural form of `word`.
    """
    if word in adj_plural_of:
        return adj_plural_of[word]
    if not word.islower() and word.lower() in adj_plural_of:
        return adj_plural_of[word.lower()]
    return word

def convert_to_singular(word: str) -> str:
    """Convert `word` to singular form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: The singular form of `word`.
    """
    if word in adj_singular_of:
        return adj_singular_of[word]
    if not word.islower() and word.lower() in adj_singular_of:
        return adj_singular_of[word.lower()]
    return word
'''
        self.output_code(generated_code)

    def output_code(self, generated_code):
        with open(self.fname, "w+") as f:
            f.write(generated_code)

class VerbTestWriter(TestWriter):
    def __init__(self, reader, class_name):
        super().__init__(class_name)
        self.reader = reader
        """
        For each test case we need the following information to be passed to the format:
        test_class:         Equivalent to class_name, already known as self.test_class
        test_function:      Name of function to test.
        test_args:          List of dictionaries with testing arguments.
        test_name_pascal:   Name of the test in Pascal Case
        """
   
    def write_tests(self):
        self.write_is_singular_test()
        self.write_is_plural_test()
        self.write_to_singular_test()
        self.write_to_plural_test()

    def write_is_singular_test(self):
        test_path = self.test_folder_name + "//test_adjective_core_is_singular.py"
        test_function = "is_singular"
        test_name_pascal = "AdjectiveIsSingular"
        test_args = [
            {
                "in": sing,
                "out": True
            } for plur, sing in self.reader.literals["singular"].items()
        ]
        test_args += [
            {
                "in": plur,
                "out": False
            } for plur, sing in self.reader.literals["singular"].items()
            if sing != plur
        ]
        test_args += [
            {
                "in": args["in"].title(),
                "out": args["out"]
            } for args in test_args
        ]
        self.write_test(test_path, test_function, test_name_pascal, test_args)

    def write_is_plural_test(self):
        test_path = self.test_folder_name + "//test_adjective_core_is_plural.py"
        test_function = "is_plural"
        test_name_pascal = "AdjectiveIsSingular"
        test_args = [
            {
                "in": plur,
                "out": True
            } for sing, plur in self.reader.literals["plural"].items()
        ]
        test_args += [
            {
                "in": sing,
                "out": False
            } for sing, plur in self.reader.literals["plural"].items()
            if sing != plur
        ]
        test_args += [
            {
                "in": args["in"].title(),
                "out": args["out"]
            } for args in test_args
        ]
        self.write_test(test_path, test_function, test_name_pascal, test_args)

    def write_to_singular_test(self):
        test_path = self.test_folder_name + "//test_adjective_core_to_singular.py"
        test_function = "singular"
        test_name_pascal = "AdjectiveToSingular"
        test_args = [
            {
                "in": sing,
                "out": sing
            } for plur, sing in self.reader.literals["singular"].items()
        ]
        test_args += [
            {
                "in": plur,
                "out": sing
            } for plur, sing in self.reader.literals["singular"].items()
        ]
        test_args += [
            {
                "in": args["in"].title(),
                "out": args["out"].title()
            } for args in test_args
            if len(args["in"]) > 1
        ]
        self.write_test(test_path, test_function, test_name_pascal, test_args)

    def write_to_plural_test(self):
        test_path = self.test_folder_name + "//test_adjective_core_to_plural.py"
        test_function = "plural"
        test_name_pascal = "AdjectiveToPlural"
        test_args = [
            {
                "in": plur,
                "out": plur
            } for sing, plur in self.reader.literals["plural"].items()
        ]
        test_args += [
            {
                "in": sing,
                "out": plur
            } for sing, plur in self.reader.literals["plural"].items()
        ]
        test_args += [
            {
                "in": args["in"].title(),
                "out": args["out"].title()
            } for args in test_args
            if len(args["in"]) > 1
        ]
        self.write_test(test_path, test_function, test_name_pascal, test_args)

if __name__ == "__main__":
    in_fname = "lei//adjectives.lei"
    out_fname = "inflex//adjective_core.py"
    class_name = "Adjective"
    reader = Reader(in_fname)
    reader.parse_file()
   
    cwriter = CodeWriter(reader, out_fname)
    cwriter.write_file()
   
    twriter = VerbTestWriter(reader, class_name)
    twriter.write_tests()
