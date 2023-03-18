'use strict';

const addFavoriteButton = document.querySelector('.add-favorite');
const removeFavoriteButton = document.querySelector('.remove-favorite');

addFavoriteButton.addEventListener('click', (evt) => {
  evt.preventDefault();
    const external_id = document.querySelector("#external_id").innerHTML;
    const venue_name = document.querySelector("#venue_name").innerHTML;
    const phone = document.querySelector("#phone").innerHTML;
    const address = document.querySelector("#address").innerHTML;
    const rating = document.querySelector("#rating").innerHTML;
    const review_count = document.querySelector("#review_count").innerHTML;
    addFavorite(external_id, venue_name, phone, address, rating, review_count);
  });

  removeFavoriteButton.addEventListener('click', function(evt) {
    removeFavorite(external_id);
  });

function addFavorite(external_id, venue_name, phone, address, rating, review_count) {
  const input = {
    venue_name: venue_name,
    external_id: external_id,
    phone: phone,
    address: address,
    rating: rating,
    review_count: review_count
  }
  fetch('/add-favorite', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(input)
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      alert('Added to favorites!');  
    } else {
      alert('Error adding to favorites.');
    }
  })
  .catch(function(error) {
    console.error('Error adding favorite:', error);
    alert('Error adding to favorites.');
  });
}
