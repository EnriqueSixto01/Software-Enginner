/*Los objetos son usados para almacenar datos de una manera estructurada */
/*Se pueden usar u omitir las comillas para las propiedeades de una sola palabra */
const Guitarra ={
    madera: "Caoba",
    cuerdas: 6,
    trastes: 24,
    marca: "Ibanez",
    color: "Negro Cristal"
};

//Accediendo a las propiedades de un objeto con la notacion punto(.) o la notacion corchete([])
const valuemarca = Guitarra.marca;
const valuecoulor = Guitarra.color;

console.log(valuemarca);
console.log(valuecoulor);