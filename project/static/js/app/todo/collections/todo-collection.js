define(function( require, exports, module ){

var backbone = require('backbone');
var Todo = require('../models/todo').Todo;

var TodoCollection =  backbone.Collection.extend({
    model: Todo,
    url: '/api/v1/todoitem/',

    parse: function(data){
        return data.objects;
    },

    initialize: function(){

    },

    getCompleted: function(){
        return this.filter(isCompleted);
    },

    getActive: function(){
        return this.reject(isCompleted);
    },
});

exports.TodoCollection = TodoCollection;

});
