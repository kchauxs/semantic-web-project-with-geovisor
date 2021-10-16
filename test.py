import rdflib

g = rdflib.graph.ConjunctiveGraph()
g.parse('ontologie/jenaV4.owl', format="xml")

qres = g.query("""
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix : <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>
    SELECT DISTINCT ?nombre ?direccion ?horario ?calificacion ?comentarios ?o
     WHERE {
     ?s rdf:type ?object.
  	 ?s :nombre ?nombre .
     ?s :direccion ?direccion .
  	 ?s :horario ?horario .
     ?s :calificacion ?calificacion .
     ?s :comentarios ?comentarios .
    optional { ?s :brindan ?o } .
    optional { ?s :esta ?o } .
    optional { ?s :posee ?o } .
    optional { ?s :Ttiene ?o } .
    FILTER (REGEX(str(?object),"aerop","i")).
}
""")


for results in qres:
    print(results, end='\n\n')
