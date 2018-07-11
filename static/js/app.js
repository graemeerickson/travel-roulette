let map;

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();
  window.sr = ScrollReveal();
  sr.reveal('.search-section');

  let delay = 1000;
  let cities = ['Barcelona', 'Cancun','Dubai','Tokyo','Maui','Seattle'];
  let input = document.getElementById('destination-box');
  input.setAttribute('placeholder', 'Seattle')

  for (let i = 0; i < cities.length; i++) {
    set(cities[i], i * delay);
  }

  function set(city, d) {
    setTimeout(function () {
      setInterval(function () {
        input.setAttribute('placeholder', city);
      }, delay * cities.length);
    }, d);
  }

  $('.search-button').on('click', function (event) {
    event.preventDefault();
    let tripPurposeSelection = $('.trip-purpose-select')[0].selectedOptions[0].innerText;
    let regionSelection = $('.region-select')[0].selectedOptions[0].innerText;
    // let monthSelection = $('.month-select')[0].selectedOptions[0].innerText;
    let element = $('.destination-box');
    $.ajax({
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      url: '/destinations/',
      method: 'POST',
      data: {'trip_purpose': tripPurposeSelection, 'selected_region': regionSelection},
      success: function (response) {
        element.val(response.city);
        appendDestinationDetails(response)
      },
      error: function (response) {
        console.log('response:', response)
        handleError
      }
    })
  })
});

const appendMap = (latitude, longitude, mapboxToken) => {
  $('#destination-top-section-map').empty()
  let html1 = `<div class='row map-row' id='map' style='width: 100%; height: 350px;'></div>`
  $('#destination-top-section-map').append(html1)
  let html = `<script>
                mapboxgl.accessToken = '${mapboxToken}';
                map = new mapboxgl.Map({
                  container: 'map',
                  center: [${longitude},${latitude}],
                  zoom: 11,
                  style: 'mapbox://styles/mapbox/streets-v9'
                });
            </script>`
  $('.map-row').append(html)
}

const appendSights = (sights) => {
  $('#destination-top-section-sights').empty()
  let html1 = `<hr><h4 class="destination-detail-heading">Top Sights</h4>
              <div class="row sites-row"></div>`
  $('#destination-top-section-sights').append(html1)

  sights.forEach( (val) => {
    let html = `<div class="col m12 l4">
                  <div class="card horizontal">
                    <div class="card-stacked">
                      <div class="card-content destination-content">
                        <h6 class="destination-card-name">${val.sight_name}</h6>
                        <p>${val.address_formatted}</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.sites-row').append(html)
  })
}
const appendFood = (food) => {
  $('#destination-top-section-food').empty()
  let html1 = `<hr><h4 class="destination-detail-heading">Top Restaurants</h4>
              <div class="row food-row"></div>`
  $('#destination-top-section-food').append(html1)

  food.forEach((val) => {
    let html = `<div class="col m12 l4">
                  <div class="card horizontal">
                    <div class="card-stacked">
                      <div class="card-content destination-content">
                        <h6 class="destination-card-name">${val.restaurant_name}</h6>
                        <p>${val.address_formatted}</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.food-row').append(html)
  })
}
const appendDrinks = (drinks) => {
  $('#destination-top-section-drinks').empty()
  let html1 = `<hr><h4 class="destination-detail-heading">Top Bars</h4>
              <div class="row drinks-row"></div>`
  $('#destination-top-section-drinks').append(html1)
  drinks.forEach((val) => {
    let html = `<div class="col m12 l4">
                  <div class="card horizontal">
                    <div class="card-stacked">
                      <div class="card-content destination-content">
                        <h6 class="destination-card-name">${val.bar_name}</h6>
                        <p>${val.address_formatted}</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.drinks-row').append(html)
  })
}

const appendDestinationDetails = (destination) => {
  $('#destination-top-section-error').empty()
  sr.reveal('.results-section');
  appendMap(destination.lat, destination.long, destination.mapbox_api_token)
  appendSights(destination.sights);
  appendFood(destination.food);
  appendDrinks(destination.drinks);
}

const handleError = (response) => {
  $('#destination-top-section-error').empty()
  $('#destination-top-section-map').empty()
  $('#destination-top-section-sights').empty()
  $('#destination-top-section-food').empty()
  $('#destination-top-section-drinks').empty()
  
  let html = `<div id='destination-top-section-error'>
                <h6>We couldn't find any destinations meeting your criteria. Adjust your criteria and try again!</h6>
              </div>`
  
  $('.results-section').append(html)
}

function getCookie(c_name) {
  if (document.cookie.length > 0) {
    c_start = document.cookie.indexOf(c_name + "=");
    if (c_start != -1) {
      c_start = c_start + c_name.length + 1;
      c_end = document.cookie.indexOf(";", c_start);
      if (c_end == -1) c_end = document.cookie.length;
      return unescape(document.cookie.substring(c_start, c_end));
    }
  }
  return "";
}