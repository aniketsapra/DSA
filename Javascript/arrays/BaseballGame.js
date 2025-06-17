// Easy
// Stack

var calPoints = function(operations) {
   let total = 0;
   let stack = [];
   for( let i = 0; i < operations.length; i++){
    if( operations[i] == "+" ){
       let plus = stack[stack.length - 1] + stack[stack.length - 2];
       stack.push(plus);
    } else if( operations[i] == "D" ){
        let d = stack[stack.length - 1] * 2;
        stack.push(d);
    } else if ( operations[i] == "C" ){
        stack.pop();
    } else {
        stack.push( parseInt(operations[i]) );  // to convert string into integer
    }
   }

   for( let j = 0; j < stack.length; j++){
    total += stack[j]
   }
   return total
};



var calPoints = function(operations) {
            //x = new score
        //+ = new score that is sum of prev 2 scores
        //D = new score that is double of previous score
        //C = invalidate the previous score, removing it from record
        //Return the sum of all the scores on the record after applying all the operations

        let record = []
        for(let i= 0; i < operations.length; i++) {
            if(operations[i] == "+") {
                //add new score that is sum of previous 2 scores
                let last = record[record.length - 1]
                let secondLast = record[record.length - 2]
                record.push(last+secondLast)
                
            } else if(operations[i] == "D"){
                //add new score that is double the last score
                let last = record[record.length - 1]
                record.push(last * 2)
            } else if(operations[i] == "C") {
                //invalidate previous score by removing it
                record.pop()
            } else {
                // add new score
                record.push(parseInt(operations[i], 10))
            }
        }

        let total = 0
        for(let i = 0; i < record.length; i++) {
            total += record[i]
        }
        return total
};