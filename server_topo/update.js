window.setInterval(update_map, 1000);
var topo_data;

function update_map() {
	$.getScript( "lsp.js", function(data, textStatus, jqxhr ) {
	  // console.log( data ); // Data returned
	  // console.log( textStatus ); // Success
	  // console.log( jqxhr.status ); // 200
	  // console.log( "Load was performed." );
	});

	update_lsp();
}


function update_lsp() {
	var path = new Array();
	$.each(lsp_1_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});
	lsp_1.setPath(path);

	var path = new Array();
	$.each(lsp_2_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});
	lsp_2.setPath(path);

	var path = new Array();
	$.each(lsp_3_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});

	lsp_3.setPath(path);

	var path = new Array();
	$.each(lsp_4_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});

	lsp_4.setPath(path);

	var path = new Array();
	$.each(lsp_5_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});
	lsp_5.setPath(path);

	var path = new Array();
	$.each(lsp_6_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});

	lsp_6.setPath(path);

	var path = new Array();
	$.each(lsp_7_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});
	
	lsp_7.setPath(path);

	var path = new Array();
	$.each(lsp_8_path, function(index, value) {
		path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		// 
	});
	
	lsp_8.setPath(path);
}