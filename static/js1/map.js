require([
    "esri/Map",
    "esri/views/MapView",
    "esri/widgets/BasemapToggle",
    // "esri/widgets/BasemapGallery",
    "esri/widgets/Search",
    "esri/layers/FeatureLayer"
], function(Map, MapView, BasemapToggle, Search, FeatureLayer) {
    var map = new Map({
    // basemap: "topo-vector"
    basemap: "streets-navigation-vector"
    });

    // longitude, latitude
    var view = new MapView( { container: "viewDiv", map: map, center: [-117.713814,34.101379], zoom: 11 });

    var basemapToggle = new BasemapToggle({ view: view, nextBasemap: "satellite" });
    view.ui.add(basemapToggle, "bottom-right");

    // Load vector tile basemaps
    // var basemapGallery = new BasemapGallery({
    //     view: view,
    //     source: {
    //         portal: {
    //         url: "https://www.arcgis.com",
    //         useVectorBasemaps: true
    //       }
    //     }
    //   });
    // view.ui.add(basemapGallery, "top-right");

    // Search widget
    var search = new Search({
        view: view
    });
    view.ui.add(search, "top-right");




    // // Add the layer to the map
    // var trailsLayer = new FeatureLayer({
    //     url: "https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services/Trailheads/FeatureServer/0",
    //   });
    //
    // map.add(trailsLayer); // Optionally add layer to map
    //
    // // Add the trailheads as a search source
    // search.sources.push({
    //     layer: trailsLayer,
    //     searchFields: ["TRL_NAME"],
    //     displayField: "TRL_NAME",
    //     exactMatch: false,
    //     outFields: ["TRL_NAME", "PARK_NAME"],
    //     resultGraphicEnabled: true,
    //     name: "Trailheads",
    //     placeholder: "Example: Medea Creek Trail",
    //   });

    // // Trailheads feature layer (points)
    // var trailheadsLayer = new FeatureLayer({ url: "https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services/Trailheads/FeatureServer/0" });
    // map.add(trailheadsLayer);
    //
    // // Trails feature layer (lines)
    // var trailsLayer = new FeatureLayer({ url: "https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services/Trails/FeatureServer/0"});
    // map.add(trailsLayer, 0);
    //
    // // Parks and open spaces (polygons)
    // var parksLayer = new FeatureLayer({ url: "https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services/Parks_and_Open_Space/FeatureServer/0"});
    // map.add(parksLayer, 0);


    // // too many data
    // var crimeData = new FeatureLayer( {
    //     url: "https://services.arcgis.com/q3Zg9ERurv23iysr/arcgis/rest/services/Crime_Data_from_2010_to_Present/FeatureServer/0?token=4r1UTakwHQUdQh8I4xRfVipZnGsL23bFhUmZXgODNbT36M-y9n_76wBt3uqTnjrQNSjAdxhNQqdGRLwJC_2yRCh18eayJkO1InwHaWmQEVQrrXMO2CFLbUHVJtOz32nJw0IOydVXsjSBahIqhZeU6zwPDvqL4b5xErIcWanS4ySapEIWTz1KLUkPiWr5bs7qAFAbcfI2LAJrl_vWxM_H7mnrAnOIB0i8lPEkgfBehtfjGbCWOYEK2PGyAM84XwYg",
    //     outFields: ["AREA","Crm_Cd"],
    //     popupTemplate: {  // Enable a popup
    //       title: "Crime in {AREA}", // Show attribute value
    //       content: "Crime Commited: {Crm_Cd}."  // Display text in pop-up
    //     }
    //
    // });
    // map.add(crimeData, 0);



2




    // --------------------------------------------------------------------------------
    // view on click function


    view.on("click", function(evt){
        search.clear();
        view.popup.clear();
        if (search.activeSource) {
            var geocoder = search.activeSource.locator; // World geocode service
            var params = {
                location: evt.mapPoint
            };
            geocoder.locationToAddress(params)
                .then(function(response) { // Show the address found
                    var address = response.address;
                    showPopup(address, evt.mapPoint);
                    },
                    function(err) { // Show no address found
                    showPopup("No address found.", evt.mapPoint);
                    });
            }
        });


    function showPopup(address, pt) {
        view.popup.open({
            title:  + Math.round(pt.longitude * 100000)/100000 + "," + Math.round(pt.latitude * 100000)/100000,
            content: address,
            location: pt
            });
    }



});




