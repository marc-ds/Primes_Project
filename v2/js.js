
function sendform() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/v2/sequenceSeekerV2_view.py");
    xhr.timeout = 4294967295;

    function carregou() {document.getElementById("loader").style.visibility='visible';}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker").innerHTML = xhr.responseText;

    };

    xhr.send(new FormData(formElement));
    document.onload = carregou();

}