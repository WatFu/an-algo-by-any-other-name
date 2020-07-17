// I: ring array of letters size 1-100 can be duplicates, key letter 1-100
// O: minimum number of steps to input key
// C: can only spin clockwise and countercw cant rnadomly go to letters, always can spell
// E: 0 string or 1 letter rings

// const ringRoutes = (ring, key) => {
//   const makeObjRoutes = () => {
//     let h = {}
//     for (let i = 0; i < ring.length; i += 1) {
//       h[ring[i]] = {};
//     }

//     let uniqueLetters = Object.keys(h);
//     for (let i = 0; i < uniqueLetters.length; i += 1) {
//       let stack = [];
//       for (let j = 0; j < ring.length; j += 1) {
//         if (ring[j] === uniqueLetters[i]) {
//           stack.push(j);
//         }
//       }

//       for (let k = 0; k < uniqueLetters.length; k += 1) {
//         if (uniqueLetters[k] !== uniqueLetters[i]) {
//           for (let l = 0; l < stack.length; l += 1) {
//             let l_pointer = stack[l];
//             let r_pointer = stack[l];
//             let distance = 0;
//             while (ring[l_pointer] !== uniqueLetters[k] && ring[r_pointer] !== uniqueLetters[k]) {
//               if (l_pointer === 0) {
//                 l_pointer = ring.length - 1;
//               } else {
//                 l_pointer -= 1;
//               }
//               if (r_pointer === ring.length - 1 ) {
//                 r_pointer = 0;
//               } else {
//                 r_pointer += 1;
//               }
//               distance += 1;
//             }
//             h[uniqueLetters[i]][uniqueLetters[k]] = distance;
//           }

//         }

//       }
//     }
//     return h;
//   }

//   let solvedRoutes = makeObjRoutes();

//   const solver = (routeObj) => {
//     let total = key.length - 1;
//     for (let i = 0; i < key.length - 1; i+= 1) {
//       total += routeObj[key[i]][key[i + 1]];
//     }
//     return total;
//   }

//   return solver(solvedRoutes);
// }

// console.log(ringRoutes(['g','o','d','d','i','n','g'], 'gd'));


const ringRoutes = (ring, key) => {
  const makeObjRoutes = () => {
    let h = [];

    for (let i = 0; i < ring.length; i += 1) {
      h[i] = {};
      for (let k = 0; k < ring.length; k += 1) {
        if (ring[k] !== ring[i]) {
          let l_pointer = i;
          let r_pointer = i;
          let l_distance = 0;
          let r_distance = 0;
          while (ring[l_pointer] !== ring[k] && ring[r_pointer] !== ring[k]) {
            if (l_pointer === 0) {
              l_pointer = ring.length - 1;
            } else {
              l_pointer -= 1;
            }
            if (r_pointer === ring.length - 1) {
              r_pointer = 0;
            } else {
              r_pointer += 1;
            }
            r_distance += 1;
            l_distance -= 1;
          }
          if (ring[l_pointer] === ring[k]) {
            h[i][ring[k]] = l_distance;
          } else if (ring[r_pointer] === ring[k]) {
            h[i][ring[k]] = r_distance;
          }

        } else {
          h[i][ring[k]] = 0;
        }
      }
    }
    return h;
  }

  let solvedRoutes = makeObjRoutes();

  let startStack = [];
  for (let i = 0; i < ring.length; i += 1) {
    if (ring[i] === ring[0]) {
      startStack.push(i);
    }
  }

  const solver = (routeObj, startIndex) => {
    let total = key.length;
    let position = startIndex;
    for (let i = 0; i < key.length - 1; i += 1) {
      // console.log('position is ', position,' and obj is ', routeObj[position], 'and key i + 1 is ', key[i + 1])
      total += Math.abs(routeObj[position][key[i + 1]]);
      position += routeObj[position][key[i + 1]];
    }
    return total;
  }

  let finalLength;
  for (let j = 0; j < startStack.length; j += 1) {
    if (finalLength === undefined) {
      finalLength = solver(solvedRoutes, startStack[j]);
    } else {
      newLength = solver(solvedRoutes, startStack[j]);
      if (newLength < finalLength) {
        finalLength = newLength;
      }
    }
  }

  return finalLength;
}

console.log(ringRoutes(['g', 'o', 'd', 'd', 'i', 'n', 'g'], 'godding'));