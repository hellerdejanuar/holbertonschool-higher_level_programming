#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cn = 0;
  list.forEach(function (element) {
    if (element === searchElement) {
      cn++;
    }
  });
  return (cn);
};
