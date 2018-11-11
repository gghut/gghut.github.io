angular.module('blog', ['ui.router'])
    .controller('listController', [
        '$scope',
        '$http',
        '$stateParams',
        function ($scope, $http, $stateParams) {
            $scope.page_index = function(index){
                $http.get('data/list/'+index+'.json')
                .then(function (result) {
                    if (result.status == 200) {
                        $scope.list = result.data.list;
                    } else {
                        console.log(result.status)
                    }
                }).catch(function () {
                    console.log('error')
                })
            }
            $scope.page_index(1)
        },
    ])
    .config(function ($urlRouterProvider, $stateProvider) {
        $urlRouterProvider.otherwise('/index');
        $stateProvider.state('index', {
            url: '/index',
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