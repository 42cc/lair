basePath = '../../';

files = [
    JASMINE,
    JASMINE_ADAPTER,
    'static/js/lib/angular.js',
    'js_tests/lib/angular-mocks.js',
    'static/js/*.js',
    'js_tests/unit/**/*.js'
];

autoWatch = true;

browsers = ['Chrome'];

junitReporter = {
    outputFile: 'test_out/unit.xml',
    suite: 'unit'
};
