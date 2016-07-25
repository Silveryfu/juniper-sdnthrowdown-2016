var map;
var lsp_1, lsp_2, lsp_3, lsp_4;
var lsp_5, lsp_6, lsp_7, lsp_8;

var lsp_1_path, lsp_2_path, lsp_3_path, lsp_4_path;
var lsp_5_path, lsp_6_path, lsp_7_path, lsp_8_path;

function initMap() {
  var mapDiv = document.getElementById('map');
  map = new google.maps.Map(mapDiv, {
    center: {lat: 32.789997, lng: -96.77},
    zoom: 5
  });

  set_topo();
  set_marker();  
  set_lsp();
}

function set_marker() {
  var myCenter=new google.maps.LatLng(40.432488, -56.088068);

  var icon_1 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#f1c40f',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_1=new google.maps.Marker({
  position:myCenter,
  icon: icon_1,
  label: "1"
  });

  marker_1.addListener('click', function() {
      add_lsp_1();
  });

  marker_1.addListener('dblclick', function() {
      remove_lsp_1();
  });

  marker_1.setMap(map);

  function add_lsp_1() {
     lsp_1.setMap(map);
  }

  function remove_lsp_1() {
     lsp_1.setMap(null);
  }


  var myCenter=new google.maps.LatLng(38.432488, -56.088068);

  var icon_2 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#f39c12',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_2=new google.maps.Marker({
  position:myCenter,
  icon: icon_2,
  label: "2"
  });

  marker_2.addListener('click', function() {
      add_lsp_2();
  });

  marker_2.addListener('dblclick', function() {
      remove_lsp_2();
  });

  marker_2.setMap(map);

  function add_lsp_2() {
     lsp_2.setMap(map);
  }

  function remove_lsp_2() {
     lsp_2.setMap(null);
  }

  var myCenter=new google.maps.LatLng(36.432488, -56.088068);

  var icon_3 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#e67e22',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_3=new google.maps.Marker({
  position:myCenter,
  icon: icon_3,
  label: "3"
  });

  marker_3.addListener('click', function() {
      add_lsp_3();
  });

  marker_3.addListener('dblclick', function() {
      remove_lsp_3();
  });

  marker_3.setMap(map);

  function add_lsp_3() {
     lsp_3.setMap(map);
  }

  function remove_lsp_3() {
     lsp_3.setMap(null);
  }

  var myCenter=new google.maps.LatLng(34.432488, -56.088068);

  var icon_4 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#d35400',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_4=new google.maps.Marker({
  position:myCenter,
  icon: icon_4,
  label: "4"
  });

  marker_4.addListener('click', function() {
      add_lsp_4();
  });

  marker_4.addListener('dblclick', function() {
      remove_lsp_4();
  });

  marker_4.setMap(map);

  function add_lsp_4() {
     lsp_4.setMap(map);
  }

  function remove_lsp_4() {
     lsp_4.setMap(null);
  }

  var myCenter=new google.maps.LatLng(32.432488, -56.088068);

  var icon_5 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#e74c3c',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_5=new google.maps.Marker({
  position:myCenter,
  icon: icon_5,
  label: "5"
  });

  marker_5.addListener('click', function() {
      add_lsp_5();
  });

  marker_5.addListener('dblclick', function() {
      remove_lsp_5();
  });

  marker_5.setMap(map);

  function add_lsp_5() {
     lsp_5.setMap(map);
  }

  function remove_lsp_5() {
     lsp_5.setMap(null);
  }

  var myCenter=new google.maps.LatLng(30.432488, -56.088068);

  var icon_6 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#c0392b',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_6=new google.maps.Marker({
  position:myCenter,
  icon: icon_6,
  label: "6"
  });

  marker_6.addListener('click', function() {
      add_lsp_6();
  });

  marker_6.addListener('dblclick', function() {
      remove_lsp_6();
  });

  marker_6.setMap(map);

  function add_lsp_6() {
     lsp_6.setMap(map);
  }

  function remove_lsp_6() {
     lsp_6.setMap(null);
  }

  var myCenter=new google.maps.LatLng(28.432488, -56.088068);

  var icon_7 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#3498db',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_7=new google.maps.Marker({
  position:myCenter,
  icon: icon_7,
  label: "7"
  });

  marker_7.addListener('click', function() {
      add_lsp_7();
  });

  marker_7.addListener('dblclick', function() {
      remove_lsp_7();
  });

  marker_7.setMap(map);

  function add_lsp_7() {
     lsp_7.setMap(map);
  }

  function remove_lsp_7() {
     lsp_7.setMap(null);
  }

  var myCenter=new google.maps.LatLng(26.432488, -56.088068);

  var icon_8 = {
      path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
      fillColor: '#2980b9',
      fillOpacity: .6,
      strokeWeight: 0,
      // scale: iconSize
  };

  var marker_8=new google.maps.Marker({
  position:myCenter,
  icon: icon_8,
  label: "8"
  });

  marker_8.addListener('click', function() {
      add_lsp_8();
  });

  marker_8.addListener('dblclick', function() {
      remove_lsp_8();
  });

  marker_8.setMap(map);

  function add_lsp_8() {
     lsp_8.setMap(map);
  }

  function remove_lsp_8() {
     lsp_8.setMap(null);
  }
}


function set_lsp() {
  var lsp_weight = 10;

  lsp_1 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#f1c40f',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_1.setMap(null);

  lsp_2 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#f39c12',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_2.setMap(null);

  lsp_3 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#e67e22',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_3.setMap(null);

  lsp_4 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#d35400',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_4.setMap(null);

  lsp_5 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#e74c3c',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_5.setMap(null);

  lsp_6 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#c0392b',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_6.setMap(null);

  lsp_7 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_7.setMap(null);

  lsp_8 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#2980b9',
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight
  });

  lsp_8.setMap(null);
}

function set_topo() {
  var routermap = {
    chicago: {
      center: {lat: 41.878, lng: -87.629}

    },
    newyork: {
      center: {lat: 40.714, lng: -74.005}

    },
    losangeles: {
      center: {lat: 34.052, lng: -118.243}

    },
    dallas: {
      center: {lat: 32.789997, lng: -96.77}

    },
    miami: {
      center: {lat: 25.78, lng: -80.21}

    },
    houston: {
      center: {lat: 29.770002, lng: -95.39}
    },
    tampa: {
      center: {lat: 27.960001, lng: -82.48}
    },
    sanfranciso: {
      center: {lat: 37.79, lng: -122.55}
    }
  };

  for (var router in routermap) {
    // Add the circle for this router to the map.
    var cityCircle = new google.maps.Circle({
      strokeColor: '#16a085',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#16a085',
      fillOpacity: 0.35,
      map: map,
      center: routermap[router].center,
      radius: 100000
    });
  }

  var link_ny_miami = new google.maps.Polyline({
    path: [{lat: 40.714, lng: -74.005}, {lat: 25.78, lng: -80.21}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_ny_miami.setMap(map);

  var link_sf_dallas = new google.maps.Polyline({
    path: [{lat: 37.79, lng: -122.55}, {lat: 32.789997, lng: -96.77}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_sf_dallas.setMap(map);

  var link_sf_chicago = new google.maps.Polyline({
    path: [{lat: 37.79, lng: -122.55}, {lat: 41.878, lng: -87.629}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_sf_chicago.setMap(map);

  var link_sf_la = new google.maps.Polyline({
    path: [{lat: 37.79, lng: -122.55}, {lat: 34.052, lng: -118.243}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_sf_la.setMap(map);

  var link_dallas_chicago = new google.maps.Polyline({
    path: [{lat: 32.789997, lng: -96.77}, {lat: 41.878, lng: -87.629}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_dallas_chicago.setMap(map);


  var link_miami_dallas = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21}, {lat: 32.789997, lng: -96.77}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_miami_dallas.setMap(map);


  var link_dallas_la = new google.maps.Polyline({
    path: [{lat: 32.789997, lng: -96.77}, {lat: 34.052, lng: -118.243}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_dallas_la.setMap(map);

  var link_dallas_houston = new google.maps.Polyline({
    path: [{lat: 32.789997, lng: -96.77},  {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_dallas_houston.setMap(map);

  var link_miami_chicago = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21}, {lat: 41.878, lng: -87.629}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_miami_chicago.setMap(map);

  var link_miami_houston = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21},  {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_miami_houston.setMap(map);


  var link_miami_tampa = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21}, {lat: 27.960001, lng: -82.48}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_miami_tampa.setMap(map);

  var link_la_houston = new google.maps.Polyline({
    path: [{lat: 34.052, lng: -118.243},  {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_la_houston.setMap(map);


  var link_houston_tampa = new google.maps.Polyline({
    path: [ {lat: 29.770002, lng: -95.39}, {lat: 27.960001, lng: -82.48}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_houston_tampa.setMap(map);


  var link_tampa_ny = new google.maps.Polyline({
    path: [{lat: 27.960001, lng: -82.48}, {lat: 40.714, lng: -74.005}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_tampa_ny.setMap(map);

  var link_ny_chicago = new google.maps.Polyline({
    path: [{lat: 40.714, lng: -74.005}, {lat: 41.878, lng: -87.629}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_ny_chicago.setMap(map);
}

