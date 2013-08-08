describe('Tweets', function() {

    describe('TweetListCtrl', function(){
        var scope, ctrl, $httpBackend;

        // The injector ignores leading and trailing underscores here (i.e. _$httpBackend_).
        // This allows us to inject a service but then attach it to a variable
        // with the same name as the service.
        beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.expectGET('/data/tweets/').
                respond([
                    {"id": 365205651267416064, "text": "test1"},
                    {"id": 365205746851393536, "text": "test2"},
                    {"id": 365215008914800640, "text": "test3"},
                ]);

            scope = $rootScope.$new();
            ctrl = $controller(TweetListCtrl, {$scope: scope});
        }));

        it('should create "tweets" model with 3 items fetched', function() {
            expect(scope.tweets).toBeUndefined();
            $httpBackend.flush();
            expect(scope.tweets.length).toEqual(3);
            expect(scope.tweets[0].text).toEqual('test1');
        });
    });
});
