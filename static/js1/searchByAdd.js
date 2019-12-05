let houseAdd = window.location.href.split('?')[1].split('=')[1];

$(document).ready( function(){
    let url = window.location.href;
    console.log("splitted url: ");console.log(url);
    let uri = window.location.search;
    console.log("search part: "); console.log(uri);
});

let searchB = $("#searchBar");
let searchR = $("#searchResults");


searchB.submit( function (event) {
    event.preventDefault();
    let searchQuery = $("#searchBar").serialize();
    console.log(searchQuery);
    submitSearchForm(searchQuery);
});

function submitSearchForm(searchQuery) {
    $.get("sbAdd", searchQuery, function(resultData){handleSearchQuery(resultData);});
}

function handleSearchQuery(resultData) {
    $("#resultDiv").show();
    searchR.html("");

    console.log(resultData.length);console.log(resultData);


    // let data = JSON.parse(resultData);
    // console.log("getForm: ");console.log(resultData);console.log("json data: ");console.log(data);
    let rowEntry = '<div class="row">';
    if(resultData.length === 0){
        console.log("is oo");
        rowEntry += '<div class="card" style="margin:5%;padding:5%;width:80%;"><p>Sorry. We currently do not have any house data in the area</p></div></div>';
        searchR.append(rowEntry);
    }
    else{
        for (let i = 0; i < resultData.length; i++) {
            // rowEntry += '<div class="card" style="margin-top:10%;width:90%;">';
            // rowEntry += '<div class="card"><img src="' + resultData[i]['image'] + '" style="width:400px;height:300px;" alt="Image">' + '</div>';
            // rowEntry += '<div>' + 'Address: ' + resultData[i]['address'] + '</div>';
            // rowEntry += '<div>' + 'Price:   ' + resultData[i]['price'] + '</div>';
            // rowEntry += '<div>' + 'Room: ' + resultData[i]['room'] + '</div>';
            // rowEntry += '<div>' + 'Bath: ' + resultData[i]['bath'] + '</div>';
            // rowEntry += '<div>' + 'Size: ' + resultData[i]['size'] + 'sq ft</div>';
            // rowEntry += '<div>' + 'Summary: ' + resultData[i]['summary'] + '</div>';
            // rowEntry += '<div>' + 'For ' + resultData[i]['categories'] + '</div>';
            // rowEntry += '</div>';


            rowEntry += '<div class="col-md-4"><div class="card mb-4 shadow-sm">';
            rowEntry += '<img class="resultImg" src="' + resultData[i]['image'] + '" alt="image..">';
            rowEntry += '<div class="card-body">';
            rowEntry += '<span class="card-text">' + resultData[i]['address'] + '</span>';
            rowEntry += '<br><span class="card-text">Price: $' + resultData[i]['price'] + '</span>';

            rowEntry += '<div class="d-flex justify-content-between align-items-center">';
            rowEntry += '<span class="text-muted">' + resultData[i]['room'] + ' bed </span>';
            rowEntry += '<span class="text-muted">' + resultData[i]['bath'] + ' bath</span>';
            rowEntry += '<span class="text-muted">' + resultData[i]['size'] + ' sqft</span>';
            rowEntry += '<button type="button" class="btn btn-sm btn-outline-secondary moreBtn" ' +
                'onclick="window.location.href = \'houseDetail.html?id=' +  resultData[i]['id'] + '\'">More Details</button>';
            rowEntry += '</div>';
            // rowEntry += '<p class="card-text">Summary: ' + resultData[i]['summary'] + '</p>';
            // rowEntry += '<p class="card-text">For ' + resultData[i]['categories'] + '</p>';

            rowEntry += '</div></div></div>';



        }
        rowEntry += '</div>';
        searchR.append(rowEntry);
    }

    return resultData;
}

// $("moreBtn").onclick()



// $().on('load',
//     jQuery.ajax({
//         dataType:"json",
//         method:"GET",
//         url: "sbAdd",
//         data: {'starDetail': sid},
//         success: function(resultData){getStarInfo(resultData)},
//         error: function (jqXhr, textStatus, errorMessage) {
//             console.log("Error", errorMessage)
//         }
//     }));
