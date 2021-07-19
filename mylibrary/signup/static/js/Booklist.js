function searchBy(){
  var element;
  var inputSearch = document.getElementById("search");
  var filter = inputSearch.value.toLowerCase();

  var table = document.getElementById("table");
  var row = table.getElementsByTagName("tr");

  for (var i = 1; i < row.length; i++) 
  {
    element = row[i];
    if (element) 
    {
      textVal = element.textContent || element.innerText;

      if (textVal.toLowerCase().indexOf(filter) > -1) 
      {
        row[i].style.display = "";
      } 
      else 
      {
        row[i].style.display = "none";
      }
    }
  }
}
