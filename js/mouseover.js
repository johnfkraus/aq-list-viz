
function doMouseover(x) {
  console.log(x.innerHTML);
  id = x.innerHTML;

  x.style.height = "64px";
  x.style.width = "64px";
}

function unMouseover(x) {
  console.log(x.innerHTML);
  x.style.height = "32px";
  x.style.width = "32px";
}

$(".refNumLink")
  .mouseover(function () {
    var searchTermId;
    searchTermId = $(this)
      .val();
    console.log("searchTermId: " + searchTermId);
    return myNetwork.updateSearchId(searchTermId);
  });