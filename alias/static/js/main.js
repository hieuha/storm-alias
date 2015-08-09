function Alias($scope, $http) {
    $scope.version = "0.0.1";
    $scope.state = {
        action: "Add new",
        position: localStorage.getItem("position") == "top" ? "top" : ""
    };

    function fetch(callback) {
        $http.get("/list").success(function(data) {
            $scope.aliases = data;
            if (callback) callback();
        });
    }

    function plural() {
        $scope.aliases.plural = $scope.aliases.length > 1 ? "es" : "";
    }

    function focus() {
        var name = document.getElementById("name");
        name.focus();
        name.select();
    }

    $scope.save = function() {
        if (!$scope.name || !$scope.command) {
            alert("you must fill all fields!");
            return focus();
        }
        alias = JSON.stringify({
            name: $scope.name,
            command: $scope.command,
            status: $scope.status ? ($scope.status) : false
        });
        console.log(alias);
        if ($scope.state.editIndex > -1) {
            $http.put('/update', alias).
            success(function(data, status) {
                console.log(data);
                if (status == 200) {
                    $scope.aliases[$scope.state.editIndex] = {
                        name: $scope.name,
                        command: $scope.command,
                        status: $scope.status
                    }
                    $scope.name = $scope.command = "";
                    $scope.status = false;
                    $scope.state.editIndex = -1;
                    $scope.state.action = "Add new";
                    focus();
                    fetch();
                } else {
                    alert("something wrong...");
                }
            }).error(function() {
                alert("something wrong...");
            });

        } else {
            $http.put('/update', alias).
            success(function(data, status) {
                if (status == 200) {
                    $scope.aliases.push({
                        name: $scope.name,
                        command: $scope.command,
                        status: $scope.status
                    });
                    $scope.name = $scope.command = "";
                    $scope.status = false;
                    $scope.state.action = "Add new";
                    focus();
                    fetch(plural);
                } else {
                    alert("something wrong...");
                }
            }).error(function() {
                alert("something wrong...");
            });
        }
    };


    $scope.toggleTop = function() {
        var current = $scope.state.position;
        var next = current == "top" ? "bottom" : "top";
        localStorage.setItem("position", next);
        $scope.state.position = next;
    };


    $scope.edit = function(alias, index) {
        $scope.state.editIndex = index;
        $scope.state.action = "Edit " + alias.name;
        $scope.name = alias.name;
        $scope.command = alias.command;
        if (alias.status == 1) {
            $scope.status = true;
        } else {
            $scope.status = false;
        }
        $scope.reset();
        alias.editing = true;
        focus();
    };

    $scope.delete = function(alias) {
        $http.post("/delete", JSON.stringify({
            name: alias.name
        })).
        success(function() {
            fetch(function() {
                plural();
                $scope.name = $scope.command = "";
                $scope.status = false;
                $scope.reset();
            });
        })
    };

    $scope.reset = function() {
        $scope.aliases = $scope.aliases.map(function(alias) {
            alias.editing = false;
            return alias;
        });
        plural();
    };

    $scope.aliases = [];
    fetch(plural);
    $scope.reset();
}
