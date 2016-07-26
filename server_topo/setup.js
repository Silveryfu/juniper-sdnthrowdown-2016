var map;
var lsp_1, lsp_2, lsp_3, lsp_4;
var lsp_5, lsp_6, lsp_7, lsp_8;

var lsp_1_path, lsp_2_path, lsp_3_path, lsp_4_path;
var lsp_5_path, lsp_6_path, lsp_7_path, lsp_8_path;

var lsp_f;

var lsp_1_color, lsp_2_color, lsp_3_color, lsp_4_color;
var lsp_5_color, lsp_6_color, lsp_7_color, lsp_8_color;

var link_fail;

var link_event = new Array();

var link_1 = new Array();
var link_2 = new Array();
var link_3 = new Array();
var link_4 = new Array();
var link_5 = new Array();
var link_6 = new Array();
var link_7 = new Array();
var link_8 = new Array();
var link_9 = new Array();
var link_10 = new Array();
var link_11 = new Array();
var link_12 = new Array();
var link_13 = new Array();
var link_14 = new Array();
var link_15 = new Array();

var link_1_bw;
var link_2_bw;
var link_3_bw;
var link_4_bw;
var link_5_bw;
var link_6_bw;
var link_7_bw;
var link_8_bw;
var link_9_bw;
var link_10_bw;
var link_11_bw;
var link_12_bw;
var link_13_bw;
var link_14_bw;
var link_15_bw;

function animateObject(line) {
    var count = 0;
    if(line.get('strokeOpacity') == 0.9) {
      return;
    }
    window.setInterval(function() {
      count = (count + 1) % 200;
      var icons = line.get('icons');
      icons[0].offset = (count / 2) + '%';
      line.set('icons', icons);
  }, 20);
    line.set('strokeOpacity', 0.9); 
}

function de_animateObject(line) {
}

function initMap() {
  var mapDiv = document.getElementById('map');
  map = new google.maps.Map(mapDiv, {
    center: {lat: 30.789997, lng: -92.77},
    // center: {lat: 32.789997, lng: -96.77},
    zoom: 5
  });

  lsp_1_color = '#f1c40f';
  lsp_2_color = '#f39c12';
  lsp_3_color = '#d35400';
  lsp_4_color = '#c0392b';
  lsp_5_color = '#8e44ad';
  lsp_6_color = '#16a085';
  lsp_7_color = '#3498db';
  lsp_8_color = '#34495e';

  set_topo();
  set_marker();
  set_marker_fc();
  set_lsp();
  set_link_bw();
  set_fail_link();
}

function set_fail_link() {
  var cross_weight = 3;
  var cross_icon = {
    path: "M -2,-2 2,2 M 2,-2 -2,2",
    strokeWeight: cross_weight,
    scale: 10
  };
 
    link_fail = new google.maps.Polyline({
    geodesic: true,
    strokeColor: '#c0392b',
    strokeOpacity: 1.0,
    icons: [{
      icon: cross_icon,
      offset: '50%',
    }],
    strokeWeight: 4
  });
 
  link_fail.setMap(null);
}

function set_link_bw() {

link_1_bw = new google.maps.Polyline({
    path: [{lat: 37.79, lng: -122.55}, {lat: 32.789997, lng: -96.77}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_1_bw.setMap(map);

link_2_bw = new google.maps.Polyline({
  path: [{lat: 37.79, lng: -122.55}, {lat: 41.84, lng: -87.68}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_2_bw.setMap(map);

link_3_bw = new google.maps.Polyline({
  path: [{lat: 37.79, lng: -122.55}, {lat: 34.11, lng: -118.41}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_3_bw.setMap(map);

link_4_bw = new google.maps.Polyline({
  path: [{lat: 32.789997, lng: -96.77}, {lat: 25.78, lng: -80.21}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_4_bw.setMap(map);

link_5_bw = new google.maps.Polyline({
  path: [{lat: 32.789997, lng: -96.77}, {lat: 41.84, lng: -87.68}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_5_bw.setMap(map);

link_6_bw = new google.maps.Polyline({
  path: [{lat: 32.789997, lng: -96.77}, {lat: 34.11, lng: -118.41}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_6_bw.setMap(map);

link_7_bw = new google.maps.Polyline({
  path: [{lat: 32.789997, lng: -96.77}, {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_7_bw.setMap(map);

link_8_bw = new google.maps.Polyline({
  path: [{lat: 25.78, lng: -80.21},  {lat: 40.67, lng: -73.94}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_8_bw.setMap(map);

link_9_bw = new google.maps.Polyline({
  path: [{lat: 25.78, lng: -80.21}, {lat: 41.84, lng: -87.68}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_9_bw.setMap(map);

link_10_bw = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21}, {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_10_bw.setMap(map);

link_11_bw = new google.maps.Polyline({
    path: [{lat: 25.78, lng: -80.21}, {lat: 27.960001, lng: -82.48}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_11_bw.setMap(map);


link_12_bw = new google.maps.Polyline({
    path: [{lat: 34.11, lng: -118.41}, {lat: 29.770002, lng: -95.39}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_12_bw.setMap(map);

link_13_bw = new google.maps.Polyline({
    path: [{lat: 29.770002, lng: -95.39}, {lat: 27.960001, lng: -82.48}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_13_bw.setMap(map);

link_14_bw = new google.maps.Polyline({
    path: [{lat: 27.960001, lng: -82.48}, {lat: 40.67, lng: -73.94}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_14_bw.setMap(map);

link_15_bw = new google.maps.Polyline({
    path: [{lat: 40.67, lng: -73.94}, {lat: 41.84, lng: -87.68}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 0.5,
    strokeWeight: 2
  });

link_15_bw.setMap(map);

}

function set_marker_fc() {
  var myCenter=new google.maps.LatLng(42.432488, -70.088068);

  var icon_f = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: '#ecf0f1',
    fillOpacity: .6,
    strokeWeight: 0,
      // scale: iconSize
    };

    var marker_f=new google.maps.Marker({
      position:myCenter,
      icon: icon_f,
      label: "F"
    });

    marker_f.addListener('click', function() {
      add_lsp_f();
    });

    marker_f.addListener('dblclick', function() {
      remove_lsp_f();
    });

    marker_f.setMap(map);

    function add_lsp_f() {
     lsp_1.setMap(map);
     lsp_2.setMap(map);
     lsp_3.setMap(map);
     lsp_4.setMap(map);
     lsp_5.setMap(map);
     lsp_6.setMap(map);
     lsp_7.setMap(map);
     lsp_8.setMap(map);
   }

   function remove_lsp_f() {
     lsp_f.setMap(null);
   }

   var myCenter=new google.maps.LatLng(42.432488, -66.088068);

   var icon_c = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: '#7f8c8d',
    fillOpacity: .6,
    strokeWeight: 0,
      // scale: iconSize
    };

    var marker_c=new google.maps.Marker({
      position:myCenter,
      icon: icon_c,
      label: "C"
    });

    marker_c.addListener('click', function() {
      remove_lsp_c();
    });

  // marker_c.addListener('dblclick', function() {
  //     add_lsp_c();
  // });

  marker_c.setMap(map);

  function add_lsp_c() {
   lsp_c.setMap(map);
 }

 function remove_lsp_c() {
   lsp_1.setMap(null);
   lsp_2.setMap(null);
   lsp_3.setMap(null);
   lsp_4.setMap(null);
   lsp_5.setMap(null);
   lsp_6.setMap(null);
   lsp_7.setMap(null);
   lsp_8.setMap(null);
 }
}

function set_marker() {
  var myCenter=new google.maps.LatLng(40.432488, -68.088068);


  var icon_1 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_1_color,
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
      animateObject(lsp_1);
    });

    marker_1.addListener('rightclick', function() {
      remove_lsp_1();
      de_animateObject(lsp_1);
    });

    marker_1.setMap(map);

    function add_lsp_1() {
     lsp_1.setMap(map);
   }

   function remove_lsp_1() {
     lsp_1.setMap(null);
   }

   var myCenter=new google.maps.LatLng(38.432488, -68.088068);

   var icon_2 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_2_color,
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
      animateObject(lsp_2);
    });

    marker_2.addListener('rightclick', function() {
      remove_lsp_2();
      de_animateObject(lsp_2);
    });

    marker_2.setMap(map);

    function add_lsp_2() {
     lsp_2.setMap(map);
   }

   function remove_lsp_2() {
     lsp_2.setMap(null);
   }

   var myCenter=new google.maps.LatLng(36.432488, -68.088068);

   var icon_3 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_3_color,
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
      animateObject(lsp_3);
    });

    marker_3.addListener('rightclick', function() {
      remove_lsp_3();
      de_animateObject(lsp_3);
    });

    marker_3.setMap(map);

    function add_lsp_3() {
     lsp_3.setMap(map);
   }

   function remove_lsp_3() {
     lsp_3.setMap(null);
   }

   var myCenter=new google.maps.LatLng(34.432488, -68.088068);

   var icon_4 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_4_color,
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
      animateObject(lsp_4);
    });

    marker_4.addListener('rightclick', function() {
      remove_lsp_4();
      de_animateObject(lsp_4);
    });

    marker_4.setMap(map);

    function add_lsp_4() {
     lsp_4.setMap(map);
   }

   function remove_lsp_4() {
     lsp_4.setMap(null);
   }

   var myCenter=new google.maps.LatLng(32.432488, -68.088068);

   var icon_5 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_5_color,
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
      animateObject(lsp_5);
    });

    marker_5.addListener('rightclick', function() {
      remove_lsp_5();
      de_animateObject(lsp_5);
    });

    marker_5.setMap(map);

    function add_lsp_5() {
     lsp_5.setMap(map);
   }

   function remove_lsp_5() {
     lsp_5.setMap(null);
   }

   var myCenter=new google.maps.LatLng(30.432488, -68.088068);

   var icon_6 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_6_color,
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
      animateObject(lsp_6);
    });

    marker_6.addListener('rightclick', function() {
      remove_lsp_6();
      de_animateObject(lsp_6);
    });

    marker_6.setMap(map);

    function add_lsp_6() {
     lsp_6.setMap(map);
   }

   function remove_lsp_6() {
     lsp_6.setMap(null);
   }

   var myCenter=new google.maps.LatLng(28.432488, -68.088068);

   var icon_7 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_7_color,
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
      animateObject(lsp_7);
    });

    marker_7.addListener('rightclick', function() {
      remove_lsp_7();
      de_animateObject(lsp_7);
    });

    marker_7.setMap(map);

    function add_lsp_7() {
     lsp_7.setMap(map);
   }

   function remove_lsp_7() {
     lsp_7.setMap(null);
   }

   var myCenter=new google.maps.LatLng(26.432488, -68.088068);

   var icon_8 = {
    path: "M-20,0a20,20 0 1,0 40,0a20,20 0 1,0 -40,0",
    fillColor: lsp_8_color,
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
      animateObject(lsp_8);
    });

    marker_8.addListener('rightclick', function() {
      remove_lsp_8();
      de_animateObject(lsp_8);
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
  var arrow_weight = 7;
  var arrow_icon = {
    path: google.maps.SymbolPath.FORWARD_OPEN_ARROW,
    strokeWeight: arrow_weight
  };

  lsp_1 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_1_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_1.setMap(null);

  lsp_2 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_2_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]

  });

  lsp_2.setMap(null);

  lsp_3 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_3_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_3.setMap(null);

  lsp_4 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_4_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_4.setMap(null);

  lsp_5 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_5_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_5.setMap(null);

  lsp_6 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_6_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_6.setMap(null);

  lsp_7 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_7_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
  });

  lsp_7.setMap(null);

  lsp_8 = new google.maps.Polyline({
    geodesic: true,
    strokeColor: lsp_8_color,
    strokeOpacity: 1.0,
    strokeWeight: lsp_weight,
    icons: [{
      icon: arrow_icon,
      offset: '100%',
    }
    // , {
    //   icon: arrow_icon,
    //   offset: '75%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '50%',
    // }, {
    //   icon: arrow_icon,
    //   offset: '25%',
    // }
    ]
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

    if(router == "sanfranciso" || router == "newyork") {
      cityCircle.strokeColor = "#e74c3c";
      cityCircle.fillColor = "#27ae60";
      cityCircle.radius = 100000;
      cityCircle.strokeWeight = 4;
    }
  }

  var link_fail = new google.maps.Polyline({
    path: [{lat: 37.79, lng: -122.55}, {lat: 32.789997, lng: -96.77}],
    geodesic: true,
    strokeColor: '#3498db',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  link_fail.setMap(null);


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

