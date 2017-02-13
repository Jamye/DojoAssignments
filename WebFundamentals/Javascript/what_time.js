//input, hour, min, period

//output, just after, almost

function tellTime(hour, min, period){
    if(period === "AM" && min < 30){
        console.log(" It's just after " + hour + " in the morning")
      } else if(period === "AM" && min > 30){
        console.log("It's almost " + (hour + 1) + " in the morning")
      }

    if (period === "PM" && min < 30){
        console.log("It's just after " + (hour) + " in the evening")
      } else if (period === "PM" && min > 30){
        console.log("It's almost " + (hour + 1) + " in the evening")
      }
}


tellTime(4,40,"PM");
