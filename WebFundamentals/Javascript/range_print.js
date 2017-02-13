function RangePrint(start,skip,end){
    end = end || null
    skip = skip || 1

    if (end === null) {
      end = start;
      start = 0;
    }

    for (var i = start; i < end; i+=skip){
    console.log(i)
    }


  // var i = start;
  // while(i < end)
  //   console.log(i)
  //   i = i + skip;
}

RangePrint(-5)
