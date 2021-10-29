# -*- coding: utf-8 -*-
"""Task09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DBz_xNg8D3NNHVqFdmD6xK4dJYZ7dyiV

**Task 09: Data linking**
"""

#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials/"

from rdflib import Graph, Namespace, Literal, URIRef, OWL, RDF

g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

"""Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos."""

OWL = Namespace("http://www.w3.org/2002/07/owl#")
NS3 = Namespace("http://data.three.org#")
NS4 = Namespace("http://data.four.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

for s3, p3, o3 in g1.triples((None, RDF.type, NS3.Person)):
  for s4, p4, o4 in g2.triples((None, RDF.type, NS4.Person)):
    if (g1.value(subject=s3, predicate=VCARD.Given, object=None) == g2.value(subject=s4, predicate=VCARD.Given, object=None) and
       g1.value(subject=s3, predicate=VCARD.Family, object=None) == g2.value(subject=s4, predicate=VCARD.Family, object=None)):
      g3.add((s3, OWL.sameAs, s4))

for s, p, o in g3:
  print(s, p, o)
