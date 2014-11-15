// declare a module
var app = angular.module('CoopFriend', ['ui.bootstrap']);


app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.controller('MainCtrl', function($scope, $http) {

  $scope.selected = undefined;
  // Any function returning a promise object can be used to load values asynchronously
  $scope.getStreamSuggestion = function(val) {
    return $http.get('/postSubmit').then(function(response){
      return response.data.results.map(function(item){
        return item.programs;
      });
    });
  };
    $scope.test_programs = [];

    $http.get('/getPrograms')
       .then(function(res){
          $scope.test_programs = res.data;
        //console.log(res.data);
    });
    

    // process the form
    $scope.processForm = function() {
        $http({
            method  : 'POST',
            url     : '/postSubmit',
            data    : {my_program:$scope.my_info.name,
                       my_faculty:$scope.my_info.faculty,
                       my_term:$scope.my_info.my_term,
                       my_stream:$scope.my_info.stream,
                       friend_program:$scope.friend_info.name,
                       friend_faculty:$scope.friend_info.faculty,
                       friend_program:$scope.friend_info.my_term,
                       friend_program:$scope.friend_info.stream},
            headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function(data) {
                console.log(data);

                if (!data.success) {
                    // if not successful, bind errors to error variables
                    $scope.errorName = data.errors.name;
                    $scope.errorSuperhero = data.errors.superheroAlias;
                } else {
                    // if successful, bind success message to message
                    $scope.message = data.message;
                }
            });
    };
});
