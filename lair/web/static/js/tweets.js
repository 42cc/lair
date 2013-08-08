'use strict';

function TweetListCtrl($scope, $http) {
    $http.get('/data/tweets/').success(function(data) {
        $scope.tweets = data;
    });
}

TweetListCtrl.$inject = ['$scope', '$http']
