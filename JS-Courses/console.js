var hola = "Hola, Mundo!";
console.log(hola.length);  //Puede encontrar la longitud de un String escribiendo .length
                           //después de la variable de cadena.

var lastName = "Lovelace";

firstLetterOfLastName = lastName[lastName.length -1]; 
console.log(firstLetterOfLastName);

/************************************************ ARRAYS *************************************************/
var array = [['Enrique', 26],["Dany",25]];
console.log(array[1][0]);

var myArray = [50,60,70];
var myData = myArray[0];
console.log(myData);

var myArray = [
                [1,2,3],             //Indice 0
                [4,5,6],             //Indice 1
                [7,8,9],             //Indice 2
                [[10,11,12], 13, 14] //Indice 3, con 3 arrays dentro
              ];

var myData = myArray[3][2];
console.log(myData);

var myArray = [["John", 23], ["cat", 2]];
myArray.push(["dog", 3])  //La función .push(); toma uno o más parámetros y los "empuja" al final de la matriz.

var f = "azure";
console.log(f.length);
console.log(f[f.length - 1]);

var Remove = myArray.pop(); //La funcion .pop(); elimina el último elemento de una matriz y devuelve ese elemento.
console.log(Remove);
console.log(myArray);

var Removed = myArray.shift(); //La funcion .shift(); elimina el primer elemento de una matriz y devuelve ese elemento.
console.log(Removed);
console.log(myArray);

var myArray_1 = [["John", 23], ["dog", 3]];
myArray_1.shift();                          //eliminamos el primer elemnto del arreglo
myArray_1.unshift(["Paul",35]); //.unshift() funciona exactamente igual .push(), pero en lugar de agregar 
                              // el elemento al final de la matriz, unshift() agrega el elemento al principio de la matriz.
console.log(myArray_1)

console.log(typeof(f));

const FCC = "freeCodeCamp";      //Declaramos una variable constante, lo que significa que no se puede reasignar su valor
let fact = "is cool!";           //Declaramos una variable let que mas adelante cambiará de valor
fact = "is awesome!";
console.log(FCC, fact);

//Nota: No se puede declarar dos veces la misma variable con let
//let variable = "Luis";      
//let variable = "Enrique";//