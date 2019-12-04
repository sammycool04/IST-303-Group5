console.log(" In astar.js : \n");

//retrieve the query part from url
let houseId = window.location.href.split('?')[1].split('=')[1];
console.log("splitted url: ");console.log(houseId);

let searchR = $("#searchResults");


$.get("sbId", {'id':houseId}, function(resultData){handleSearchQuery(resultData);});

function handleSearchQuery(resultData) {
    searchR.html("");

    console.log(resultData.length);console.log(resultData);

    // let data = JSON.parse(resultData);
    // console.log("getForm: ");console.log(resultData);console.log("json data: ");console.log(data);


    let rowEntry = '<div class="row">';
    if(resultData.length === 0){
        console.log("is oo");
        rowEntry += '<div class="card" style="margin:5%;padding:5%;width:80%;"><p>Sorry. We currently do not have any more details.</p></div></div>';
        searchR.append(rowEntry);
    }
    else{
        rowEntry += '<div class="col-md-12"><div class="card mb-4 shadow-sm">';
        rowEntry += '<img class="resultImg" src="' + resultData['image'] + '" alt="image..">';
        rowEntry += '<div class="card-body">';
        rowEntry += '<span class="card-text">' + resultData['address'] + '</span>';
        rowEntry += '<br><span class="card-text">Price: $' + resultData['price'] + '</span>';

        rowEntry += '<div class="d-flex justify-content-between align-items-center">';
        rowEntry += '<span class="text-muted">' + resultData['room'] + ' bed </span>';
        rowEntry += '<span class="text-muted">' + resultData['bath'] + ' bath</span>';
        rowEntry += '<span class="text-muted">' + resultData['size'] + ' sqft</span>';
        rowEntry += '</div>';
        rowEntry += '<p class="card-text">Summary: ' + resultData['summary'] + '</p>';
        rowEntry += '<p class="card-text">For ' + resultData['categories'] + '</p>';

        rowEntry += '</div></div></div>';

        }
        rowEntry += '</div>';
        searchR.append(rowEntry);

    return resultData;
}