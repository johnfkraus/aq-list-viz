function scsearchquery() {
    let search_query = document.getElementById("searchbox").value;
    let cards = document.querySelectorAll('.box');
    for (var i = 0; i < cards.length; i++) {
        if(cards[i].textContent.toLowerCase()
                .includes(search_query.toLowerCase())) {
            cards[i].classList.remove("sc-display-none");
        } else {
            cards[i].classList.add("sc-display-none");
        }
    }
  }