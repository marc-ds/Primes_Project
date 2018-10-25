
function sendform() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV2_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {document.getElementById("loader").style.visibility='visible';}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}

function sendformv3() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV3_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {
        document.getElementById("loader").style.visibility='visible';
        document.getElementById("sequence_seeker_table").style.visibility='hidden';
}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker_table").style.visibility='visible';
        document.getElementById("sequence_seeker_form").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}

function sendformv3a() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV3a_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {
        document.getElementById("loader").style.visibility='visible';
        document.getElementById("sequence_seeker_table").style.visibility='hidden';
}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker_table").style.visibility='visible';
        document.getElementById("sequence_seeker_form").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}

function sendformv4() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV4_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {
        document.getElementById("loader").style.visibility='visible';
        document.getElementById("sequence_seeker_table").style.visibility='hidden';
}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker_table").style.visibility='visible';
        document.getElementById("sequence_seeker_form").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}