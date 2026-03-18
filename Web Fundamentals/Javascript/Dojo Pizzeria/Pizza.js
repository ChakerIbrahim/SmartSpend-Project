function pizzaOven(CrustType, sauseType, cheeseType,toppings){
    var pizza = {};
pizza.CrustType = CrustType;
pizza.sauseType = sauseType;
pizza.cheeseType = cheeseType;
pizza.toppings = toppings;

return pizza;
}

var pizza1 = pizzaOven
("deep dish","traditional",['mozzarella'],['pepperoni','sausage'])
console.log(pizza1);

var pizza2 = pizzaOven
("hand tossed",'marinara',["mozzarella",'feta'],['mushrooms','olives','onions'])
console.log(pizza2);

var pizza3 = pizzaOven
("hand tossed",'fourSeason','mozzarlla',['olives','corn','pepper','mushrooms','salami'])

var pizza4 = pizzaOven
('hand tossed','barbeque',['goda','mozzarlla'],['chiken','mushrooms','extra barbeque sause'])

console.log(pizza3);
console.log(pizza4);

function randomPizza(){
    var crusts = ["deep dish", "thin crust", "hand tossed", "stuffed crust"];
    var sauces = ["traditional", "marinara", "bbq", "alfredo"];
    var cheeses = ["mozzarella", "cheddar", "feta", "parmesan"];
    var toppings = ["pepperoni", "sausage", "mushrooms", "olives", "onions", "chicken", "bacon"];
    
    var pizza ={};

    pizza.crustType = crusts[Math.floor(Math.random() * crusts.length)];
    pizza.sauseType = sauces[Math.floor(Math.random() * sauces.length)];
    pizza.cheeseType = cheeses[Math.floor(Math.random()* sauces.length)];
    pizza.toppings = toppings[Math.floor(Math.random() * toppings.length)];

    return pizza;

}
 var random = randomPizza()
console.log(random);




