// input array
// output new array with only numbers;

var arr = [1, "apple", -3, "orange", 0.5];

function onlyNums(arr){

  var nums=[];
  for(var i = 0; i < arr.length; i++){
    if(typeof arr[i] === "number"){
      nums.push(arr[i])
    }
  }
  return nums;
}

console.log(onlyNums(arr))
