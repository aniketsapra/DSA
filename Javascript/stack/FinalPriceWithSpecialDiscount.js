var finalPrices = function(prices) {
    let stack = [];
    let result = [...prices];

    for (let i = 0; i < prices.length; i++) {
        while (stack.length && prices[stack[stack.length - 1]] >= prices[i]) {
            let j = stack.pop();
            result[j] = prices[j] - prices[i];
        }
        stack.push(i);
    }

    return result;
};
