/*--- print Numbers ---*/
for(i=1;i<=10;i++){
    console.log(i);
}

/*--- Reverse Number---*/
for(i=10;i>=1;i--){
    console.log(i);
}

/*---Even Number---*/
for(i=1;i<=20;i++){
    if(i%2==0){
        console.log(i);
    }
}

/*---Odd Number---*/
for(i=1;i<=20;i++){
    if(i%2==1){
        console.log(i);
    }
}
/*---Sum of number---*/
let sum =0;
for(i=1;i<=10;i++){
sum +=i;  
console.log(sum);    
}

/*---FizzBuzz---*/
for(i=1;i<=30;i++){
    if(i%5==0 && i%3==0){
        console.log("FizzBuzz");
    }
    else if(i%5==0){
        console.log("Buzz");
    }
    else if(i%3==0){
        console.log("Fizz")
    }
    else {
        console.log(i);
    }
}

