#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import re

VERSION = 20210415.220120

adj_is_singular = [
    "a",
    "an",
    "her",
    "his",
    "its",
    "my",
    "that",
    "their",
    "this",
    "your"
]

adj_is_plural = [
    "our",
    "some",
    "their",
    "these",
    "those",
    "your"
]

adj_singular_of = {
    "our": "my",
    "some": "a",
    "their": "their",
    "these": "this",
    "those": "that",
    "your": "your"
}

adj_plural_of = {
    "a": "some",
    "an": "some",
    "her": "their",
    "his": "their",
    "its": "their",
    "my": "our",
    "that": "those",
    "their": "their",
    "this": "these",
    "your": "your"
}

def is_plural(word: str) -> bool:
    """Detect whether `word` is in plural form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: True if `word` is deemed plural.
    """
    return word in adj_is_plural or\
           word.lower() in adj_is_plural or\
           (word not in adj_is_singular and word.lower() not in adj_is_singular)

def is_singular(word: str) -> bool:
    """Detect whether `word` is in singular form.

    Args:
        word (str): Input word or collocation.

    Returns:
        str: True if `word` is deemed singular.
    """
    return word in adj_is_singular or\
           word.lower() in adj_is_singular or\
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
