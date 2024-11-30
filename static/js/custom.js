



// to get current year
function getYear() {
  var currentDate = new Date();
  var currentYear = currentDate.getFullYear();
  document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// lightbox
// $(document).on("click", '[data-toggle="lightbox"]', function (event) {
//   event.preventDefault();
//   $(this).ekkoLightbox({
//     alwaysShowClose: true,
//     onShown: function(){
//       console.log('1212122');
//       var description = $(this).attr('data-description');
//       console.log(description);
//       if (description) {
        
//         $('.ekko-lightbox .modal-footer').html('<div>' + description + '</div>');
//         console.log('1212122yuvi121214');
//       }
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", function() {
  var lightboxTriggers = document.querySelectorAll('.lightbox-trigger');

  lightboxTriggers.forEach(function(lightboxTrigger) {
    lightboxTrigger.addEventListener("click", function(event) {
      event.preventDefault();
      
      // Initialize Ekko Lightbox with the clicked element
      $(lightboxTrigger).ekkoLightbox({
        alwaysShowClose: true,
        // onShown: function() {
        //   // Get the description from the data-description attribute of the clicked element
        //   var description = lightboxTrigger.getAttribute('data-description');
          
        //   if (description) {
        //     // Remove any existing description elements
        //     $('.ekko-lightbox .modal-body .description').remove();
        //     // Append the description to the lightbox modal's body
        //     $('.ekko-lightbox .modal-body').append('<div style="text-align: justify; margin:10px;" class="description">' + description + '</div>');
        //   }
        // }
      });
    });
  });
});


/** google_map js **/
// function myMap() {
//   var mapProp = {
//     center: new google.maps.LatLng(40.71775, -74.05973),
//     zoom: 18
//   };
//   var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
// }


// Function to handle form submission
// Function to display the popup on page load
function showPopup() {
  document.getElementById("mobilePopup").style.display = "block";
  
}

function closePopup() {
  document.getElementById("mobilePopup").style.display = "none";
}


  // Function to handle form submission
  function submitForm(event) {
      // Prevent the form from submitting in the traditional manner
      event.preventDefault();
      
      // Here you can add code to handle form submission, such as sending data to a server
      
      // After successful submission, hide the popup and allow access to the home page
      var popup = document.getElementById("mobilePopup");
      if (popup) {
          popup.style.display = "none";
          alert('Form Submitted');
      }
  }

  // Close popup when the form is submitted
  $("#popupForm").submit(function(event) {
      submitForm(event);
  });


  $(window).on('load', function () {
    setTimeout(function() {
      $('.loader-box').fadeOut(500); // Hide the loading animation after the delay
  }, 500); // Adjust the delay time (in milliseconds) as needed
    
  })
