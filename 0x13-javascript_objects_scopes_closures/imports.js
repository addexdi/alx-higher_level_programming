#!/usr/bin/node
let biz = function func (){};
biz.prototype.log = function(){
    console.log('Anonymous func');
}

module.exports = new biz();