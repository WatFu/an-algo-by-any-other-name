// I: array of int
// O: int amount of rain
// C:
// E: flat array = 0

var trap = function (rainArr) {
  let stack = [];
  let curr_sum = 0;
  let curr_height = 0;
  let res = 0;
  let i = 0;
  if (rainArr.length === 0) {
    return 0;
  }
  while (i < rainArr.length) {
    if (stack.length === 0) {
      if (rainArr[i] !== 0) {
        stack.push(rainArr[i]);
      }
    } else {
      let tmp = stack.pop();
      if (rainArr[i] <= tmp) {
        stack.push(tmp);
        stack.push(rainArr[i]);
      } else {
        let curr_elements = [];
        while (rainArr[i] >= tmp && stack.length !== 0) {
          curr_elements.push(tmp);
          tmp = stack.pop();
        }
        if (tmp !== curr_elements[curr_elements.length - 1]) {
          curr_elements.push(tmp);
        }
        if (curr_elements.length === 1) {
          stack = [rainArr[i]];
        } else {
          if (rainArr[i] >= curr_elements[curr_elements.length - 1] && stack.length === 0) {
            for (let k = 0; k < curr_elements.length - 1; k += 1) {
              res += (curr_elements[curr_elements.length - 1] - curr_elements[k]);
            }
            curr_sum = 0;
            stack = [rainArr[i]];
          } else {
            if (rainArr[i] >= curr_height) {
              curr_sum = 0;
            }
            for (let k = 0; k < curr_elements.length - 1; k += 1) {
              curr_sum += (rainArr[i] - curr_elements[k]);
              curr_height = rainArr[i];
            }
            stack = [...stack, ...curr_elements.reverse()];
            stack.push(rainArr[i]);
          }
        }
      }
    }
    i += 1;
  }
  return res + curr_sum;
};