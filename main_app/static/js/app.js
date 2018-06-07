let destinationSight1, destinationSight2, destinationSight3;
let destinationFood1, destinationFood2, destinationFood3;
let destinationDrinks1, destinationDrinks2, destinationDrinks3;
let destinationSights = [];
let destinationFood = [];
let destinationDrinks = [];

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();

  $('.search-button').on('click', function (event) {
    event.preventDefault();
    let tripPurposeSelection = $('.trip-purpose-select')[0].selectedOptions[0].innerText;
    let regionSelection = $('.region-select')[0].selectedOptions[0].innerText;
    // let monthSelection = $('.month-select')[0].selectedOptions[0].innerText;
    console.log(tripPurposeSelection);
    console.log(regionSelection);
    // console.log(monthSelection);
    let element = $('.destination-box');
    $.ajax({
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      url: '/destinations/',
      method: 'POST',
      data: {'trip_purpose': tripPurposeSelection, 'selected_region': regionSelection},
      success: function (response) {
        console.log(response)
        element.val(response.city);
        appendDestinationDetails(response)
      }
    })
  })
});

const appendSights = (sights) => {
  $('.sites-row').empty()
  sights.forEach( (val) => {
    let html = `<div class="col m12 l4">
                  <h5 class="header">${val.sight_name}</h5>
                  <div class="card horizontal">
                    <div class="card-image">
                      <img src="https://lorempixel.com/100/190/nature/6">
                    </div>
                    <div class="card-stacked">
                      <div class="card-content">
                        <p>I am a very simple card. I am good at containing small bits of information.</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.sites-row').append(html)
  })
}
const appendFood = (food) => {
  $('.food-row').empty()
  food.forEach((val) => {
    let html = `<div class="col m12 l4">
                  <h5 class="header">${val.restaurant_name}</h5>
                  <div class="card horizontal">
                    <div class="card-image">
                      <img src="https://lorempixel.com/100/190/nature/6">
                    </div>
                    <div class="card-stacked">
                      <div class="card-content">
                        <p>I am a very simple card. I am good at containing small bits of information.</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.food-row').append(html)
  })
}
const appendDrinks = (drinks) => {
  $('.drinks-row').empty()
  drinks.forEach((val) => {
    let html = `<div class="col m12 l4">
                  <h5 class="header">${val.bar_name}</h5>
                  <div class="card horizontal">
                    <div class="card-image">
                      <img src="https://lorempixel.com/100/190/nature/6">
                    </div>
                    <div class="card-stacked">
                      <div class="card-content">
                        <p>I am a very simple card. I am good at containing small bits of information.</p>
                      </div>
                    </div>
                  </div>
                </div>`
    $('.drinks-row').append(html)
  })
}

const appendDestinationDetails = (destination) => {
  appendSights(destination.sights);
  appendFood(destination.food);
  appendDrinks(destination.drinks);
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