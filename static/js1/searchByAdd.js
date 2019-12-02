
let searchB = $("#searchBar");
let searchR = $("#searchResults");


searchB.submit( function (event) {
    event.preventDefault();
    submitSearchForm(event);
});

function submitSearchForm(formSubmitEvent) {
    let searchQuery = $("#searchBar").serialize();
    $.get("sbAdd", searchQuery, function(resultData){handleSearchQuery(resultData);});
}

function handleSearchQuery(resultData) {
    $("#resultDiv").show();
    searchR.html("");

    console.log(resultData.length);console.log(resultData);


    // let data = JSON.parse(resultData);
    // console.log("getForm: ");console.log(resultData);console.log("json data: ");console.log(data);
    let rowEntry = '<div class="container>';
    if(resultData.length === 0){
        console.log("is oo");
        rowEntry += '<div class="card" style="margin:5%;padding:5%;width:80%;"><p>Sorry. We currently do not have any house data in the area</p></div></div>';
        searchR.append(rowEntry);
    }
    else{
        for (let i = 0; i < resultData.length; i++) {
            rowEntry += '<div class="card" style="margin-top:10%;width:90%;">';
            rowEntry += '<div class="card"><img src="' + resultData[i]['image'] + '" style="width:400px;height:300px;" alt="Image">' + '</div>';
            rowEntry += '<div>' + 'Address: ' + resultData[i]['address'] + '</div>';
            rowEntry += '<div>' + 'Price:   ' + resultData[i]['price'] + '</div>';
            rowEntry += '<div>' + 'Summary: ' + resultData[i]['summary'] + '</div>';
            rowEntry += '<div>' + 'For ' + resultData[i]['categories'] + '</div>';
            rowEntry += '</div>';
        }
        rowEntry += '</div>';
        searchR.append(rowEntry);
    }

    return resultData;
}
