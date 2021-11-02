# coding=utf-8
__author__ = 'velazquezerick'

import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> N | Det N | Det N PP
VP -> V | V PP | V NP | V NP PP
PP -> Prep N | Prep NP
N -> "Alexia" | "Erick" | "marche" | "boîte" |  "crayons" |  "table" | "garçon" | "femme" | "telescope"
V -> "rit" | "pleure" | "joue" | "prend" | "est" | "regarde" | "donne"
Prep -> "avec" | "à" | "sur"
Det -> "une" | "la" | "le" | "un"
""")

sent = "Alexia donne un telescope à Erick".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)


for tree in rd_parser.nbest_parse(sent):
    print tree.draw()
