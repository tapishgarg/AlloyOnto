import xml.etree.ElementTree as ET
from xml.dom import minidom
from periodictable import elements
from pymatgen import Element as El

Elements = list()
gen = (el for el in elements if (el.number < 108 and el.number > 0))
for el in gen:
    myel = El(el.symbol)
    Elements.append([myel.long_name])
len(Elements)

# tree = ET.parse("/Users/tapishgarg/Documents/BTP-Ontologies/AlloyOnto6XML.owl")

mydoc = minidom.parse("/Users/tapishgarg/Documents/BTP-Ontologies/Extending_AlloyOnto/AlloyOnto2.owl")
individuals = mydoc.getElementsByTagName("owl:NamedIndividual")

num_of_individuals = len(individuals)
print(num_of_individuals)
for i in range(num_of_individuals):
    current_iri = individuals[i].attributes['rdf:about'].value
    print(current_iri)
    if current_iri.split("#")[0] == "http://semantic.iitm.ac.in/AlloyOnto/Elements" or current_iri.split("#")[1] in Elements:
        continue
    individual_name = current_iri.split("#")[1]
    individual = individuals[i].getElementsByTagName("rdf:type")
    class_iri = individual[0].attributes['rdf:resource'].value
    individual_base_iri = class_iri.split("#")[0]
    new_iri = individual_base_iri + '#' + individual_name
    print(new_iri)
    fin = open("/Users/tapishgarg/Documents/BTP-Ontologies/Extending_AlloyOnto/AlloyOnto3.owl", "rt")
    data = fin.read()
    data = data.replace(current_iri, new_iri)
    fin.close()
    fin = open("/Users/tapishgarg/Documents/BTP-Ontologies/Extending_AlloyOnto/AlloyOnto3.owl", "wt")
    fin.write(data)
    fin.close()

print("Processing Complete!")
    
    

# fin = open("/Users/tapishgarg/Documents/BTP-Ontologies/AlloyOnto6XML.owl", "rt")
# print(fin.read())

# rdfs = mydoc.getElementsByTagName("rdf:type")
# print(rdfs[6].attributes['rdf:resource'].value)

# with open("/Users/tapishgarg/Documents/BTP-Ontologies/AlloyOnto8XML.owl", "w") as fs:
#     fs.write(mydoc.toxml())
#     fs.close()


