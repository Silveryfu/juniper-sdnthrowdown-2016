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

	$.getScript( "link_event.js", function(data, textStatus, jqxhr ) {
	  // console.log( data ); // Data returned
	  // console.log( textStatus ); // Success
	  // console.log( jqxhr.status ); // 200
	  // console.log( "Load was performed." );
	});

	$.getScript( "link.js", function(data, textStatus, jqxhr ) {
	  // console.log( data ); // Data returned
	  // console.log( textStatus ); // Success
	  // console.log( jqxhr.status ); // 200
	  // console.log( "Load was performed." );
	});
	update_link_bw();
	update_link_status();
	update_lsp();
}

function update_link_bw() {
	var delim = 2000000/1000000000;
	console.log(link_1);
	link_1_bw.setOptions({strokeWeight: link_1[link_1.length - 1].bandwidth * delim});
	link_2_bw.setOptions({strokeWeight: link_2[link_2.length - 1].bandwidth * delim});
	link_3_bw.setOptions({strokeWeight: link_3[link_3.length - 1].bandwidth * delim});
	link_4_bw.setOptions({strokeWeight: link_4[link_4.length - 1].bandwidth * delim});
	link_5_bw.setOptions({strokeWeight: link_5[link_5.length - 1].bandwidth * delim});
	link_6_bw.setOptions({strokeWeight: link_6[link_6.length - 1].bandwidth * delim});
	link_7_bw.setOptions({strokeWeight: link_7[link_7.length - 1].bandwidth * delim});
	link_8_bw.setOptions({strokeWeight: link_8[link_8.length - 1].bandwidth * delim});
	link_9_bw.setOptions({strokeWeight: link_9[link_9.length - 1].bandwidth * delim});
	link_10_bw.setOptions({strokeWeight: link_10[link_10.length - 1].bandwidth * delim});
	link_11_bw.setOptions({strokeWeight: link_11[link_11.length - 1].bandwidth * delim});
	link_12_bw.setOptions({strokeWeight: link_12[link_12.length - 1].bandwidth * delim});
	link_13_bw.setOptions({strokeWeight: link_13[link_13.length - 1].bandwidth * delim});
	link_14_bw.setOptions({strokeWeight: link_14[link_14.length - 1].bandwidth * delim});
	link_15_bw.setOptions({strokeWeight: link_15[link_15.length - 1].bandwidth * delim});
}

function update_link_status() {
	var status = link_event[link_event.length - 1].status;

	if (String(status).localeCompare('failed') == 0) {
		var link_fail_path = link_event.slice(0, 2);
		var path = new Array();
		
		$.each(link_fail_path, function(index, value) {
			path.push({lat: parseFloat(value.lat), lng: parseFloat(value.lng)});
		});
		link_fail.setMap(map);
		link_fail.setPath(path);
	} else {
		link_fail.setMap(null);
	} 
	// if (link_event[link_event.length - 1].status.localeCompare("fail") == 0) {
	// console.log("adsfas");
	// };
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