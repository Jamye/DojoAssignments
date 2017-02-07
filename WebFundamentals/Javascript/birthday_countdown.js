
//output if num>

function birthday(num){
  if(num > 30){
    console.log(num + " Too long ...")
  } else if (num <= 30 && num >= 5){
    console.log(num + " days until my birthday. ;p")
  } else if (num < 5 && num >= 1){
    console.log(num + " almost there!!".toUpperCase());
  } else {
    console.log("happy birthday".toUpperCase());
  }
  }

  birthday(60)
  birthday(31)
  birthday(30)
  birthday(29)
  birthday(5)
  birthday(4)
  birthday(1)
  birthday(0)
