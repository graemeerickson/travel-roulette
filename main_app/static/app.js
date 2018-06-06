let destinationSight1, destinationSight2, destinationSight3;
let destinationFood1, destinationFood2, destinationFood3;
let destinationDrinks1, destinationDrinks2, destinationDrinks3;
let destinationSights = [];
let destinationFood = [];
let destinationDrinks = [];

$('.search-button').on('click', function (event) {
  event.preventDefault();
  let element = $('.destination-box');
  $.ajax({
    url: '/destinations/',
    method: 'GET',
    success: function (response) {
      element.val(response.city);
      getDestinationDetails(response)
    }
  })
})

const getDestinationDetails = (destination) => {
  // get top sights
  $.ajax({
    url: `https://api.foursquare.com/v2/venues/explore/?near='${destination.city}, ${destination.country}'&client_id=&client_secret=&v=20180605&section=sights&limit=3`,
    method: 'GET',
    success: function (response) {
      destinationSights = [];
      response.response.groups[0].items.forEach( (val) => {
        destinationSights.push(val.venue)
      })
      console.log('destinationSights:', destinationSights)
    }
  })
  // get top restaurants
  $.ajax({
    url: `https://api.foursquare.com/v2/venues/explore/?near='${destination.city}, ${destination.country}'&client_id=&client_secret=&v=20180605&section=food&limit=3`,
    method: 'GET',
    success: function (response) {
      destinationFood = [];
      response.response.groups[0].items.forEach((val) => {
        destinationFood.push(val.venue)
      })
      console.log('destinationFood:', destinationFood)
    }
  })
  // get top bars
  $.ajax({
    url: `https://api.foursquare.com/v2/venues/explore/?near='${destination.city}, ${destination.country}'&client_id=&client_secret=&v=20180605&section=drinks&limit=3`,
    method: 'GET',
    success: function (response) {
      destinationDrinks = [];
      response.response.groups[0].items.forEach((val) => {
        destinationDrinks.push(val.venue)
      })
      console.log('destinationDrinks:', destinationDrinks)
    }
  })
}

const appendSights = () => {
  console.log('appendSights', destinationSights);
}
const appendFood = () => {
  console.log('appendFood', destinationFood);
}
const appendDrinks = () => {
  console.log('appendDrinks', destinationDrinks);
}

const appendDestinationDetails = () => {
  appendSights();
  appendFood();
  appendDrinks();
}