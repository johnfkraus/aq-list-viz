// js/testXML.js
//In addition to the chai package, you need to install the plugin :
//  npm install chai-xml --save-dev

var chai = require('chai');
var expect = require('chai').expect;
var chaiXml = require('chai-xml');

//loads the plugin
chai.use(chaiXml);

describe('assert some xml', function () {

  var someXml = '<root>\n\t<child name="foo" value="bar"></child>\n</root>';
  var otherXml = '<root><child value="bar" name="foo" /></root>';

  it("should be valid", function () {
    expect(someXml).xml.to.be.valid();
  });

  it("should be the same string as otherXml ", function () {
    expect(someXml).to.not.equal(otherXml);
  });
  it("should be the same XML as otherXml ", function () {
    expect(someXml).xml.to.equal(otherXml);
  });
});

/*
 Usage


 XML must be a string
 Add the property xml to your chain
 The equal/eq/equals methods compare XML instead of the strings
 The valid method check whether the XML is well-formed
 Contributing

 Any contribution is welcome! Please check the issues. Do some unit tests as far as possible.

 Release History

 0.1.0 initial release. Support xml property, valid method and overwrite the equal/eq/equals methods
 License

 Copyright (c) 2014 Bertrand Chevrier
 Licensed under the MIT license.

 npm install chai-xml
 Package Info

 0.2.0 published 3 months ago by krampstudio
 github.com/krampstudio/chai-xml
 MIT license
 Stats

 chai, xml, test, assert, assertion, assertXml

 Dependencies (2)

 chai, xml2js

 Maintainer
 */