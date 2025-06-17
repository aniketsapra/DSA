var backspaceCompare = function(s, t) {
    let s1 = []
    let s2 = []

    for (let ch of s){
        if (ch === "#"){
            s1.pop()
        } else {
            s1.push(ch)
        }
    }

    for (let ch of t){
        if (ch === "#"){
            s2.pop()
        } else {
            s2.push(ch)
        }
       
    }

    return s1.join('') === s2.join('');
};