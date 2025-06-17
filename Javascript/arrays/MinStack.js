var MinStack = function() {
    this.Stack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    return this.Stack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    return this.Stack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
   return this.Stack[this.Stack.length-1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return Math.min(...this.Stack);
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */