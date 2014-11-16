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
    $scope.getTermsSuggestion = function(model, stream){
            $http({
            url: '/postTerms',
            method: "POST",
            data: JSON.stringify({ 'program' : model.name,
                    'stream' : stream,
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
                $scope.error = "Term Error";
            }
        );
    };   
    $http.get('/getPrograms')
       .then(function(res){
          $scope.programs_list = res.data;
        //console.log(res.data);
    });
    $scope.fade = "false";

    $scope.onStream = function(result){
        var on = 0;
        var total = 0;

        for (i = 0;  i < result.length; i++){
            total++;
            if (result[i]=="Yes"){
                on++;
            }
        }
        percentage = on/total*100;
        percentage = Math.round(percentage);
        random = Math.floor((Math.random() * 100) + 1);
        if (percentage == 0){
            if (random %2 == 0)
                return "Were you even serious? - 0%. Zero percent. Let me say that again. ZERO PERCENT. What were you thinking?";
            else
                return "Are you sure you two aren't roommates?";
        }
        else if (percentage < 10){
            return "Sorry partner. Looks like you'll have to find someone else - " + String(percentage) + "% of the time won't cut it.";
        }
        else if (percentage < 30){
            if(random%2 == 0)
                return "Fat chance. You can only sublet " + String(percentage) + "% of the time anyways.";
            else
                return "It's not you. It's me. You can only sublet " + String(percentage) + "% of the time.";
        }
        else if (percentage >= 70){
            if(random%2 == 0)
                return "Sublet. Now. Trust us on this one, you've got " + String(percentage) + "% of the next 5 years taken care of.";
            else
                return "What're you waiting for? You should've subletted long ago - " + String(percentage) + "% match for the next 5 years!";
        }
        else{
            return "Friends? Sure, why not? You spend " + String(percentage) + "% of the time together.";
        }
    };

    $scope.styleRow = function(result){
        if(result == "Yes") return {'background-color':'#CFFF19'};
        else return {'background-color':'#FC913A'};
    };
    
    // process the form
    $scope.processForm = function() {
        //check data
        if($scope.my_info.name == null || $scope.mstream == null || $scope.mterm == null || $scope.friend_info.name == null || $scope.fterm == null || $scope.fstream== null){
            $scope.error = "You forgot to fill in something.";
        }
        
        $http({
            method  : 'POST',
            url     : '/postSubmit',
            data    : JSON.stringify({my_program:$scope.my_info.name,
                       my_faculty:$scope.my_info.faculty,
                       my_term: $scope.mterm,
                       my_stream:$scope.mstream,
                       friend_program:$scope.friend_info.name,
                       friend_faculty:$scope.friend_info.faculty,
                       friend_term:$scope.fterm,
                       friend_stream:$scope.fstream}),
            headers : { 'Content-Type': 'application/json' }  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function(data) {
                console.log(data);
                $scope.results = data[1];
                console.log($scope.results);
                $scope.error = null;
                if(results == null){
                    //error?
                    $scope.error = "Something went wrong, check your values?";
                }
            })
        .error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            $scope.error = "Something went wrong, check your values?";
          });
    };
});
