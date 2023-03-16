'use strict';

console.log("hit js page")

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
    addFavorite(external_id);
  });

  removeFavoriteButton.addEventListener('click', function(evt) {
    removeFavorite(email, external_id);
  });

function addFavorite(external_id) {
  // const input = {
  //   venue: external_id
  // }
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



function removeFavorite(external_id) {
  fetch('/remove-favorite', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      external_id: external_id
    })
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      alert('Removed from favorites!');
    } else {
      alert('Error removing from favorites.');
    }
  })
  .catch(function(error) {
    console.error('Error removing favorite:', error);
    alert('Error removing from favorites.');
  });
}
