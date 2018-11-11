angular.module('blog', ['ui.router'])
    .controller('listController', [
        '$scope',
        '$http',
        '$stateParams',
        function ($scope, $http, $stateParams) {
            $http.get('data/list/'+$stateParams.page+'.json')
                .then(function (result) {
                    if (result.status == 200) {
                        $scope.list = result.data.list;
                        $scope.count = result.data.count;
                        $scope.countRange = new Array(result.data.count);
                        $scope.pageIndex = $stateParams.page;
                    } else {
                        console.log(result.status)
                    }
                }).catch(function () {
                    console.log('error')
                })
        },
    ])
    .config(function ($urlRouterProvider, $stateProvider) {
        $urlRouterProvider.otherwise('/index/0');
        $stateProvider.state('index', {
            url: '/index/:page',
            views: {
                'header': {
                    templateUrl: 'layout/header.html'
                },
                'content': {
                    templateUrl: 'layout/list.html',
                    controller: 'listController'
                },
                'footer': {
                    templateUrl: 'layout/footer.html'
                }
            }
        })
    });