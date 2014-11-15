// declare a module
var app = angular.module('CoopFriend', ['ui.bootstrap']);


app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.controller('MainCtrl', function($scope, $http) {

  $scope.selected = undefined;
  /* Any function returning a promise object can be used to load values asynchronously
  $scope.getStreamSuggestion = function(val) {
    return $http.get('/postSuggestion').then(function(response){
      return response.data.results.map(function(item){
        return item.programs;
      });
    });
  }; */
    $scope.test_programs = [];

    $scope.getStreamSuggestion = function(model){
            $http({
            url: '/postSuggestion',
            method: "POST",
            data: JSON.stringify({ 'program' : model.name,
                    'faculty' : model.faculty}),
            headers : { 'Content-Type': 'application/json' }  // set the headers so angular passing info as json
        })
        .then(function(response) {
                // success
                model.stream_choices = response.data;
            }, 
            function(response) { // optional
                // failed
                console.log("Failed to fetch stream choices");
            }
        );
    };
    
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
            data    : JSON.stringify({my_program:$scope.my_info.name,
                       my_faculty:$scope.my_info.faculty,
                       my_term:$scope.my_info.term,
                       my_stream:$scope.my_info.stream,
                       friend_program:$scope.friend_info.name,
                       friend_faculty:$scope.friend_info.faculty,
                       friend_term:$scope.friend_info.term,
                       friend_stream:$scope.friend_info.stream}),
            headers : { 'Content-Type': 'application/json' }  // set the headers so angular passing info as form data (not request payload)
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
