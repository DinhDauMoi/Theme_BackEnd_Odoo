odoo.define('geminate_ecommerce_theme.google_location', function (require) {
"use strict";
	
    var rpc = require("web.rpc");
    var ajax = require('web.ajax');

	$(document).ready(async function() {


		ajax.jsonRpc("/get/company/address", 'call',{}).then(function(data){
			console.log("--Map",$('.geminate_contact_form'))
			var google_key = data.google_api
			if(data && $('.geminate_contact_form').length > 0){
				let map;
				window.initMap = () => {
					var geocoder = new google.maps.Geocoder();
					var address = data.address;
					geocoder.geocode( { 'address': address}, function(results, status){
					    if(status == google.maps.GeocoderStatus.OK) {
						    var latitude = results[0].geometry.location.lat();
						    var longitude = results[0].geometry.location.lng();
							const mapOptions = {
							    zoom: 18,
							    center: { lat: latitude, lng: longitude},
							};
						    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
						    const marker = new google.maps.Marker({
							    // The below line is equivalent to writing:
							    // position: new google.maps.LatLng(-34.397, 150.644)
							    position: { lat: latitude, lng: longitude},
							    map: map,
							});
							// You can use a LatLng literal in place of a google.maps.LatLng object when
							// creating the Marker object. Once the Marker object is instantiated, its
							// position will be available as a google.maps.LatLng object. In this case,
							// we retrieve the marker's position using the
							// google.maps.LatLng.getPosition() method.
						  	const infowindow = new google.maps.InfoWindow({
						    	content: "<p>" + address + "</p>",
						  	});
						  	google.maps.event.addListener(marker, "click", () => {
						    	infowindow.open(map, marker);
						  	});
					  	}else{
					  		$("#map_canvas").addClass('No_mapFound')
					  		$("#map_canvas").text('No google map available!')
					  		$("#map_canvas").removeAttr('id')
					  	}
					})
				}
				if(google_key){
				    $.getScript('https://maps.googleapis.com/maps/api/js?key=' + google_key + '&callback=initMap&v=weekly')
				}else{
			  		$("#map_canvas").addClass('No_mapFound')
			  		$("#map_canvas").text('No google map available!')
			  		$("#map_canvas").removeAttr('id')
				}
			}

		});
		
	})
});
