var currentWindow = null;
var cafeData = {
  latitude: 35.684423,
  longitude: 139.743358,
  name: 'CAFE',
  type: ['不明'],
  lunch: 1000,
  dinner: 0,
  address: '東京都千代田区麹町１丁目４−４',
  point: 0,
  review: 0,
  holiday: '土日',
  station: '半蔵門',
  url: ''
}

var latitude = 35.684423;
var longitude = 139.743358;

var symbol = {
  path: google.maps.SymbolPath.CIRCLE,
  fillColor: "#ED6103",
  fillOpacity: 1,
  scale: 12,
  strokeColor: "white",
  strokeWeight: 3
};

var symbolGreen = {
  path: google.maps.SymbolPath.CIRCLE,
  fillColor: "#21bd28",
  fillOpacity: 1,
  scale: 12,
  strokeColor: "white",
  strokeWeight: 3
};


function initialize() {

  myLatLng = new google.maps.LatLng(latitude, longitude);
  var myOptions = {
    zoom: 17,
    center: myLatLng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    mapTypeControl: false
  };


  map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);

  createMarker(cafeData, map, symbol);

  $.getJSON("shop/get", function(data) {
    console.log(data);
    var len = data.length;
    data.sort(function(a,b){
      if(a.fields.name < b.fields.name) return -1;
      if(a.fields.name > b.fields.name) return 1;
      return 0;
    });
    for(var i = 0; i < len; i++) {
      shop = data[i].fields;
      if (shop.lunch == 0 || shop.lunch > 2000) {
        continue;
      }
      if (shop.latitude > 35.69 || shop.latitude < 35.68 || shop.longitude < 139.737624) {
        continue;
      }
      if (0.4 < getDistance(shop.latitude, shop.longitude, latitude, longitude)) {
        continue;
      }

      if (shop.lunch < 2000) {
        createMarker(shop, map, symbol);
      } else {
        createMarker(shop, map, symbolGreen);
      }
      $('#shopBody').append('<tr><td>' + shop.name + '</td><td>' + shop.lunch + '円</td><td>' + shop.review + '</td></tr>')
    }
  });

  google.maps.event.addListener(map, 'click', function() {
    $('body').removeClass('drawer-open');
    $('body').css('overflow', 'auto');
    currentWindow.close();
  });

  $('#shopTable').on('click', function() {
    $('body').removeClass('drawer-open');
    $('body').css('overflow', 'auto');
    currentWindow.close();
  });

  var styles = [
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [
        { lightness: 100 },
        { visibility: "simplified" }
      ]
    },{
      featureType: "road",
      elementType: "labels",
      stylers: [
        { visibility: "off" }
      ]
    },{
      featureType: "poi.business",
      elementType: "labels",
      stylers: [
        { visibility: "off" }
      ]
    },{
      featureType: "landscape",
      elementType: "labels",
      stylers: [
        { visibility: "off" }
      ]
    }
  ];
  map.setOptions({styles: styles});
  map.setTilt(45);

  google.maps.event.addListener(map, 'zoom_changed', function() {
    if (map.getZoom() > 17) {
      map.setMapTypeId(google.maps.MapTypeId.HYBRID);
    } else {
      map.setMapTypeId(google.maps.MapTypeId.ROADMAP);
    }
  });

  new google.maps.Circle({
    center: myLatLng,       // 中心点(google.maps.LatLng)
    fillColor: '#ff0000',   // 塗りつぶし色
    fillOpacity: 0.1,       // 塗りつぶし透過度（0: 透明 ⇔ 1:不透明）
    map: map,               // 表示させる地図（google.maps.Map）
    radius: 240,          // 半径（ｍ）
    strokeColor: '#ff0000', // 外周色
    strokeOpacity: 0,       // 外周透過度（0: 透明 ⇔ 1:不透明）
    strokeWeight: 0         // 外周太さ（ピクセル）
   });
}
google.maps.event.addDomListener(window, 'load', initialize);

function createMarker(data, map, symbol){
  var infoWindow = new google.maps.InfoWindow({maxWidth: 200, disableAutoPan: true});
  var marker = new google.maps.Marker({
    position: new google.maps.LatLng(data.latitude, data.longitude),
    map: map,
    icon: symbol
  });
  google.maps.event.addListener(marker, 'click', function() {
    if (currentWindow) {
      currentWindow.close();
    }

    var content = '<div class="iw-contents">' +
                  '<div class="iw-title">' + data.name.substr(0, 8) + '</div>' +
                  '<div class="iw-text">' +
                  data.type.join('/').substr(0, 11) +
                  '<br>ランチ値段　〜¥' + data.lunch +
                  '</div>' +
                  '</div>';

    infoWindow.setContent(content);
    infoWindow.open(map, marker);
    currentWindow = infoWindow;

    // Reference to the DIV that wraps the bottom of infowindow
    var iwOuter = $('.gm-style-iw');

    /* Since this div is in a position prior to .gm-div style-iw.
     * We use jQuery and create a iwBackground variable,
     * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
    */
    var iwBackground = iwOuter.prev();

    // Removes background shadow DIV
    iwBackground.children(':nth-child(2)').css({'display' : 'none'});

    // Removes white background DIV
    iwBackground.children(':nth-child(4)').css({'display' : 'none'});

    iwBackground.children(':nth-child(3)').find('div').children().css({'box-shadow': '#ccc 0px 1px 6px', 'z-index' : '1'});

    var iwCloseBtn = iwOuter.next();

    // Apply the desired effect to the close button
    iwCloseBtn.css({'display' : 'none'});

    $('.iw-text').on('click', function() {
      var id = $(this).attr('data-id');
      $('body').addClass('drawer-open');
      $('body').css('overflow', 'hidden');

      $('.nav-title').text(data.name);
      // $('.nav-maininfo tr:nth-child(1) td').text(data.type.join('/'));
      $('.nav-maininfo tr:nth-child(2) td').text("〜\u0020¥" + data.lunch);
      $('.nav-maininfo tr:nth-child(3) td').text("〜\u0020¥" + data.dinner);
      $('.nav-maininfo tr:nth-child(4) td').text(data.point + '点');
      $('.nav-maininfo tr:nth-child(5) td').text(data.review + '件');
      $('.nav-maininfo tr:nth-child(6) td').text(data.holiday);
      $('.nav-subinfo tr:nth-child(1) td').text(data.station);
      $('.nav-subinfo tr:nth-child(2) td').text(data.address);
      $('.nav-link').attr('href', data.url);
      $('.nav-review').attr('href', data.url + 'dtlrvwlst/COND-1/smp1/?lc=0&rvw_part=all');
    });
  });
}

//距離の計算//
function getDistance(lat1, lng1, lat2, lng2) {
   function radians(deg){
      return deg * Math.PI / 180;
   }

   return 6378.14 * Math.acos(Math.cos(radians(lat1))*
    Math.cos(radians(lat2))*
    Math.cos(radians(lng2)-radians(lng1))+
    Math.sin(radians(lat1))*
    Math.sin(radians(lat2)));
}
