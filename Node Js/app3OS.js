//Módulo OS

const os = require('node:os');

console.log(os.type());
console.log(os.arch());
console.log(os.release());
console.log(os.cpus());
console.log(os.freemem());
console.log(os.totalmem());
console.log(os.platform());