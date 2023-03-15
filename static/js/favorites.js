'use strict';

function addFavorite(evt) {
  evt.preventDefault();
  const venueId = evt.target.dataset.venueId;
  
  fetch(`/add-favorite/${venueId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ venue_id: venueId })
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === 'success') {
        alert(data.message);
      } else {
        console.error(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
    });
}

document.querySelectorAll('.add-favorite').forEach((button) => {
  button.addEventListener('click', addFavorite);
});
