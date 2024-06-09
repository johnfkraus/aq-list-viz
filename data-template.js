let rawJsonData = `{


`

const regex = /\\/g;
const subst = ``;
const jsonData = rawJsonData.replace(regex, subst);
//console.log('Substitution result: ', result);
// let myJsonData =  rawJsonData.replace(/\\/g, '\\');
//
// myJsonData =  rawJsonData.replace(/\/\'/g, "'");
JSON.parse(jsonData);
