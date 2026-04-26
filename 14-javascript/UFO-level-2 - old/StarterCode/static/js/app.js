// from data.js
var tableData = data;

//// Get a reference to the table body
var tbody = d3.select("tbody");

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


// filter
var button = d3.selectAll(".dropdown-item");


button.on("click", function() {

// Select the input element and get the raw HTML node
    tbody.html("");
    var filterElement = d3.select(this).node().id;
    console.log(filterElement)
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#search");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value").toLowerCase();
    console.log(inputValue);
    var filterData=tableData.filter(tableData => tableData[filterElement] === inputValue);
    renderTable(filterData)
    });
      