'use strict';

console.log("hit js page")

const addFavoriteButton = document.querySelector('.add-favorite');
const removeFavoriteButton = document.querySelector('.remove-favorite');

addFavoriteButton.addEventListener('click', (evt) => {
  evt.preventDefault();
    const venue_id = document.querySelector("#venue_id").innerHTML;
    addFavorite(venue_id);
  });

  removeFavoriteButton.addEventListener('click', function(evt) {
    removeFavorite(email, venue_id);
  });


function addFavorite(venue_id) {
  const input = {
    venue: venue_id
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



function removeFavorite(venue_id) {
  fetch('/remove-favorite', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      venue_id: venue_id
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
