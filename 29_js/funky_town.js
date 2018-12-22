/*
Team Dynamite -- Tim Marder && Mohammed Uddin
SoftDev pd06
K#29 -- Sequential Progression
2018-12-20
*/

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
};

var gcd = ( a , b ) => {

    var result = 1; //placeholder for gcd

    for (var i = 1; (i <= a) && (i <= b); ++i ) { //starts from smallest number

        if ((a % i == 0) && (b % i == 0)) { //checks if both numbers are divisible by the possible gcd

            result = i; //if so, sets the result variable to the number

        }

    }
    return result; //returns the gcd

};

var randomStudent = () => {

    var students = ['Tim', 'John', 'Steven', 'Damian', 'Shin', 'Vincent', 'Ahnaf', 'Britni'];
    //array holding the students' names
    var amount = students.length;
    //variable holding the size of the array
    var random = Math.random();
    //for convenience

    var student = students[Math.floor( random * amount )];
    //random function takes place and student is chosen

    return student;
    //chosen student is returned

};




var disfib = document.getElementById("fib");
var disgcd = document.getElementById("gcd");
var disrandstu = document.getElementById("randstu");

/*
var fibdis = function() {

    //console.log( fibonacci( 20 ) );

    document.getElementById( "fibP" ).innerHTML = fibonacci( 20 );

};
*/

/*
var gcddis = function() {

    console.log( gcd( 224383, 1273 ) );

    document.getElementById( "gcdP" ).innerHTML = gcd( 224383, 1273 );

};
*/

/*
var randstudis = function() {

    console.log( randomStudent() );

    document.getElementById( "randstuP" ).innerHTML = randomStudent();
};
*/

disfib.addEventListener( 'click',
    function( fibdis ) {
        console.log( fibonacci(20) );
        document.getElementById( "fibP" ).innerHTML = fibonacci( 20 );
    }
 );
disgcd.addEventListener( 'click',
    function ( gcddis ) {
        console.log( gcd( 224383, 1273 ) );
        document.getElementById( "gcdP" ).innerHTML = gcd( 224383, 1273 );
    }
);
disrandstu.addEventListener( 'click', randstudis );
