//this fails in case of .* being null

function isMatch(text, pattern) {
  let t_pointer = 0;
  let p_pointer = 0;
  
  while (p_pointer < pattern.length) {
    if (pattern[p_pointer] === '.') {
      if (pattern[p_pointer + 1] === '*') {
        let curr_letter = text[t_pointer];
        while (text[t_pointer] === curr_letter) {
          t_pointer += 1;
        }
        p_pointer += 2;
      }
       else {
        t_pointer += 1;
        p_pointer += 1;
       }
    } else if (pattern[p_pointer + 1] === '*') {
      while (text[t_pointer] === pattern[p_pointer]) {
        t_pointer += 1;
      }
      p_pointer += 2;
    } else {
      if (text[t_pointer] !== pattern[p_pointer]) {
        return false;
      }
      t_pointer += 1;
      p_pointer += 1;
    }
  }
  return t_pointer === text.length
}
