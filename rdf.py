# import libs
import json
import rdflib

# load triplestore
def start():
    g = rdflib.graph.ConjunctiveGraph()
    g.parse('ontologie/jenaV4.owl', format="xml")
    return g

# sparql queries
def layerList(g):
    qres = g.query("""
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix : <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>

        SELECT DISTINCT ?subject
	        WHERE { 
            ?subject rdfs:subClassOf :puntos_interes.
	        ?object rdf:type owl:Class
        }""")
    return(qres)


def layerIndividualsList(g, class_name=None):
    qres = g.query("""
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix : <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>
        select ?nombre ?Geo_Json ?direccion ?horario ?comentarios ?calificacion
        where {
            ?s rdf:type :% .
            ?s :nombre ?nombre .
            ?s :Geo_Json ?Geo_Json .
            ?s :direccion ?direccion .
            ?s :horario ?horario .
            ?s :comentarios ?comentarios .
            ?s :calificacion ?calificacion .
        }
            """.replace("%", class_name))
    return(qres)


def searcher(g, params=None):
    qres = g.query("""
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix : <http://www.semanticweb.org/root/ontologies/2021/9/untitled-ontology-14#>
    SELECT DISTINCT ?nombre ?direccion ?horario ?Geo_Json ?calificacion ?comentarios ?o
     WHERE {
        ?s rdf:type ?object.
  	    ?s :nombre ?nombre .
        ?s :direccion ?direccion .
  	    ?s :horario ?horario .
        ?s :Geo_Json ?Geo_Json .
        ?s :calificacion ?calificacion .
        ?s :comentarios ?comentarios .
        optional { ?s :brindan ?o } .
        optional { ?s :esta ?o } .
        optional { ?s :posee ?o } .
        optional { ?s :Ttiene ?o } .
        FILTER (REGEX(str(?object),"%","i")).
    }
    """.replace("%", params))
    return(qres)


def arrayIndividual(qres):
    array = []
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Address":  results[2],
            "Schedule": results[3],
            "Comments": results[4],
            "Qualification": results[5],

        })
    return array


def arrayLayerList(qres):
    array = []
    for results in qres:
        array.append({
            "Name": results[0].split('#')[1]
        })
    return array


def arraySearcher(qres):
    array = []
    for results in qres:
        array.append({
            "Suject": results[0],
            "Address":  results[1],
            "Schedule": results[2],
            "Geo_Json": json.loads(results[3]),
            "Qualification": results[4],
            "Comments": results[5],
            "Object": None if results[6] == None else results[6].split('#')[1].replace('_', ' ')

        })
    return array


def returnJson(type, g, params=None):
    if type == "parks":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "parques")))

    if type == "warehouse":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "almacen")) + arrayIndividual(layerIndividualsList(g, "galeria")))

    if type == "activities":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "balneario")) + arrayIndividual(layerIndividualsList(g, "deporte")))

    if type == "food_and_drink":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "bar")) + arrayIndividual(layerIndividualsList(g, "restaurante")))

    if type == "culture_and_religion":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "iglesia")) + arrayIndividual(layerIndividualsList(g, "museo")))

    if type == "transport":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "aeropuerto")) + arrayIndividual(layerIndividualsList(g, "terminal")))

    if type == "hotel_and_lodging":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "hospedaje")) + arrayIndividual(layerIndividualsList(g, "hotel")))

    if type == "financial_entities":
        return json.dumps(arrayIndividual(layerIndividualsList(g, "banco")) + arrayIndividual(layerIndividualsList(g, "cajero")))

    if type == "searcher":
        return json.dumps(arraySearcher(searcher(g, params)))

    if type == "layer":
        return json.dumps(arrayLayerList(layerList(g)))


if __name__ == "__main__":
    g = start()
    print(returnJson("layer", g))
