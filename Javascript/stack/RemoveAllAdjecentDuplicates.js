// easy
// stack

var removeDuplicates = function(s) {
    let stack = []
    for(let ch of s){
        if ( ch === stack[stack.length-1] && stack.length > 0){
            stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.join(''); 
};