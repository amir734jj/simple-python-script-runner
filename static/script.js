angular.module('myApp', [])
.controller('newScript', ["$scope", function($scope) {

    // Initialize ace.js
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
        maxLines: 15
    });

    // Get editor value
    $scope.getScriptText = () => editor.getSession().getValue();

    // Returns editor code
    $scope.script = $scope.getScriptText();

    // Listen to change
    editor.on("change", function() {
        $scope.script = $scope.getScriptText();
        $scope.$apply();
    });
}]);