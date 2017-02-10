// //input arbitrary number of quarter
// //output win return the numbe of quarter
//
//
function slots(num){
  var wins = 0;

  for(var i = num; i > 0; i--){
    if(Math.floor((Math.random() * 100) + 1) === 7){
      wins = i + getRandomInt(50,100);
      break;
    }
  }
  return wins;
};


function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}


console.log(slots(50));


// function slots(){
//   var wins = 50;
//
//   var i =50
//   while(i>0){
//     if(Math.floor((Math.random()*100)+1) === 30){
//       wins =  wins + (Math.floor((Math.random()*50)+1))
//       break;
//     }
//     i--;
//   }
//   console.log(i)
//   return wins;
//   }
//

// console.log(getRandomInt(50,100));
