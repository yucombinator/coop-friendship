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
    $scope.my_info = [];
    $scope.friend_info = [];
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
    $scope.getTermsSuggestion = function(model){
            $http({
            url: '/postTerms',
            method: "POST",
            data: JSON.stringify({ 'program' : model.name,
                    'faculty' : model.faculty}),
            headers : { 'Content-Type': 'application/json' }  // set the headers so angular passing info as json
        })
        .then(function(response) {
                // success
                model.terms_choices = response.data;
            }, 
            function(response) { // optional
                // failed
                console.log("Failed to fetch terms choices");
            }
        );
    };   
    $http.get('/getPrograms')
       .then(function(res){
          $scope.programs_list = res.data;
        //console.log(res.data);
    });
    $scope.fade = "false"
    $scope.styleRow = function(result){
        if(result == "On Campus") return {'background-color':'#CFFF19'};
        else return {'background-color':'#FC913A'};
    };
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
                $scope.results = data[1];
                console.log($scope.results);
				$scope.fade = "true"
                
            });
    };
});
