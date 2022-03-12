
/************************************************ FUNCTIONS *******************************************************/
function hello()
{
    console.log("Hello, World!!")
}

hello();


function functionWithArgs(num1,num2)
{
  console.log(num1 + num2)

}

functionWithArgs(2,8);

/**************************************** ALCANCE Y FUNCIONES GLOBALES *************************************/
var myGlobal = 10; //Las variables que se definen fuera de un bloque de funciones tienen alcance global.
                   //Esto significa que se pueden ver en todas partes en su código JavaScript.

function fun1() 
{
  oopsGlobal = 5;   /*Las variables que se declaran sin la palabra clave "var" se crean automáticamente 
                      en el alcance global, es decir, se pueden usar en otras funciones.
                      Esto puede crear consecuencias no deseadas en otra parte de su código 
                      o cuando se vuelve a ejecutar una función. Siempre debes declarar tus variables con var.*/
}

function fun2() {
  var output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopsGlobal != "undefined") {
    output += " oopsGlobal: " + oopsGlobal;
  }
  console.log(output);
}

fun1();
//console.log(oopsGlobal); //Si imprimimos la variable oopsGlobal despues de la funcion donde se declara,
                           //toma la variable como global.
fun2();

/********************************************** ALCANCE Y FUNCIONES LOCALES ***************************************/

/*function myLocalScope() 
{
    var myVar;                                      Las variables que se declaran dentro de una función con "var", 
                                                    así como los parámetros de la función, tienen alcance local . 
                                                    Eso significa que solo son visibles dentro de esa función.
    console.log('inside myLocalScope', myVar);
}
  myLocalScope();
  
  // myVar is not defined outside of myLocalScope
  console.log('outside myLocalScope', myVar);*/

/********************************************* ALCANCE GLOBAL VS ALCANCE LOCAL *****************************/

var outerWear = "T-Shirt";       //Es posible tener variables locales y globales con el mismo nombre. 
                                 //Cuando hace esto, la variable local tiene prioridad sobre la variable global.

function myOutfit() {
  
var outerWear = "sweater";
  return outerWear;           //Cuando la instrucción 'return' se llama en una función, se detiene la ejecución de esta. 
                              //Si se especifica un valor dado, este se devuelve a quien llama a la función.
}                             //Si se omite 'return', undefined es devuelto en su lugar.


console.log(myOutfit());

/************************************************ RETORNAR UN VALOR DE UNA FUNCION ****************************/
function operation(num)
{
    return num * 2;
}

console.log(operation(10));

/***************************************** ASIGNACIÓN CON VALOR DEVUELTO **************************************/
var processed = 0;

function processArg(num) 
{
  return (num + 3) / 5;
}

processed = processArg(7)
console.log(processed);

/********************************************* */
var sum = 0;

function addThree() {
  sum = sum + 3;
}

function addFive(){
  sum = sum +5;
}

addThree();
addFive();

console.log(sum);
/********************************************* EJEMPLO DE QUEUE *********************************************/
function nextInLine(arr, item) 
{
    
    arr.push(item);                 //Agregamos el parametro que se encuentre en item al final del arreglo.
    console.log(arr);
    var remove = arr.shift();      //Eliminamos el primer elemento del arreglo y lo almacenamos en una variable.
    return remove;                 //Retornamos el nuevo valor que se encuentra en la variable que es '1'.
}
  
  // Setup
  var testArr = [1,2,3,4,5];
  
  console.log("Antes: " + JSON.stringify(testArr));
  console.log(nextInLine(testArr, 6));
  console.log("Después: " + JSON.stringify(testArr));
