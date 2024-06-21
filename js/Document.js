function Document() { // }, width) {

  var consoleLogDocument = true,
    //that = this,
    desiredDocsHeight = 200,
    topStuffNegativeMargin = 10,
    topStuffHeight = 85;

  hideDocument();

  function hideDocument() {
    console.log("41 hello from Document.js hideDocument()");
    $('#doc-close').css('display', 'none');
    $('#doc-container').hide();
    resize(false);
  }

  function resize(showDoc) {
    console.log('Document.js 51 resize(showDoc = ', showDoc, ')');
    var docHeight = 0,
      svgHeight = 0;

    var topStuffDisplay = $("#top-stuff").css("display"); // .style(); // .getAttribute("display");
    // console.log($("#top-stuff").css("display")); // none or ?
    if (topStuffDisplay == "none") {
      console.log("topstuff display = none, ", topStuffDisplay);
      topStuffHeight = 0;
    } else {
      console.log("topstuff display = ", topStuffDisplay);
      topStuffHeight = 85; // $("#top-stuff").height();
    }

    svgHeight = window.innerHeight - docHeight - topStuffHeight - topStuffNegativeMargin;
    // console.log("svgHeight: ", svgHeight, " = window.innerHeight: ", window.innerHeight, " - docHeight: ", docHeight, " - topStuffHeight: ", topStuffHeight, ", - topStuffNegativeMargin: ", topStuffNegativeMargin);

    // svgHeight = window.innerHeight - docHeight - $('#top-stuff').height() + topStuffNegativeMargin;
    $('#svg').css('height', svgHeight + 'px');
    if (window.innerWidth < 900) {
      $('.mainTitleDiv').css('font-size', '14px');
    }

    if (consoleLogDocument) {
      // console.log('Document.js window.innerHeight = ', window.innerHeight, '; desiredDocsHeight = ', desiredDocsHeight, '; topStuffHeight = ', $('#top-stuff').height(), '; svgHeight = ', svgHeight, '\nwindow.innerWidth = ', window.innerWidth, '; docHeight = ', docHeight);

      console.log('Document.js window.innerHeight = ', window.innerHeight, '; desiredDocsHeight = ', desiredDocsHeight, '; topStuffHeight = ', topStuffHeight, '; svgHeight = ', svgHeight, '\nwindow.innerWidth = ', window.innerWidth, '; docHeight = ', docHeight);
    }
  }

  return {
    hideDocument: hideDocument,
    resize: resize
  }
}
