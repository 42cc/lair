'use strict';

angular.module('LairApp', ['TweetServices']);

angular.module('TweetServices', ['ngResource'])
    .factory('Tweets', function($resource) {
        return $resource('/data/tweets/?last_id=:last_id', {}, {
            query: {method: 'GET', params: {last_id:'all'}, isArray: true}
        });
    });

function TweetListCtrl($scope, $http, Tweets) {
    $scope.tweets = Tweets.query();
}

// TweetListCtrl.$inject = ['$scope', '$http', 'Tweets']
