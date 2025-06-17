var maxProfit = function(prices) {
    min_price = Infinity;
    max_profit = 0;

    for( let price of prices ){
        if( price < min_price ){
            min_price = price;
        } else {
            let profit = price - min_price;
            if( profit > max_profit){
                max_profit = profit;
            }
        }
    }
    return max_profit
};

// with math functions
function maxProfit(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    }

    return maxProfit;
}
