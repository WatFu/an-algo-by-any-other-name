function isMatch(text, pattern) {
  let t_pointer = 0;
  let p_pointer = 0;
  
  while (p_pointer < pattern.length) {
    if (pattern[p_pointer] === '.') {
      if (pattern[p_pointer + 1] === '*') {
        return true;
      }
      t_pointer += 1;
      p_pointer += 1;
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
