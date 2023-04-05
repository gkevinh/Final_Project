'use strict';

const removeFavoriteButton = document.querySelector('.remove-favorite');

removeFavoriteButton.addEventListener('click', (evt) => {
    evt.preventDefault();
      const external_id = document.querySelector("#external_id").innerHTML;
      const venue_name = document.querySelector("#venue_name").innerHTML;
      const phone = document.querySelector("#phone").innerHTML;
      const address = document.querySelector("#address").innerHTML;
      const rating = document.querySelector("#rating").innerHTML;
      const review_count = document.querySelector("#review_count").innerHTML;
      removeFavorite(external_id, venue_name, phone, address, rating, review_count);
    });
  
  function removeFavorite(external_id, venue_name, phone, address, rating, review_count) {
    const input = {
      venue_name: venue_name,
      external_id: external_id,
      phone: phone,
      address: address,
      rating: rating,
      review_count: review_count
    }
    fetch('/remove-favorite', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // alert('Removed from favorites!'); 
        swal("Removed from favorites!"); 
      } else {
        // alert('Error removing from favorites.');
        swal("Cannot remove. Not a favorite.");         
      }
    })
    .catch(function(error) {
      console.error('Error removing favorite:', error);
      // alert('Error removing from favorites.');
      swal("Cannot remove. Not a favorite.");   
    });
  }
  