/**************************************************** Golf Code ********************************************/
const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore(par, strokes) {
  // Only change code below this line
  if (par==par && strokes == 1){
    return names[0]
  } 
  else if (par==par && strokes <= (par -2)){
    return names[1]
  }
  else if(par==par && strokes == (par-1)){
    return names[2]
  }
  else if(par==strokes){
    return names[3]
  }
  else if(par== par && strokes == (par+1)){
    return names[4]
  }
  else if(par== par && strokes == (par+2)){
    return names[5]
  }
  else if(par==par && strokes >= (par+3)){
    return names[6]
  }
  else{
    return "Change Me";}
}

console.log(golfScore(8,1))