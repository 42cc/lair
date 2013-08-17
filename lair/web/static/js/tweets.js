'use strict';

angular.module('LairApp', ['TweetServices']);

angular.module('TweetServices', ['ngResource'])
    .factory('Tweets', function($resource) {
        return $resource('/data/tweets/?last_id=:last_id', {}, {
            query: {method: 'GET', params: {last_id:'all'}, isArray: true}
        });
    });

function TweetListCtrl($scope, $http, $timeout, Tweets) {
    $scope.tweets = [];
    var last_id = 'all';

    (function tick(){
        Tweets.query({last_id: last_id}, function(data){
            $scope.tweets = data.concat($scope.tweets);
            if (data.length > 0) {
                last_id = data[0].id_str;
            }
            $timeout(tick, 5000);
        });
    })()
}
