/* authentication */
function auth(username, password) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        document.getElementById("u_token").innerHTML = JSON.parse(
          this.responseText
        ).token;
      } else {
        alert("Error !");
      }
    }
  };

  const data = {
    username: username,
    password: password,
  };

  xhttp.open("POST", "http://127.0.0.1:8000/api/login/", true);
  xhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhttp.send(JSON.stringify(data));
}

/* conversion */
function convert(init_val, final_met) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        document.getElementById("u_result").innerHTML = JSON.parse(
          this.responseText
        ).message;
      } else {
        alert("Error !");
      }
    }
  };

  const data = {
    initial_met: final_met == "C" ? "F" : "C",
    initial_val: init_val,
    final_met: final_met,
  };

  xhttp.open("POST", "http://127.0.0.1:8000/api/converter/", true);
  xhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhttp.setRequestHeader(
    "Authorization",
    document.getElementById("u_token").innerHTML
  );
  xhttp.send(JSON.stringify(data));
}

/* history */
function history() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        document.getElementById("u_history_username").innerHTML = JSON.parse(
          this.responseText
        ).username;
        document.getElementById("u_history_data").innerHTML = JSON.stringify(
          JSON.parse(this.responseText).data,
          undefined,
          2
        );
      } else {
        alert("Error !");
      }
    }
  };

  xhttp.open("GET", "http://127.0.0.1:8000/api/history/", true);
  xhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  xhttp.setRequestHeader(
    "Authorization",
    document.getElementById("u_token").innerHTML
  );
  xhttp.send();
}

/* actions */
document
  .getElementById("u_convert")
  .addEventListener("click", function (event) {
    event.preventDefault();

    var init_val = document.getElementById("u_value").value;
    var init_met = document.getElementById("u_metric").value;

    convert(init_val, init_met);
    history();
  });

document.getElementById("u_auth").addEventListener("click", function (event) {
  event.preventDefault();

  var username = document.getElementById("u_username").value;
  var password = document.getElementById("u_password").value;

  auth(username, password);
});

document
  .getElementById("u_get_history")
  .addEventListener("click", function (event) {
    history();
  });
