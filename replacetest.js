let jsonData = `{
      "narrativeFileName": "TBD",
      "REFERENCE_NUMBER": "QDi.293",
      "name": "ABDUL RAHIM BA\\'AYSIR",
  }`

console.log('jsonData = ', jsonData);
// \\u2018
let myJsonData =  jsonData.replace("//\/\/\\'/g", "'");

// # let myJsonData =  jsonData.replace(/\/\/\\/g, '');
//
console.log("myJsonData = ", myJsonData);



const regex = /\\\\'/gm;

// Alternative syntax using RegExp constructor
// const regex = new RegExp('\\\\\\\\\'', 'gm')

const str = `      "narrativeFileName": "TBD",
      "REFERENCE_NUMBER": "QDi.293",
      "name": "ABDUL RAHIM BA\\\\'AYSIR",
      "name": "ABDUL RAHIM BA\\\\'AYSIR",`;
const subst = `'`;

// The substituted value will be contained in the result variable
const result = str.replace(regex, subst);

console.log('Substitution result: ', result);

// parsed = JSON.parse(myJsonData);
// console.log(parsed);
