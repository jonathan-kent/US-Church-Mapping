require([
        "esri/Map",
        "esri/layers/CSVLayer",
        "esri/views/MapView",
        "esri/widgets/Legend"],
function (Map, CSVLayer, MapView, Legend) {
  var baptistCSV = "http://jonathan-kent.com/US_religion_mapping/baptist.csv";
  var baptistRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(255, 179, 179, 0)", ratio: 0 },
      { color: "#ff0000", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const baptistLayer = new CSVLayer({
    title: "Baptist",
    url: baptistCSV,
    renderer: baptistRenderer
  });

  var methodistCSV = "http://jonathan-kent.com/US_religion_mapping/methodist.csv";
  var methodistRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(255, 208, 179, 0)", ratio: 0 },
      { color: "#ff6200", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const methodistLayer = new CSVLayer({
    title: "Methodist",
    url: methodistCSV,
    renderer: methodistRenderer
  });

  var presbyterianCSV = "http://jonathan-kent.com/US_religion_mapping/presbyterian.csv";
  var presbyterianRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(255, 236, 179, 0)", ratio: 0 },
      { color: "#ffc300", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const presbyterianLayer = new CSVLayer({
    title: "Presbyterian",
    url: presbyterianCSV,
    renderer: presbyterianRenderer
  });

  var episcopalCSV = "http://jonathan-kent.com/US_religion_mapping/episcopal.csv";
  var episcopalRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(245, 255, 179, 0)", ratio: 0 },
      { color: "#d9ff00", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const episcopalLayer = new CSVLayer({
    title: "Episcopal",
    url: episcopalCSV,
    renderer: episcopalRenderer
  });

  var catholicCSV = "http://jonathan-kent.com/US_religion_mapping/catholic.csv";
  var catholicRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(214, 255, 179, 0)", ratio: 0 },
      { color: "#77ff00", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const catholicLayer = new CSVLayer({
    title: "Catholic",
    url: catholicCSV,
    renderer: catholicRenderer
  });

  var orthodoxCSV = "http://jonathan-kent.com/US_religion_mapping/orthodox.csv";
  var orthodoxRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(187, 255, 179, 0)", ratio: 0 },
      { color: "#15ff00", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const orthodoxLayer = new CSVLayer({
    title: "Orthodox",
    url: orthodoxCSV,
    renderer: orthodoxRenderer
  });

  var adventistCSV = "http://jonathan-kent.com/US_religion_mapping/adventist.csv";
  var adventistRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(179, 255, 201, 0)", ratio: 0 },
      { color: "#00ff4c", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const adventistLayer = new CSVLayer({
    title: "Adventist",
    url: adventistCSV,
    renderer: adventistRenderer
  });

  var mennoniteCSV = "http://jonathan-kent.com/US_religion_mapping/mennonite.csv";
  var mennoniteRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(179, 255, 231, 0)", ratio: 0 },
      { color: "#00ffae", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const mennoniteLayer = new CSVLayer({
    title: "Mennonite",
    url: mennoniteCSV,
    renderer: mennoniteRenderer
  });

  var messianicCSV = "http://jonathan-kent.com/US_religion_mapping/messianic.csv";
  var messianicRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(179, 250, 255, 0)", ratio: 0 },
      { color: "#00eeff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const messianicLayer = new CSVLayer({
    title: "Messianic Judaism",
    url: messianicCSV,
    renderer: messianicRenderer
  });

  var reformedCSV = "http://jonathan-kent.com/US_religion_mapping/reformed.csv";
  var reformedRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(179, 221, 255, 0)", ratio: 0 },
      { color: "#008cff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const reformedLayer = new CSVLayer({
    title: "Reformed",
    url: reformedCSV,
    renderer: reformedRenderer
  });

  var calvinistCSV = "http://jonathan-kent.com/US_religion_mapping/calvinist.csv";
  var calvinistRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(179, 190, 255, 0)", ratio: 0 },
      { color: "#002aff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const calvinistLayer = new CSVLayer({
    title: "Calvinist",
    url: calvinistCSV,
    renderer: calvinistRenderer
  });

  var lutheranCSV = "http://jonathan-kent.com/US_religion_mapping/lutheran.csv";
  var lutheranRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(195, 179, 255, 0)", ratio: 0 },
      { color: "#3700ff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const lutheranLayer = new CSVLayer({
    title: "Lutheran",
    url: lutheranCSV,
    renderer: lutheranRenderer
  });

  var pentecostalCSV = "http://jonathan-kent.com/US_religion_mapping/pentecostal.csv";
  var pentecostalRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(224, 179, 255, 0)", ratio: 0 },
      { color: "#9900ff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const pentecostalLayer = new CSVLayer({
    title: "Pentecostal",
    url: pentecostalCSV,
    renderer: pentecostalRenderer
  });

  var protestantCSV = "http://jonathan-kent.com/US_religion_mapping/protestant.csv";
  var protestantRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(254, 179, 255, 0)", ratio: 0 },
      { color: "#fb00ff", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const protestantLayer = new CSVLayer({
    title: "Protestant",
    url: protestantCSV,
    renderer: protestantRenderer
  });

  var quakerCSV = "http://jonathan-kent.com/US_religion_mapping/quaker.csv";
  var quakerRenderer = {
    type: "heatmap",
    colorStops: [
      { color: "rgba(255, 176, 226, 0)", ratio: 0 },
      { color: "#ff00a2", ratio: 1 }
    ],
    maxPixelIntensity: 25,
    minPixelIntensity: 0
  };


  const quakerLayer = new CSVLayer({
    title: "Quaker",
    url: quakerCSV,
    renderer: quakerRenderer
  });


  const map = new Map({
    basemap: "dark-gray-vector",
    layers: [protestantLayer, baptistLayer, pentecostalLayer, methodistLayer,
            catholicLayer, lutheranLayer, presbyterianLayer, episcopalLayer,
            adventistLayer, orthodoxLayer, reformedLayer, mennoniteLayer,
            quakerLayer, messianicLayer, calvinistLayer]
  });

  const view = new MapView({
    container: "viewDiv",
    center: [-90.90614554667947, 38.44811777828268],
    zoom: 4.35,
    map: map
  });

  // layer toggles

  var protestantLayerToggle = document.getElementById("protestantLayer");
  protestantLayerToggle.addEventListener("change", function () {
    protestantLayer.visible = protestantLayerToggle.checked;
  });
  var baptistLayerToggle = document.getElementById("baptistLayer");
  baptistLayerToggle.addEventListener("change", function () {
    baptistLayer.visible = baptistLayerToggle.checked;
  });
  var methodistLayerToggle = document.getElementById("methodistLayer");
  methodistLayerToggle.addEventListener("change", function () {
    methodistLayer.visible = methodistLayerToggle.checked;
  });
  var pentecostalLayerToggle = document.getElementById("pentecostalLayer");
  pentecostalLayerToggle.addEventListener("change", function () {
    pentecostalLayer.visible = pentecostalLayerToggle.checked;
  });
  var catholicLayerToggle = document.getElementById("catholicLayer");
  catholicLayerToggle.addEventListener("change", function () {
    catholicLayer.visible = catholicLayerToggle.checked;
  });
  var lutheranLayerToggle = document.getElementById("lutheranLayer");
  lutheranLayerToggle.addEventListener("change", function () {
    lutheranLayer.visible = lutheranLayerToggle.checked;
  });
  var presbyterianLayerToggle = document.getElementById("presbyterianLayer");
  presbyterianLayerToggle.addEventListener("change", function () {
    presbyterianLayer.visible = presbyterianLayerToggle.checked;
  });
  var episcopalLayerToggle = document.getElementById("episcopalLayer");
  episcopalLayerToggle.addEventListener("change", function () {
    episcopalLayer.visible = episcopalLayerToggle.checked;
  });
  var adventistLayerToggle = document.getElementById("adventistLayer");
  adventistLayerToggle.addEventListener("change", function () {
    adventistLayer.visible = adventistLayerToggle.checked;
  });
  var orthodoxLayerToggle = document.getElementById("orthodoxLayer");
  orthodoxLayerToggle.addEventListener("change", function () {
    orthodoxLayer.visible = orthodoxLayerToggle.checked;
  });
  var reformedLayerToggle = document.getElementById("reformedLayer");
  reformedLayerToggle.addEventListener("change", function () {
    reformedLayer.visible = reformedLayerToggle.checked;
  });
  var mennoniteLayerToggle = document.getElementById("mennoniteLayer");
  mennoniteLayerToggle.addEventListener("change", function () {
    mennoniteLayer.visible = mennoniteLayerToggle.checked;
  });
  var quakerLayerToggle = document.getElementById("quakerLayer");
  quakerLayerToggle.addEventListener("change", function () {
    quakerLayer.visible = quakerLayerToggle.checked;
  });
  var messianicLayerToggle = document.getElementById("messianicLayer");
  messianicLayerToggle.addEventListener("change", function () {
    messianicLayer.visible = messianicLayerToggle.checked;
  });
  var calvinistLayerToggle = document.getElementById("calvinistLayer");
  calvinistLayerToggle.addEventListener("change", function () {
    calvinistLayer.visible = calvinistLayerToggle.checked;
  });

  view.ui.components = [ "attribution" ];
  view.ui.add(titleDiv, "top-left");
  view.ui.add(
    new Legend({
      view: view
    }),
    "bottom-left"
  );

});
