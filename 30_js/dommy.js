// Team Big KAraZIes -- Tim Marder & Ahnaf Kazi
// SoftDev pd06
// K #30: Sequential Progression III: Season of the Witch
// 2018-12-21

var thelist = document.getElementById('thelist');
var head = document.getElementById('h');
var addbutt = document.getElementById('b');
var fibbutt = document.getElementById('fb');
var fibcount = 0;

var fibonacci = (n) => {

    if (n == 0) { //base case
        return 0;
    }
    if (n == 1){ //the 1th number is 1 so 1+0 = 1
        return 1;
    }
    else { //all other cases
        return fibonacci(n-2) + fibonacci(n - 1); //adds number and the one before it
    }
}

//Sets header to "Hello World!" at mouseout.
thelist.addEventListener('mouseout',
			 function(e){
			     head.innerHTML = "Hello World!";
			 }
			);

//changes header when hovering over list
thelist.addEventListener('mouseover',
			 function(e){
			     head.innerHTML = e.target.innerHTML;
			 }
			);

//removes list element on click
thelist.addEventListener('click',
			 function(e){
			     e.target.remove();
			 }
         );

//adds PISTACIOS to the list
addbutt.addEventListener('click',
			 function(e){
			     var kid = document.createElement('li');
			     kid.innerHTML = "PISTACHIOS";
			     thelist.appendChild(kid);
			 }
         );


var listtoo = document.getElementById('fiblist');

//adds fib to the list
fibbutt.addEventListener('click',
			 function(e){
			     var kid = document.createElement('li');
			     kid.innerHTML = fibonacci(fibcount);
			     fibcount++;
			     listtoo.appendChild(kid);
			 }
         );
