'use strict';

function addFavorite(user_id, venue_id) {
  evt.preventDefault();

  fetch('/add-favorite', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id: user_id,
      venue_id: venue_id
    })
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
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
