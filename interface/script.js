//create the map
var map = L.map('map').setView([1.6184774183504775, -75.60791370550324], 15); //start map obj
var overlayMaps = {};

var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', { //create the layer
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
});
map.addLayer(osmLayer);


//L.marker([48.833, 2.333]).addTo(map).bindPopup("<b>Hello world!</b><br>I am a popup.");//add first marker

//display meteo on map click
var popup = L.popup();
async function onMapClick(e) {
    //console.log(e.latlng)
    //get weather
    API_METEO = 'http://api.openweathermap.org/data/2.5/weather?lat=' + e.latlng.lat + '&lon=' + e.latlng.lng + '&appid=0c0c9aa8bb23a8054260d263e56fc1cc';
    const responseM = await fetch(API_METEO);
    const dataM = await responseM.json();
    //console.log(dataM)
    //get air quality
    API_AIR = "https://api.waqi.info/feed/geo:" + e.latlng.lat + ";" + e.latlng.lng + "/?token=3ea0f358523452559d46c9d0c715e7908e9d993c"
    const responseA = await fetch(API_AIR);
    const dataA = await responseA.json();
    //console.log(dataA)
    const message = "<b>" + dataM.name + "</b><br>Temperatura : " + ((dataM.main.temp - 273).toFixed(1)) + "°C<br>Clima : " + dataM.weather[0].description + "<br>Índice de calidad del aire  : " + dataA.data.aqi
    popup
        .setLatLng(e.latlng)
        .setContent(message)
        .openOn(map);
}
map.on('click', onMapClick);





const formulario = document.querySelector('#formulario');
const boton = document.querySelector('#boton');
const resultado = document.querySelector('#resultado');
const sujecto = document.querySelector('#sujecto');
let marker = []


function markerDelAgain(marker) {
    try {
        for (i = 0; i < marker.length; i++) {
            map.removeLayer(marker[i]);
        }
    } catch (error) {
        return
    }
}


async function filtrar() {
    markerDelAgain(marker)
    const texto = formulario.value.toLowerCase();
    const response = await fetch(`http://127.0.0.1:5000/searcher?param=${texto}`, { mode: 'cors' });
    const data = await response.json();
    let nameSubjet = ""
    /* let padlock = false */

    resultado.innerHTML = '';
    sujecto.innerText = '';

    if (texto.trim() === '') {
        resultado.innerHTML += ` <li class="list-group-item list-group-item-danger">Producto no encontrado...</li>`
        return
    }

    for (let item of data) {
        let { Suject, Schedule, Address, Qualification, Object } = item
        //Object == null ? Suject : Object
        resultado.innerHTML += `
        <li class="list-group-item"><b>Sitio: </b>${Suject} - <b>Objeto: </b>${Object} - <b>   Dirección: </b>${Address} - <b>Calificación: </b>${Qualification} - <b>Horario: </b>${Schedule}</li>`
        let [long, lat] = item.Geo_Json.coordinates
        let textPopup = `
        <b>${Object == null ? Suject : Object}</b>
        `

        /*  if (!padlock) {
             marker.push(L.marker([long, lat], { icon: blueIcon }).addTo(map).bindPopup(textPopup))
         }
  */
        if (Object != null) {
            nameSubjet = Suject
            /* padlock = true */
        }
        marker.push(L.marker([long, lat], { icon: blueIcon }).addTo(map).bindPopup(textPopup))

    };

    /* if (nameSubjet) {
        sujecto.innerText = nameSubjet
    } */
    formulario.value = "";
}

boton.addEventListener('click', filtrar);
//formulario.addEventListener('keyup', filtrar);

async function getIndividuals(nomCouche) {
    //console.log("loading " + nomCouche)
    const APIPython = "http://127.0.0.1:5000/" + nomCouche;
    const response = await fetch(APIPython, { mode: 'cors' });
    const pythonJSON = await response.json();

    //console.log("displaying " + nomCouche)
    //console.log(pythonJSON)
    let listeCouche = []
    for (let i = 0; i < pythonJSON.length; i++) {
        let { Geo_Json, Name, Comments, Qualification, Address, Schedule } = pythonJSON[i]
        let [long, lat] = Geo_Json.coordinates

        let textPopup = `
        <b>${Name}</b>
        <br>
        Reseñas: ${Comments}
        <br>
        Calificacion: ${Qualification}
        <br>
        Dirección: ${Address}
        <br>
        Horario: ${Schedule}
        `

        let iconObj = getColorIcon(nomCouche)
        listeCouche.push(L.marker([long, lat], { icon: iconObj })
            .bindPopup(textPopup)
            .on('dblclick', ondbClick));
    };
    let couche = L.layerGroup(listeCouche);
    overlayMaps[nomCouche.replace("_", " ").toUpperCase()] = couche;
}

function ondbClick(e) {
    alert("TEST");
}

function getColorIcon(nomCouche) {
    let iconObj = goldIcon;
    if (nomCouche == "parques") {
        iconObj = greenIcon;
    }
    if (nomCouche == "compras") {
        iconObj = goldIcon;
    }
    if (nomCouche == "actividades") {
        iconObj = blueIcon;
    }
    if (nomCouche == "comidas_bebidas") {
        iconObj = orangeIcon;
    }
    if (nomCouche == "cultura_religion") {
        iconObj = violeIcon;
    }
    if (nomCouche == "transporte") {
        iconObj = geyIcon;
    }
    if (nomCouche == "Hoteles_Hospedajes") {
        iconObj = redIcon;
    }
    if (nomCouche == "entidades_financieras") {
        iconObj = blackIcon;
    }
    return iconObj
}

//ICON
var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var goldIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-gold.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var blueIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var orangeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var violeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});


var geyIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-grey.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var blackIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-black.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});



async function getLayers() {
    const APIPython = "http://127.0.0.1:5000/layer";
    const response = await fetch(APIPython, { mode: 'cors' });
    return await response.json();
}

async function mainGet() {
    let layer = await getLayers()

    for (let index = 0; index < layer.length; index++) {
        await getIndividuals(layer[index].Name);
    }

    /* await getIndividuals("Parques", "parks");
    await getIndividuals("Compras", "warehouse");
    await getIndividuals("Actividades", "activities");
    await getIndividuals("Comida y Bebidas", "food_and_drink");
    await getIndividuals("Cultura y Religion", "culture_and_religion");
    await getIndividuals("Transporte", "transport");
    await getIndividuals("Hoteles y Hospedaje", "hotel_and_lodging");
    await getIndividuals("Entidades Financieras", "financial_entities"); */

}
mainGet().then(res => {
    L.control.layers({}, overlayMaps).addTo(map);

});
