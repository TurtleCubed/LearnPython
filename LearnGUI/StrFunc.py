#!/usr/bin/env python
###############################################################################################
#
# @file      StrFunc.py
# @author    Tristan Yoo (tristan.yoo@gmail.com)
# @date      June 10, 2019
# @brief     Provides string editing methods that are used in StringButtons
#
# @copyright Copyright (c) 2019 Tristan Yoo
#
###############################################################################################


def caps(string):
    return string.upper()


def revWords(string):
    words = string.split()
    reversed_word = ""
    for word in words:
        reversed_word = word + " " + reversed_word
    while reversed_word[len(reversed_word) - 1] == " ":
        reversed_word = reversed_word[:-1]
    return reversed_word


def reverse(string):
    reversed_string = ""
    for i in range(len(string)):
        reversed_string = string[i] + reversed_string
    return reversed_string


def red(string):
    return string
