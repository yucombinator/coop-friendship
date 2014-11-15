// declare a module
var app = angular.module('CoopFriend', ['ui.bootstrap']);


app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.controller('MainCtrl', function($scope, $http) {

  $scope.selected = undefined;
  // Any function returning a promise object can be used to load values asynchronously
  $scope.getLocation = function(val) {
    return $http.get('http://maps.googleapis.com/maps/api/geocode/json', {
      params: {
        address: val,
        sensor: false
      }
    }).then(function(response){
      return response.data.results.map(function(item){
        return item.formatted_address;
      });
    });
  };

    $scope.test_programs = [{'name':'Software Engineering','faculty':'engineering','color':'purple', 'require_stream':'false'},{'name':'Actuarial Science','faculty':'math','color':'pink','require_stream':'true'},
    {'name':'Anthropology','faculty':'arts','color':'orange', 'require_stream':'false'}];
    
    // process the form
    $scope.processForm = function() {
        $http({
            method  : 'POST',
            url     : '/postSubmit',
            data    : {my_program:$scope.my_info.name,
                       my_term:$scope.my_info.my_term,
                       my_stream:$scope.my_info.stream,
                       friend_program:$scope.friend_info.name,
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