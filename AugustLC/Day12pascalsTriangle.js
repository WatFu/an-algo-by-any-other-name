var getRow = function(rowIndex) {
    let res = [];
    
    
    for (let i = 0; i < rowIndex + 1; i += 1) {
        let tmp = res.slice();
        for (let j = 1; j < i; j += 1) {
            res[j] = tmp[j - 1] + tmp[j];
        }
        res.push(1);
    }
    
    return res;
};
