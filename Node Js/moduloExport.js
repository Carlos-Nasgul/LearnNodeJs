function sumar(a, b) {
    return a + b;
}

function saludar(nombre) {
    return `Hola ${nombre}`;
}

//module.exports.suma = sumar;
//module.exports.saludar1 = saludar;

module.exports = {
    saludar1: saludar,
    suma: sumar

}