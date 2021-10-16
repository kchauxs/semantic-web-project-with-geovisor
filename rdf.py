# import libs
import json
import rdflib

# load triplestore


def start():
    g = rdflib.graph.ConjunctiveGraph()
    g.parse('ontologie/jenaV3.owl', format="xml")
    return g

# sparql queries


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


def listeParcs1(g):
    qres = g.query("""

        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Low_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)


def listeParcs2(g):
    qres = g.query("""

        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Medium_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)


def listeParcs3(g):
    qres = g.query("""

        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Portion_Arbres_Hauts ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :High_Fresh_Parks .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Portion_Arbres_Hauts ?Portion_Arbres_Hauts .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)


def listeActiv(g):
    qres = g.query("""

        SELECT ?Name ?Geo_Json ?Coord ?Adress ?Arrondissements ?Description ?Payant ?Horaires_Lundi ?Horaires_Mardi ?Horaires_Mercredi ?Horaires_Jeudi ?Horaires_Vendredi ?Horaires_Samedi  ?Horaires_Dimanche
        WHERE {
            ?s rdf:type :Fresh_place .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Adress ?Adress .
            ?s :Arrondissements ?Arrondissements .
            ?s :Description ?Description .
            ?s :Payant ?Payant .
            ?s :Horaires_Lundi ?Horaires_Lundi .
            ?s :Horaires_Mardi ?Horaires_Mardi .
            ?s :Horaires_Mercredi ?Horaires_Mercredi .
            ?s :Horaires_Jeudi ?Horaires_Jeudi .
            ?s :Horaires_Vendredi ?Horaires_Venredi .
            ?s :Horaires_Samedi ?Horaires_Samedi .
            ?s :Horaires_Dimanche ?Horaires_Dimanche .
            }""")
    return(qres)


def listeVelo(g):
    qres = g.query("""

        SELECT ?Name ?Geo_Json ?Coord  ?Arrondissements ?BiDirectional ?Sens_circulation
        WHERE {
            ?s rdf:type :bicycle_path .
            ?s :Name ?Name .
            ?s :Geo_Json ?Geo_Json .
            ?s :Coord ?Coord .
            ?s :Arrondissements ?Arrondissements .
            ?s :BiDirectional ?BiDirectional .
            ?s :Sens_circulation ?Sens_circulation .
            }""")
    return(qres)

# to JSON


def arrayParks(qres):
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


def arrayEvent(qres):
    array = []
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Adresse": results[3],
            "Arrondissements": results[4],
            "Description": results[5],
            "Payant": results[6],
            "Horaires_Lundi": results[7],
            "Horaires_Mardi": results[8],
            "Horaires_Mercredi": results[9],
            "Horaires_Jeudi": results[10],
            "Horaires_Vendredi": results[11],
            "Horaires_Samedi": results[12],
            "Horaires_Dimanche": results[13],
        }
        )
    return array


def arrayVelo(qres):
    array = []
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Arrondissements": results[3],
            "Bidirectionnel": results[4],
            "Sens de circulation": results[5],
        })
    return array


def arrayParcs(qres):
    array = []
    for results in qres:
        array.append({
            "Name": results[0],
            "Geo_Json": json.loads(results[1]),
            "Coord": [float(coord) for coord in results[2].split(",")],
            "Adresse": results[3],
            "Arrondissements": results[4],
            "Description": results[5],
            "Portion d'arbres hauts": results[6],
            "Horaires_Lundi": results[7],
            "Horaires_Mardi": results[8],
            "Horaires_Mercredi": results[9],
            "Horaires_Jeudi": results[10],
            "Horaires_Vendredi": results[11],
            "Horaires_Samedi": results[12],
            "Horaires_Dimanche": results[13],
        })
    return(array)


def returnJson(type, g):
    if type == "parks":
        return json.dumps(arrayParks(layerIndividualsList(g, "parques")))

    if type == "warehouse":
        return json.dumps(arrayParks(layerIndividualsList(g, "almacen")) + arrayParks(layerIndividualsList(g, "galeria")))

    if type == "activities":
        return json.dumps(arrayParks(layerIndividualsList(g, "balneario")) + arrayParks(layerIndividualsList(g, "deporte")))

    if type == "food_and_drink":
        return json.dumps(arrayParks(layerIndividualsList(g, "bar")) + arrayParks(layerIndividualsList(g, "restaurante")))

    if type == "culture_and_religion":
        return json.dumps(arrayParks(layerIndividualsList(g, "iglesia")) + arrayParks(layerIndividualsList(g, "museo")))

    if type == "transport":
        return json.dumps(arrayParks(layerIndividualsList(g, "aeropuerto")) + arrayParks(layerIndividualsList(g, "terminal")))

    if type == "hotel_and_lodging":
        return json.dumps(arrayParks(layerIndividualsList(g, "hospedaje")) + arrayParks(layerIndividualsList(g, "hotel")))

    if type == "financial_entities":
        return json.dumps(arrayParks(layerIndividualsList(g, "banco")) + arrayParks(layerIndividualsList(g, "cajero")))


if __name__ == "__main__":
    g = start()
    print(returnJson("food_and_drink", g))
