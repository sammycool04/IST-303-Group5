
console.log("home.js?");
let url = window.location.href;
let uri = window.location.search;
console.log("search part: "); console.log(uri);
console.log("splitted url: ");console.log(url);


// $("#searchBtn").click(function(event) {
//     event.preventDefault();
//     alert( "Handler for .click() called." );
// });



let searchQuery = $("#searchBar").serialize();
