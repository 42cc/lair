describe('Tweets', function() {

    beforeEach(function(){
        this.addMatchers({
            toEqualData: function(expected) {
                return angular.equals(this.actual, expected);
            }
        });
    });

    beforeEach(module('TweetServices'));

    describe('TweetListCtrl', function(){
        var scope, ctrl, $httpBackend, $timeout;

        // The injector ignores leading and trailing underscores here (i.e. _$httpBackend_).
        // This allows us to inject a service but then attach it to a variable
        // with the same name as the service.
        beforeEach(inject(function(_$httpBackend_, $rootScope, $controller, _$timeout_) {
            $httpBackend = _$httpBackend_;
            $timeout = _$timeout_;
            $httpBackend.when('GET', '/data/tweets/?last_id=all')
                .respond([
                    {"id_str": "365205651267416064", "text": "test1"},
                    {"id_str": "365205746851393536", "text": "test2"},
                    {"id_str": "365215008914800640", "text": "test3"},
                ]);

            scope = $rootScope.$new();
            ctrl = $controller(TweetListCtrl, {$scope: scope});
        }));

        it('should create "tweets" model with 3 items fetched', function() {
            expect(scope.tweets).toEqual([]);
            expect(scope.last_id).toEqual('all');
            $httpBackend.flush();
            expect(scope.tweets.length).toEqual(3);
            expect(scope.tweets[0].text).toEqual('test1');
            expect(scope.last_id).toEqual('365205651267416064');
        });

        it('should get one more tweet from update', function() {
            $httpBackend.flush();
            $httpBackend.when('GET', '/data/tweets/?last_id=365205651267416064')
                .respond([
                    {"id_str": "365205651267417742", "text": "test4"},
                ]);
            $timeout.flush();
            $httpBackend.flush();
            expect(scope.tweets.length).toEqual(4);
            expect(scope.tweets[0].text).toEqual('test4');
            expect(scope.last_id).toEqual('365205651267417742');
        });
    });
});
