
$(document).ready( function(){
    let houseAdd = window.location.href.split('?')[1];
    console.log('houseAdd??');console.log(houseAdd);console.log('......');
    if(houseAdd !== undefined){
        submitSearchForm(houseAdd);
    }
});

let searchB = $("#searchBar");
let searchR = $("#searchResultsField");


searchB.submit( function (event) {
    event.preventDefault();
    let searchQuery = $("#searchBar").serialize();
    console.log('sQuery:?');console.log(searchQuery);

    submitSearchForm(searchQuery);
});

function submitSearchForm(searchQuery) {
    $.get("sbAdd", searchQuery, function(resultData){handleSearchQuery(resultData);});
}

function handleSearchQuery(resultData) {
    // console.log('searchResult:??');console.log(resultData);
    searchR.html("");

    $("#resultDiv").show();
    // console.log(resultData.length);console.log(resultData);
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

            rowEntry += '</div></div></div>';

        }
        rowEntry += '</div>';
        searchR.append(rowEntry);
    }

    return resultData;
}

// $("moreBtn").onclick()

