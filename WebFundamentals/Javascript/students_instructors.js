var stu = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function namePrint(arr){
  for(var i = 0; i < arr.length; i++){
    console.log(arr[i].first_name + " " + arr[i].last_name)
  }
}

namePrint(stu);