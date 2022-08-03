#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return (newlist);
};
