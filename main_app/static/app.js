let destinationSight1, destinationSight2, destinationSight3;
let destinationFood1, destinationFood2, destinationFood3;
let destinationDrinks1, destinationDrinks2, destinationDrinks3;
let destinationSights = [];
let destinationFood = [];
let destinationDrinks = [];

$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.search-button').on('click', function (event) {
    event.preventDefault();
    let element = $('.destination-box');
    $.ajax({
      url: '/destinations/',
      method: 'GET',
      success: function (response) {
        console.log(response)
        element.val(response.city);
        appendDestinationDetails(response)
      }
    })
  })
});

const appendSights = () => {
  console.log('appendSights', destinationSights);
}
const appendFood = () => {
  console.log('appendFood', destinationFood);
}
const appendDrinks = () => {
  console.log('appendDrinks', destinationDrinks);
}

const appendDestinationDetails = (destination) => {
  appendSights();
  appendFood();
  appendDrinks();
}