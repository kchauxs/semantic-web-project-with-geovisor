#import libs
import json
import rdflib

# load triplestore


def start():
    g = rdflib.Graph()
    g.parse('turismo_v2.owl', format="xml")
    return g

# sparql queries


def listeClass(g):
    qres = g.query("""
        SELECT ?Coordenadas ?Geo_Json ?Nombre ?Descripcion
        WHERE {
            
                ?s rdf:type :deporte .
                ?s :Coordenadas ?Coordenadas .
                ?s :Geo_Json ?Geo_Json .
                ?s :Nombre ?Nombre .
                ?s :Descripcion ?Descripcion .
            

            }
            """)
    return(qres)


""" 
def listeClass(g):
    qres = g.query(
        SELECT ?Coordenadas ?Geo_Json ?Nombre ?Descripción
        WHERE {
            ?s rdf:type :deporte .
            ?o rdf:type :tiene_disponibilidad .
            ?p rdf:type :horario_completo .
            ?s :Coordenadas ?Coordenadas .
            ?s :Geo_Json ?Geo_Json .
            ?s :Nombre ?Nombre .
            ?s :Descripción ?Descripción .
            })
    return(qres)
 """
# to JSON


""" def arrayClass(qres):
    array = []
    for results in qres:

        array.append({
            "Coord": [float(coord) for coord in results[0].split(",")],
            "Geo_Json": json.loads(results[1]),
            "Name": results[2],
            "Descripcion": results[3],
        })
    return array


def returnJson(type, g):
    if type == "test":
        return json.dumps(arrayClass(listeClass(g)))


if __name__ == "__main__":
    g = start()
    print(returnJson("test", g))
 """

import json
import rdflib

# load triplestore


g = rdflib.graph.ConjunctiveGraph()
g.parse('jena.owl', format="xml")

qres = g.query("""
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix : <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#> 

    select ?nombre ?Geo_Json ?direccion ?horario ?comentarios ?calificacion
    where {
        ?s rdf:type :parques .
        ?s :nombre ?nombre .
        ?s :Geo_Json ?Geo_Json .
        ?s :direccion ?direccion .
        ?s :horario ?horario .
        ?s :comentarios ?comentarios .
        ?s :calificacion ?calificacion .
    }""")


for results in qres:
    print(results, end='\n\n')


"""
    PREFIX data: <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>
    SELECT ?nombre 
        WHERE {
            ?s rdf:type :parques .
            ?s :nombre ?nombre 
            }
"""


"""
PREFIX data: <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>

SELECT ?nombre ?calificacion ?comentarios ?direccion ?Geo_Json ?horario
where{ 
  	?parque data:nombre ?nombre .
  	?parque data:calificacion ?calificacion .
    ?parque data:comentarios ?comentarios .
  	?parque data:direccion ?direccion .
  	?parque data:Geo_Json ?Geo_Json .
    ?parque data:horario ?horario         
}
"""
"""
SELECT DISTINCT ?subject ?object
	WHERE { ?subject rdf:type owl:Class }
"""
