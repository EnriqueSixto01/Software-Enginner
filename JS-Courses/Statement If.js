function igualdad(valor)            //=== y !=== son operadores con logica estricta que no permite la conversion de
{                                   //tipo de dato como los operadores == o != 
    if(valor == 5){
        return "Es verdadero"}
    else if(valor !=10){
        return "No igual"}
    return "Igual"
}

console.log(igualdad(5));
console.log(igualdad("5"));
console.log(igualdad('10'));

/************************************************ Operator && **************************************************/
function logicOperators(valor)
{
    if(valor >=15 && valor<=30)
        return true
    return false
}

console.log(logicOperators(10));
console.log(logicOperators(18));


/************************************************* Operator || ***************************************************/
function logicOperators_1(valor)
{
    if(valor <=15 || valor >=30)
        console.log("True");
    else
        console.log("False");
}

logicOperators_1(10);
logicOperators_1(18);
logicOperators_1(29);

/**************************************************** SWITCH *************************************************/
function caseInSwitch(val) 
{
    let answer = "";
    
    switch(val)
    {
        case 1:
            answer="alpha"   //Siempre se coloca un break; para finalizar una sentencia, de lo contrario seguiria
            break;           //ejecutandose el programa hasta encontrar un break;
        case 2:                 
            answer ="beta"
            break;
        case 3:
            answer="gamma"
            break;
        case 4:
            answer="delta"
            break;
    }
        return answer;
}
  
  console.log(caseInSwitch(4));
  console.log(caseInSwitch(3));
  console.log(caseInSwitch(2));
  console.log(caseInSwitch(1));
/************************************************ SWITCH con default *************************************************/
function switchOfStuff(val) 
{
    let answer = "";
    
    switch(val)
    {
      case "a":
        answer = "apple"
        break;
      case "b":
        answer = "bird"
        break;
      case "c":
        answer = "cat"
        break;
      default:
        answer = "stuff"
        break;
    }
  
    return answer;
}
  
  console.log(switchOfStuff("b"));
  
/*****************************************Multiple Identical Options in Switch Statements *******************/
function sequentialSizes(val) {
    let answer = "";

    switch(val)
    {
      case 1:
      case 2:
      case 3:
        answer = "Low";
        break;
      case 4:
      case 5:
      case 6:
        answer = "Mid";
        break;
      case 7:
      case 8:
      case 9:
        answer = "High";
    }
    return answer;
  }
  
  console.log(sequentialSizes(1));
  console.log(sequentialSizes(3));
  console.log(sequentialSizes(5));
  console.log(sequentialSizes(8));

  /****************************************** Switch with specific case *************************************/
  function chainToSwitch(val) {
    let answer = "";
    switch(val)
    {
      case "bob":
        answer = "Marley";
        break;
      case 42:
        answer = "The Answer";
        break;
      case 1:
        answer = "There is no #1";
        break;
      case 99:
        answer = "Missed me by this much!";
        break;
      case "John":
        answer = "";
        break;
      case 156:
        answer = "";
        break;
      default:
          answer = "Ate Nine";
  
    }
    
    return answer;
  }
  
  console.log(chainToSwitch("bob"));
  console.log(chainToSwitch(42));
  console.log(chainToSwitch(1));
  console.log(chainToSwitch(99));
  console.log(chainToSwitch(7));

/************************************* Returning Boolean Values from Functions ***********************/
function isLess(a, b) 
{
  return a <= b;
}

console.log(isLess(10, 15));
console.log(isLess(15, 10));

/************************************* Return Early Pattern for Functions ****************************/

function abTest(a, b) 
{
  if (a < 0 || b< 0)
  {
    console.log("undefined");
    return undefined;
  }

    return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

console.log(abTest(2,2));
abTest(-2, 2);
abTest(-8, 3);  

/***************************************** Counting Cards *********************************************/
let count = 0;

function cc(card) 
{
  
  switch(card)
  {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      break;

    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
      break;
  }
  if(count > 0)
  {
    return count + " Bet";
  }
  else
  {
    return count + " Hold"
  }
}


console.log(cc(2),cc(10),cc('K'),cc('A'));
