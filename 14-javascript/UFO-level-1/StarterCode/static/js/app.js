// from data.js
var tableData = data;

//// Get a reference to the table body
var tbody = d3.select("tbody");
var button = d3.select("#filter-btn");

// Append table function
function renderTable(d) {
    d.forEach(ufo => {
    var row = tbody.append("tr");
    Object.entries(ufo).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
}

//return table when first load of the index.html
renderTable(tableData);
//filter

button.on("click", function() {

    tbody.html("");
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var filterData=tableData.filter(tableData => tableData.datetime === inputValue);
    renderTable(filterData)
});
  
