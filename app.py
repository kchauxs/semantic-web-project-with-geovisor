from flask import Flask, request
from flask_cors import CORS
import rdf

# start app
print("[INFO] Starting app: OK")
app = Flask(__name__)
CORS(app)
print("[INFO] App started: OK")

# load database
print("[INFO] Loading RDF database: OK")
g = rdf.start()
print("[INFO] Database loaded: OK")


@app.route('/parks', methods=['GET'])
def fontaines():
    return rdf.returnJson("parks", g)


@app.route('/warehouse', methods=['GET'])
def warehouse():
    return rdf.returnJson("warehouse", g)


@app.route('/activities', methods=['GET'])
def activities():
    return rdf.returnJson('activities', g)


@app.route('/food_and_drink', methods=['GET'])
def food_and_drink():
    return rdf.returnJson("food_and_drink", g)


@app.route('/culture_and_religion', methods=['GET'])
def culture_and_religion():
    return rdf.returnJson("culture_and_religion", g)


@app.route('/transport', methods=['GET'])
def transport():
    return rdf.returnJson("transport", g)


@app.route('/hotel_and_lodging', methods=['GET'])
def hotel_and_lodging():
    return rdf.returnJson("hotel_and_lodging", g)


@app.route('/financial_entities', methods=['GET'])
def financial_entities():
    return rdf.returnJson("financial_entities", g)


@app.route('/searcher')
def searcher():
    param = request.args.get('param')
    #print(rdf.returnJson("searcher", g, param))
    return rdf.returnJson("searcher", g, param)
    # return '''<h1>Param: {}</h1>'''.format(param)


if __name__ == '__main__':
    app.run()
