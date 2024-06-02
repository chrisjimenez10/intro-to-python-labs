//Reverse It
const reverseIt = () => {
    let string = "a man, a plan, a canal, frenemies!";
  
    let reverse = "";
  
    for (let i=0; i < string.length; i++) {
      reverse += string[string.length - (i+1)];
    };
  
    console.log(reverse);
  };
// reverseIt();

// Swap Em
const swapEm = () => {
    let a = 10;
    let b = 30;
    let temp;
  
    temp = b;
    b = a;
    a = temp;
  
    console.log("a is now " + a + ", and b is now " + b);
  };
// swapEm();

//Multiply Array/List
const multiplyArray = (ary) => {
    if (ary.length == 0) { return 1; };
  
    let total = 1;
    // let total = ary[0];
  
    for (let i=0; i < ary.length; i++) {
      total = total * ary[i];
    };
    
    console.log(total)
    return total;
  };
// multiplyArray([1, 2, 3, 4]);

//Nth Fibonacci
const nthFibonacciNumber = () => {
let fibs = [1, 1];
let num = prompt("which fibonacci number do you want?");

while (fibs.length < parseInt(num)) {
    let length = fibs.length;
    let nextFib = fibs[length - 2] + fibs[length - 1];
    fibs.push(nextFib);
}

console.log(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
};
// nthFibonacciNumber();

//Search
const searchArray = (array, value) => {
    
    for(let i = 0; i < array.length; i++) {
        if(array[i] == value) {
        return true;
        }
    }
    return false;
};
const myArray = [1, 2, 3]
// console.log(searchArray(myArray, 4))

//Palindrome
const isPalindrome = (str) => {
    for(let i = 0; i < str.length/2; i++){
      if(str[i] != str[str.length-i-1]){
        return false;
        break;
      }
    }
    return true;
  };
// console.log(isPalindrome("civic"))

const hasDupes = (arr) => {
    let obj = {};
    for (i = 0; i < arr.length; i++) {
      if(obj[arr[i]]) {
        return true;
      }
      else {
        obj[arr[i]] = true;
      }
    }
    return false;
  };

// console.log(hasDupes([1, 2, 3,]))

