# coding=utf-8
__author__ = 'velazquezerick'
import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> N | Det N | Det N PP | "Erick" | "Alexia"
VP -> V | V NP | V NP PP | V PP PP
PP -> P NP
V -> "court" | "joue" | "prend" | "donne" | "regarde"
Det -> "ses" | "le" | "une" | "sa" | "la"
P -> "dans" | "avec" | "à"
N -> "garçon" | "marche" |"mère" |"lettre" | "jardin" | "amies" | "femme" | "telescope"

""")
sent = "le garçon regarde la femme avec le telescope".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)


for tree in rd_parser.nbest_parse(sent):
    print tree.draw()


print len(rd_parser.nbest_parse(sent))