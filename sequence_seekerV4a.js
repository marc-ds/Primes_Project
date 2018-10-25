function sendform() {
    var formElement = document.querySelector("form");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/cgi-bin/sequenceSeekerV4a_view.py");
    xhr.timeout = 4294967295;

    function set_loader() {
        document.getElementById("loader").style.visibility='visible';
        document.getElementById("sequence_seeker_table").style.visibility='hidden';
}

    xhr.onload = function () {

        document.getElementById("loader").style.visibility='hidden';
        document.getElementById("sequence_seeker_table").style.visibility='visible';
        document.getElementById("sequence_seeker_table").innerHTML = xhr.responseText;
    };

    xhr.send(new FormData(formElement));
    document.onload = set_loader();

}